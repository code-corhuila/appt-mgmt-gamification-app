# Criterios de Aceptación: HU-001 - Registro de Usuario (Backend)

Estos criterios definen cuándo el trabajo del backend para esta HU se considera terminado desde una perspectiva funcional y técnica.

## Criterios de Aceptación

### Escenario 1: Registro Exitoso vía API
- **Dado** que el frontend envía una solicitud `POST` válida a `/api/auth/register`.
- **Cuando** los datos no existen previamente en la base de datos.
- **Entonces** el sistema debe responder con un código HTTP `201`.
- **Y** debe persistir el usuario en MongoDB con la contraseña hasheada (no en texto plano).

### Escenario 2: Intento de Registro con Email Duplicado
- **Dado** que el correo electrónico ya está registrado en el sistema.
- **Cuando** se intenta realizar un nuevo registro con ese mismo correo.
- **Entonces** el sistema debe denegar la creación.
- **Y** debe responder con un código HTTP `409` y un mensaje claro de conflicto.

### Escenario 3: Validación de Datos de Entrada
- **Dado** que el request body contiene un email mal formado o una contraseña vacía.
- **Cuando** se procesa la solicitud.
- **Entonces** el sistema debe responder con un código HTTP `400`.
- **Y** debe devolver una lista de los errores de validación específicos.

### Escenario 4: Seguridad de Persistencia
- **Dado** un registro exitoso.
- **Cuando** se consulta la base de datos directamente.
- **Entonces** el campo `password` debe contener un hash ilegible generado por `bcrypt`.

## Definición de "Hecho" (DoD) para Backend
- [ ] Código subido al repositorio y revisado por pares.
- [ ] Pruebas unitarias pasando al 100%.
- [ ] Endpoint probado exitosamente con Postman/Insomnia.
- [ ] Documentación del endpoint actualizada.
