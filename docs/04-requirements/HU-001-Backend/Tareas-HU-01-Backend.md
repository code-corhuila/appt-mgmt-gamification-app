# Tareas: HU-001 - Registro de Usuario (Backend)

Este documento detalla las tareas técnicas necesarias para implementar el backend de la HU-001.

## Tareas Técnicas

### 1. Configuración del Entorno y Estructura
- [ ] Inicializar el proyecto Node.js con TypeScript (si no existe).
- [ ] Configurar las variables de entorno (`.env`) para la conexión a MongoDB.
- [ ] Estructurar las carpetas del servidor (`src/controllers`, `src/services`, `src/models`, `src/routes`).

### 2. Modelado de Datos
- [ ] Definir el esquema de Mongoose para `User` (Perfil) en MongoDB.
- [ ] Implementar validaciones a nivel de esquema (email único, campos requeridos).

### 3. Implementación de Lógica de Negocio (Servicios)
- [ ] Crear el servicio de autenticación.
- [ ] Implementar la función de hashing de contraseñas usando `bcrypt`.
- [ ] Implementar la lógica para verificar si un usuario ya existe antes de crearlo.

### 4. Desarrollo de Endpoints (Controladores y Rutas)
- [ ] Crear el endpoint `POST /api/auth/register`.
- [ ] Implementar validaciones de entrada usando `express-validator`.
- [ ] Manejar respuestas exitosas (201 Created) y errores (400 Bad Request, 409 Conflict).

### 5. Pruebas y Verificación
- [ ] Escribir pruebas unitarias para el servicio de registro.
- [ ] Realizar pruebas de integración del endpoint con una base de datos de prueba.
- [ ] Verificar el almacenamiento correcto de la contraseña hasheada.

### 6. Documentación
- [ ] Actualizar la documentación de la API en Postman o Swagger.
