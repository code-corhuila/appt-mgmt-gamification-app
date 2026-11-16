# Changelog

Notable changes to Salud Activa are recorded here.

## [3.0.0] - 2026-10-29

### Added
- Production-grade Observability: Trace propagation (`x-trace-id`), structured JSON log contract, `/metrics` endpoint with OpenTelemetry format, defined SLOs and fast-burn alert rules.
- Threat Modeling & DevSecOps Security: STRIDE threat model on Trust Boundary TB1 (API Gateway), IP & User rate limiting middleware, payload schema validation, RBAC security gates, and automated Trivy container security scanning in CI/CD.
- Saga Pattern & Chaos Engineering: Transactional Outbox pattern with RabbitMQ event bus, compensating saga transactions (`appointment.cancelled.v1`), and demo failure injection via `/api/demo/fail-next-saga` showing graceful degradation.
- Production CI/CD Pipeline: GitHub Actions workflow with Docker image validation, Trivy security gate, GHCR package publishing, and EC2 deployment trigger.
- Complete documentation suite: Updated ADRs, Threat Model (STRIDE), Security Backlog, Observability Runbooks, and Sustentación Guide.

## [2.0.0] - 2026-10-08

### Added

- Added a local Docker Compose demo with a persistent MongoDB volume and container health checks.
- Added separate liveness and readiness endpoints and per-domain MongoDB status reporting.
- Added a deterministic test for API behavior while MongoDB is unavailable.

### Changed

- Reused one MongoDB connection for the logical per-domain databases, consistent with ADR-004 and Anexo J.
- Clarified ownership boundaries and documented the legacy domains that remain in the gateway.
- Extracted independently started Auth and Appointments services behind the backwards-compatible API Gateway.
- Added the Auth user/reservation REST contract and the Appointments booking saga with compensating release.
- Added an embedded, durable appointment outbox and RabbitMQ relay with retry/dead-letter handling.
- Preserved the web and Android `/api/auth` and `/api/turnos` routes and corrected the web appointment payload.
