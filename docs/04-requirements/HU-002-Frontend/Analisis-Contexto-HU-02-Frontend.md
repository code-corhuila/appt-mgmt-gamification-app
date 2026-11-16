# Análisis de Contexto: HU-002 - Login (Frontend)

Este documento describe el flujo de usuario, el contexto técnico y las consideraciones de seguridad para el frontend.

## Flujo de Usuario
1. El usuario abre la aplicación.
2. Si no hay sesión, se muestra la pantalla de Login.
3. El usuario ingresa credenciales.
4. El sistema valida localmente (campos no vacíos).
5. Se envía la petición al backend.
6. Si es correcto, se guarda el token y se navega al Home.
7. Si falla, se muestra un mensaje descriptivo sin comprometer la seguridad.

## Consideraciones Técnicas
- **Gestión de Sesión:** El token JWT debe persistir para evitar que el usuario se loguee cada vez que abre la app.
- **Seguridad:** No se deben mostrar logs de la contraseña en la consola de depuración.
- **Offline:** La pantalla de login requiere conexión a internet; debe manejarse el error de "Sin conexión".

## Casos de Borde
- El token expira mientras el usuario usa la app (manejo de error 401 global).
- El usuario intenta volver atrás desde el Home al Login (limpiar el backstack).
- Conexión lenta: el botón de login debe deshabilitarse durante la petición para evitar múltiples clics.
