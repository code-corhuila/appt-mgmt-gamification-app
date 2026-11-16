const request = require('supertest');
const express = require('express');
const jwt = require('jsonwebtoken');

// Mock API Gateway Application setup for security unit testing
const JWT_SECRET = 'test-security-secret-key-2026';

function createTestGateway() {
  const app = express();
  app.use(express.json());

  // Authorization verification middleware
  const verifyTokenAndRole = (requiredRole) => (req, res, next) => {
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({ error: 'Missing or malformed Authorization header' });
    }

    const token = authHeader.split(' ')[1];
    try {
      const decoded = jwt.verify(token, JWT_SECRET);
      req.user = decoded;

      if (requiredRole && decoded.role !== requiredRole) {
        return res.status(403).json({ error: 'Forbidden: Insufficient privileges for requested route' });
      }

      next();
    } catch (err) {
      return res.status(403).json({ error: 'Forbidden: Invalid or expired token signature' });
    }
  };

  // Turnos booking creation endpoint (Requires 'patient' or 'admin' role)
  app.post('/api/turnos', verifyTokenAndRole('patient'), (req, res) => {
    res.status(201).json({ status: 'SUCCESS', message: 'Appointment booked successfully' });
  });

  // Admin-only system endpoint
  app.delete('/api/turnos/admin/purge', verifyTokenAndRole('admin'), (req, res) => {
    res.status(200).json({ status: 'SUCCESS', message: 'Purged schedule logs' });
  });

  // Specific appointment endpoint checking cross-resource ownership (M1)
  const mockAppointments = {
    'appt-100': { ownerId: 'patient_123', especialidad: 'Cardiologia' }
  };

  app.get('/api/turnos/:id', verifyTokenAndRole('patient'), (req, res) => {
    const appt = mockAppointments[req.params.id];
    if (!appt) return res.status(404).json({ error: 'Appointment not found' });
    if (appt.ownerId !== req.user.sub) {
      return res.status(403).json({ error: 'Forbidden: Resource belongs to another user' });
    }
    return res.status(200).json({ status: 'SUCCESS', appointment: appt });
  });

  return app;
}

describe('Negative Security Authorization Tests — TB1 Gateway Perimeter', () => {
  let app;

  beforeAll(() => {
    app = createTestGateway();
  });

  test('1. Unauthenticated request to /api/turnos MUST fail with 401 Unauthorized', async () => {
    const response = await request(app)
      .post('/api/turnos')
      .send({ especialidad: 'Cardiologia', fecha: '2026-11-01' });

    expect(response.status).toBe(401);
    expect(response.body.error).toContain('Missing or malformed Authorization header');
  });

  test('2. Request with tampered/forged JWT signature MUST fail with 403 Forbidden', async () => {
    const forgedToken = jwt.sign({ sub: 'user123', role: 'patient' }, 'WRONG_SECRET_KEY');

    const response = await request(app)
      .post('/api/turnos')
      .set('Authorization', `Bearer ${forgedToken}`)
      .send({ especialidad: 'Cardiologia', fecha: '2026-11-01' });

    expect(response.status).toBe(403);
    expect(response.body.error).toContain('Forbidden: Invalid or expired token');
  });

  test('3. Patient user attempting to invoke Admin purge endpoint MUST fail with 403 Forbidden', async () => {
    const patientToken = jwt.sign({ sub: 'patient_456', role: 'patient' }, JWT_SECRET);

    const response = await request(app)
      .delete('/api/turnos/admin/purge')
      .set('Authorization', `Bearer ${patientToken}`);

    expect(response.status).toBe(403);
    expect(response.body.error).toContain('Insufficient privileges');
  });

  test('4. Cross-ownership violation (M1): User 2 attempting to access User 1 resource MUST fail with 403 Forbidden', async () => {
    const userTwoToken = jwt.sign({ sub: 'patient_789_other_user', role: 'patient' }, JWT_SECRET);

    const response = await request(app)
      .get('/api/turnos/appt-100')
      .set('Authorization', `Bearer ${userTwoToken}`);

    expect(response.status).toBe(403);
    expect(response.body.error).toContain('Resource belongs to another user');
  });
});
