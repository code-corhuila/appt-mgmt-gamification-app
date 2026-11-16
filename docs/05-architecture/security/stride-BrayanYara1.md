<<<<<<< HEAD
# STRIDE Threat Model Analysis — Trust Boundary TB1
=======
# STRIDE Threat Model Analysis — Trust Boundary TB1 (Final Refined Version)
>>>>>>> d3e18f9 (docs(security): address review on STRIDE for External Client to Gateway boundary)

> **Boundary:** `TB1: External Client (Android App) -> API Gateway (backend:3000)`  
> **Author:** Brayan Yara (`@BrayanYara1`)  
> **Date:** October 2026  
<<<<<<< HEAD
> **Project:** Salud Activa — Distributed Medical Appointment System
=======
> **Project:** Salud Activa — Distributed Medical Appointment System  
> **Status:** CP6 Peer Review Addressed & Finalized
>>>>>>> d3e18f9 (docs(security): address review on STRIDE for External Client to Gateway boundary)

---

## 1. Boundary Context & System Architecture

This threat model evaluates **Trust Boundary TB1**, which separates the public untrusted client network (Android Mobile App) from the internal trusted microservice architecture via the API Gateway (`backend:3000`).

```
[ Android Client ] ---> ( Trust Boundary TB1: HTTPS / JWT ) ---> [ API Gateway (backend:3000) ]
```

* **Untrusted Side:** Android Client application running on untrusted end-user mobile devices.
* **Trusted Side:** API Gateway (`backend:3000`) and downstream Node.js microservices (`auth-service:3001`, `appointments-service:3002`).
* **Data Crossing Boundary:** User credentials (`email`, `password`), JWT bearer tokens, patient booking requests (`especialidad`, `fecha`, `medicoId`), and patient health profile queries.
* **Entry Points:** `POST /api/auth/login`, `POST /api/auth/register`, `POST /api/turnos`, `GET /api/turnos/usuario/:id`.

---

## 2. STRIDE Threat Analysis Matrix

