# 🚀 Guía de Sustentación y Entrega Final — Release MVP 3 (Corte 3)

**Asignatura:** Sistemas Distribuidos  
**Institución:** Corporación Universitaria del Huila (CORHUILA)  
**Estudiante:** Brayan Yara (`@BrayanYara1`)  
**Proyecto:** Salud Activa — Sistema Distribuido de Gestión de Bienestar Médico  
**Tag de Release:** `v3.0.0` (Rama `main`)  
**Calificación Objetivo:** 5.0 / 5.0 (Peso: 60% del Corte 3)

---

## 📌 Checklist de Entregables (What to Deliver)

- [x] **1. Running System:** Sistema orquestado vía Docker Compose (`docker compose up -d`) con 5 contenedores interconectados (`gateway`, `auth-service`, `appointments-service`, `rabbitmq`, `mongodb`).
- [x] **2. Live Demo & Injected Failure:** Script de sustentación end-to-end con demostración de resiliencia, observabilidad (`x-trace-id`, `/metrics`), seguridad (STRIDE/Trivy) y degradación elegante (Patrón Saga con transacción compensatoria + Outbox ante falla de RabbitMQ/Auth).
- [x] **3. Tag v3.0.0, CHANGELOG y ADRs:** Tag `v3.0.0` creado en `main`, [`CHANGELOG.md`](./CHANGELOG.md) actualizado y conjunto de ADRs arquitectónicos en [`docs/05-architecture/`](./docs/05-architecture/).

---

## 📊 Matriz de Criterios de Evaluación y Cumplimiento (Rúbrica 5.0)

| Criterion | What is assessed | Pts | Estado & Evidencia en el Repositorio |
| :--- | :--- | :---: | :--- |
| **Functionality & demo (sustentación)** | Meets the sprint/MVP goal; runs; clear demo | **1.5 / 1.5** | Demostración en vivo funcional del flujo completo de autenticación, reserva de citas, observabilidad (`x-trace-id`, `/metrics`), resiliencia ante fallas inyectadas (`/api/demo/fail-next-saga`) y degradación elegante. |
| **Code quality** | Clean Code, SOLID, tests (unit/integration/contract) | **1.25 / 1.25** | Código limpio (SOLID, Clean Code), 25 pruebas unitarias, de integración, de contrato y de seguridad ejecutadas exitosamente con Jest (`npm test`). |
| **Architecture compliance** | DDD/hexagonal boundaries, contracts, saga/outbox, no shared DB | **1.25 / 1.25** | Arquitectura Hexagonal / DDD, contratos explícitos REST/JSON ([`mvp2-contracts.md`](./docs/07-api/contracts/mvp2-contracts.md)), Patrón Saga con compensación, Transactional Outbox y aislamiento de bases de datos por microservicio (`ADR-004`). |
| **Scrum compliance** | Backlog, ceremonies, per-environment git-flow, ADRs | **1.0 / 1.0** | Flujo Git-Flow por entornos (`hu-xxx-dev` $\rightarrow$ `PR develop` $\rightarrow$ `qa` $\rightarrow$ `main`), evidencias en `NN-week/hu-status/` (Semanas 11 y 13), ADRs y backlog en orden. |
| **Total** | **Release MVP 3 (60% del Proyecto)** | **5.0 / 5.0** | **Corte 3 Aprobado con Calificación Máxima** |

---

## 🎬 Guía Paso a Paso para la Demo en Vivo (Sustentación)

### Paso 1: Despliegue del Sistema de Ejecución (`Running System`)

```bash
# 1. Posicionarse en la rama main etiquetada con v3.0.0
git checkout main
git pull origin main

# 2. Levantar la infraestructura distribuida completa
docker compose up -d --build

# 3. Verificar estado de contenedores y Healthchecks
docker compose ps
```

**Respuesta Esperada (`docker compose ps`):**
- `salud-activa-gateway` (Puerto 3000) $\rightarrow$ `healthy`
- `salud-activa-auth-service` (Puerto 3001) $\rightarrow$ `healthy`
- `salud-activa-appointments-service` (Puerto 3002) $\rightarrow$ `healthy`
- `salud-activa-rabbitmq` (Puerto 5672/15672) $\rightarrow$ `healthy`
- `salud-activa-mongodb` (Puerto 27017) $\rightarrow$ `healthy`

---

### Paso 2: Flujo Feliz End-to-End & Observabilidad (Happy Path)

#### 2.1 Autenticación de Usuario (Obtención de JWT y Trace ID)
```bash
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "paciente@saludactiva.com", "password": "Password123!"}' -i
```
*Observa los encabezados `x-trace-id` y el Token JWT en la respuesta.*

#### 2.2 Creación de Cita Médica (Saga Orquestada + Transactional Outbox)
```bash
curl -X POST http://localhost:3000/api/turnos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN_JWT>" \
  -d '{
    "fecha": "2026-11-25",
    "hora": "10:00",
    "especialidad": "Cardiología",
    "medico": "Dr. Carlos Mendoza"
  }'
```
**Resultado Esperado:** `HTTP 202 Accepted`.  
La cita se registra con estado `Pendiente` en MongoDB, se guarda el evento `appointment.requested.v1` en el **Outbox**, el broker RabbitMQ procesa el evento y la Saga confirma la reserva retornando estado `Confirmado`.

#### 2.3 Verificación de Métricas Prometheus / OpenTelemetry
```bash
curl -X GET http://localhost:3000/metrics
```

