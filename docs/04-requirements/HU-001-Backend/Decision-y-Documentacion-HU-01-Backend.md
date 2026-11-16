# Decisión y Documentación: HU-001 - Registro de Usuario (Backend)

Este documento registra las decisiones técnicas y la documentación del contrato de la API.

## Decisiones Técnicas

### D-001: Algoritmo de Hashing
- **Decisión:** Usar `bcrypt` con un salt factor de 10.
- **Razón:** Equilibrio óptimo entre seguridad y tiempo de procesamiento en el servidor.

### D-002: Almacenamiento de Usuario
- **Decisión:** El modelo de usuario completo residirá en MongoDB.
- **Razón:** Alineación con el ADR-002 para la gestión de perfiles y escalabilidad futura en datos médicos.

### D-003: Validación Previa al Registro
- **Decisión:** La validación de "correo ya existente" se hará en la capa de servicio antes de intentar la persistencia, para manejar el error de forma controlada.

## Documentación del API Endpoint

### Endpoint: Registro de Usuario
- **URL:** `/api/auth/register`
- **Método:** `POST`
- **Auth Requerida:** No

#### Request Body
```json
{
  "email": "usuario@ejemplo.com",
  "password": "Password123!",
  "fullName": "Juan Pérez"
}
```

#### Response Success (201 Created)
```json
{
  "status": "success",
  "message": "User registered successfully",
  "data": {
    "userId": "64f1234567890abcdef12345",
    "email": "usuario@ejemplo.com"
  }
}
```

#### Response Error (409 Conflict)
```json
{
  "status": "error",
  "message": "Account already exists with this email"
}
```