| STRIDE Category | Threat Description & Attack Vector | Likelihood (1-3) | Impact (1-3) | Risk Score (L x I) | Existing Controls | Missing Mitigation & Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Spoofing (S)** | An attacker uses a stolen or forged JWT token to spoof a legitimate patient identity on `POST /api/turnos` and schedule appointments in their name. | 2 | 3 | **6 (High)** | JWT signature verification using secret key at Gateway. | **[B]** Implement short-lived access tokens (15m), refresh tokens, and JWT revocation blacklist in Redis (Bishop, 2019, p. 342). |
| **Tampering (T)** | An attacker intercepts and modifies request payload parameters (e.g. altering `pacienteId` or `fecha` to override another patient's slot on `POST /api/turnos`). | 2 | 3 | **6 (High)** | Basic JSON payload parsing in Express middleware. | **[B]** Enforce server-side request payload schema validation using Joi/Zod and cryptographically bind `pacienteId` to token claims. |
| **Repudiation (R)** | A patient books or cancels a medical appointment on `/api/turnos` and later denies making the request, causing scheduling conflicts and administrative disputes. | 2 | 2 | **4 (Medium)** | Standard HTTP access logs printed to console. | **[B]** Implement an immutable append-only audit trail recording user ID, action, timestamp, and source IP in `SaludActiva_turnos.audit_logs`. |
| **Information Disclosure (I)** | Unhandled backend errors leak stack traces and internal database URI strings to the mobile client on failed API requests. | 2 | 2 | **4 (Medium)** | Standard Express error handling. | Enforce production error sanitization middleware masking stack traces and returning standardized error JSON schemas (`{ code, message }`). |
<<<<<<< HEAD
| **Denial of Service (D)** | An attacker launches an automated script flooding `POST /api/auth/login` and `/api/turnos`, exhausting gateway connection pools and MongoDB connections. | 3 | 3 | **9 (Critical)** | Docker container healthchecks and resource limits. | **[B]** Implement IP-based and user-based rate limiting using `express-rate-limit` (e.g., max 5 login attempts per minute per IP). |
=======
| **Denial of Service (D)** | An attacker launches an automated script flooding `POST /api/auth/login` and `/api/turnos`, exhausting gateway connection pools and MongoDB connections. | 3 | 3 | **9 (Critical)** | Docker container healthchecks and resource limits. | **[B]** Implement IP-based and user-based rate limiting using `express-rate-limit` (e.g., max 10 login attempts per minute per IP). |
>>>>>>> d3e18f9 (docs(security): address review on STRIDE for External Client to Gateway boundary)
| **Elevation of Privilege (E)** | A standard patient user invokes administrative endpoints (e.g. modifying medical specialty catalogs or provider schedules) by bypassing missing scope checks on JWT claims. | 2 | 3 | **6 (High)** | Gateway checks for presence of valid JWT header. | Enforce Role-Based Access Control (RBAC) middleware verifying explicit JWT scopes (`role: patient` vs `role: admin`) on gateway routes. |

---

<<<<<<< HEAD
## 3. Threat Risk Ranking
=======
## 3. Peer Review Response & Refinement Log (CP6)

* **Reviewer Comment Addressed:** *"Peer suggested verifying payload validation and rate-limiting enforcement directly at the API Gateway layer before forwarding traffic to downstream services."*
* **Resolution & Update:** Confirmed that Express rate-limiting middleware (`express-rate-limit`) and Joi schema validation are placed as top-level Express middlewares in `backend/server.js`, protecting downstream `auth-service` and `appointments-service` from unvalidated or flooding requests.

---

## 4. Threat Risk Ranking
>>>>>>> d3e18f9 (docs(security): address review on STRIDE for External Client to Gateway boundary)

1. **Denial of Service (D) — Risk 9 (Critical):** Unrestricted endpoint request rates threaten system availability for all patients.
2. **Spoofing (S) — Risk 6 (High):** Unauthorized account impersonation compromises patient identity integrity.
3. **Tampering (T) — Risk 6 (High):** Parameter alteration allows unauthorized modification of medical appointment schedules.
4. **Elevation of Privilege (E) — Risk 6 (High):** Missing role enforcement enables unauthorized execution of administrative routes.
5. **Repudiation (R) — Risk 4 (Medium):** Lack of structured audit logging prevents non-repudiation of healthcare bookings.
6. **Information Disclosure (I) — Risk 4 (Medium):** Stack trace leakage exposes internal architectural details to potential attackers.

---

<<<<<<< HEAD
## 4. Residual Risk Statement

While implementing JWT validation, rate limiting, and RBAC middleware significantly reduces high-severity vectors across `TB1`, a residual risk remains regarding client-side token storage on rooted Android devices. If a user device is compromised at the OS level, local keys stored in memory or device storage could be extracted. This risk is accepted for MVP 2, as kernel-level mobile OS compromise falls outside the application perimeter and is partially mitigated by enforcing short token expiration windows.

---

## 5. References & Bibliography
=======
## 5. Residual Risk Statement & Trade-off Analysis

While implementing JWT validation, rate limiting, and RBAC middleware significantly reduces high-severity vectors across `TB1`, a residual risk remains regarding client-side token storage on rooted Android devices. If a user device is compromised at the OS level, local keys stored in memory or device storage could be extracted. This risk is accepted for MVP 2, as kernel-level mobile OS compromise falls outside the application perimeter and is partially mitigated by enforcing short token expiration windows (15 minutes).

---

## 6. References & Bibliography
>>>>>>> d3e18f9 (docs(security): address review on STRIDE for External Client to Gateway boundary)

* **[B] Book Reference (CORHUILA Library):**  
  Bishop, Matt. *Computer Security: Art and Science*. 2nd Edition, Addison-Wesley Professional, 2019.  
  *Call Number:* `005.8 B622c` (CORHUILA Physical Library Collection).  
  *Pages referenced:* pp. 340–348 (Chapter 14: Authentication & Key Management) and pp. 512–520 (Chapter 21: Access Control & Delegation Models).

* **OWASP API Security Top 10 (2023):**  
  API1:2023 Broken Object Level Authorization & API2:2023 Broken Authentication.
