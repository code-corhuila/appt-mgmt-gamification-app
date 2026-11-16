# Criterios de Aceptación: HU-002 - Login (Frontend)

Estos criterios definen cuándo el frontend del Login se considera funcionalmente correcto y listo para producción.

## Criterios de Aceptación

### Escenario 1: Validación Visual de Campos
- **Dado** que el usuario deja el campo de email vacío.
- **Cuando** intenta pulsar el botón de login.
- **Entonces** el botón debe estar deshabilitado O mostrar un mensaje de error indicando "El campo es requerido".

### Escenario 2: Feedback de Carga
- **Dado** que el usuario ingresa credenciales válidas y pulsa "Iniciar Sesión".
- **Cuando** la petición está en curso.
- **Entonces** se debe mostrar un indicador de carga (CircularProgressIndicator) y los inputs deben quedar bloqueados para evitar ediciones.

### Escenario 3: Manejo de Error de Autenticación
- **Dado** que el backend responde con un error 401 (Unauthorized).
- **Cuando** el frontend recibe la respuesta.
- **Entonces** debe ocultar el cargador y mostrar un mensaje de error claro: "Correo o contraseña incorrectos".

### Escenario 4: Persistencia y Navegación
- **Dado** un login exitoso.
- **Cuando** se recibe el token JWT.
- **Entonces** el sistema debe guardarlo localmente y navegar automáticamente a la pantalla de Inicio (Home).
- **Y** no debe permitir regresar a la pantalla de Login mediante el botón físico/gesto de "atrás".

## Definición de Hecho (DoD)
- [ ] La pantalla cumple con el diseño M3 establecido.
- [ ] El ViewModel tiene cobertura de pruebas unitarias.
- [ ] El flujo completo (Login -> Home) ha sido probado en un emulador/dispositivo real.
- [ ] No existen "hardcoded strings" (uso de `strings.xml`).