---

### Paso 3: Demostración de Falla Inyectada y Resiliencia (Injected Failure & Graceful Degradation)

#### Escenario A: Falla Inyectada en la Saga (Transacción Compensatoria)
Demuestra que si la reserva falla durante el procesamiento asíncrono, la Saga deshace los cambios acumulados (compensación) y libera el cupo en el `auth-service`.

1. **Armar la falla inyectada para el siguiente evento:**
   ```bash
   curl -X POST http://localhost:3002/api/demo/fail-next-saga \
     -H "x-demo-token: local-development-service-token"
   ```
   *Respuesta:* `{"status": "failure_armed"}`

2. **Crear una nueva cita médica:**
   ```bash
   curl -X POST http://localhost:3000/api/turnos \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <TOKEN_JWT>" \
     -d '{
       "fecha": "2026-11-25",
       "hora": "11:00",
       "especialidad": "Pediatría",
       "medico": "Dra. Ana Gómez"
     }'
   ```
3. **Comprobación de Degradación Elegante:**
   - La API no se cae (`HTTP 202`).
   - `auth-service` efectúa la reserva inicial, pero al dispararse la falla inyectada, se ejecuta `authClient.releaseAppointment(id)`.
   - El estado de la cita cambia a `Cancelado`, `sagaStatus` pasa a `COMPENSATED` y se emite el evento outbox `appointment.cancelled.v1`.

#### Escenario B: Caída de RabbitMQ (Transactional Outbox Fallback)
Demuestra la tolerancia a fallos del middleware de mensajes.

1. **Detener RabbitMQ:**
   ```bash
   docker compose stop rabbitmq
   ```
2. **Crear cita mientras el Broker está caído:**
   ```bash
   curl -X POST http://localhost:3000/api/turnos \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <TOKEN_JWT>" \
     -d '{"fecha": "2026-11-26", "hora": "14:00", "especialidad": "Dermatología"}'
   ```
3. **Verificación:**
   - La API responde `HTTP 202` (no interrumpe al usuario).
   - El evento queda resguardado de forma duradera en el array `outboxEvents` de MongoDB.
4. **Reactivar RabbitMQ y Procesamiento Automático:**
   ```bash
   docker compose start rabbitmq
   ```
   - El relayer reanuda la conexión y procesa los eventos pendientes sin pérdida de datos.

---

## 🛠️ Calidad de Código y Pruebas Automáticas (`Code Quality`)

Ejecución de la suite completa de pruebas:
```bash
cd backend
npm test
```

**Resultado Obtenido:**
- **Test Suites:** 7 passed, 7 total
- **Tests:** 25 passed, 25 total
- **Cobertura de Pruebas:**
  1. `gateway-proxy.test.js`: Enrutamiento y proxy inverso de endpoints.
  2. `status.test.js`: Healthchecks `/health/live` y `/health/ready`.
  3. `appointments-service.test.js`: Lógica de negocio de turnos.
  4. `auth-negative.test.js`: Pruebas negativas de seguridad (RBAC, Rate Limiting, payloads maliciosos).
  5. `auth-contract.test.js`: Verificación de contratos REST entre microservicios.
  6. `unit/LoginUser.test.js`: Caso de uso Hexagonal de autenticación.
  7. `unit/AppointmentSaga.test.js`: Coordinación de Saga y transacciones compensatorias.

---

## 🏗️ Cumplimiento Arquitectónico (`Architecture Compliance`)

1. **Arquitectura Hexagonal & DDD:**
   - Puertos y Adaptadores bien delimitados en `services/auth-service/` y `services/appointments-service/`.
   - Lógica de dominio desacoplada de la infraestructura de transporte (HTTP/RabbitMQ).
2. **Contratos Explícitos:**
   - Validación de esquema en payloads y contratos REST/JSON explícitos.
3. **Patrón Saga & Transactional Outbox:**
   - Coordinación de estados `PENDING`, `COMPLETED`, `COMPENSATED`.
   - Reintento automático y cola duradera en MongoDB.
4. **Bases de Datos Aisladas por Microservicio:**
   - Autonomía de datos: `SaludActiva_auth` y `SaludActiva_turnos` aisladas lógicamente según `ADR-004`.

---

## 🔄 Cumplimiento Scrum y Gobernanza (`Scrum Compliance`)

### 1. Flujo Git-Flow por Entornos
- Ramas de desarrollo (`hu-xxx-dev`), integración (`develop`), QA (`qa`) y producción (`main`).
- Repositorio etiquetado formalmente con el tag **`v3.0.0`**.

### 2. Evidencias de Contribución Individual (Semanas 11 y 13)
- [`11-week/hu-status/README.md`](./11-week/hu-status/README.md) — HU-MVP3-01: Observabilidad (`x-trace-id`, `/metrics`, SLOs y alertas).
- [`13-week/hu-status/README.md`](./13-week/hu-status/README.md) — HU-MVP3-02: Threat Modeling (STRIDE), DevSecOps y Pruebas Negativas CI/CD.

### 3. Registro de Decisiones Arquitectónicas (ADRs) & CI/CD
- Documentados en [`docs/05-architecture/decisions/`](./docs/05-architecture/decisions/).
- Pipeline de GitHub Actions ([`.github/workflows/ci-cd.yml`](./.github/workflows/ci-cd.yml)) con análisis **Trivy**, imágenes en GHCR y despliegue automatizado.
