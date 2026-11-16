# Tareas: HU-002 - Login (Frontend)

Este documento detalla las tareas técnicas necesarias para implementar la interfaz y lógica de inicio de sesión.

## Tareas Técnicas

### 1. Diseño y UI (Compose)
- [ ] Crear el layout de la pantalla de Login usando Jetpack Compose.
- [ ] Implementar campos de texto para `Email` y `Password` con soporte para visibilidad de contraseña.
- [ ] Agregar validaciones visuales en tiempo real (campos requeridos, formato de email).
- [ ] Implementar estados de carga (ProgressBar) y mensajes de error (Snackbars/Toasts).

### 2. Lógica de Presentación (ViewModel)
- [ ] Crear `LoginViewModel` para gestionar el estado de la UI (`LoginState`).
- [ ] Implementar la validación de entrada antes de llamar al repositorio.
- [ ] Manejar la navegación hacia la pantalla principal tras un login exitoso.

### 3. Capa de Datos e Integración
- [ ] Definir el `AuthRepository` y su implementación.
- [ ] Configurar la llamada al endpoint de backend `POST /api/auth/login` usando Retrofit.
- [ ] Implementar el almacenamiento seguro del token JWT (DataStore o EncryptedSharedPreferences).

### 4. Navegación
- [ ] Configurar la ruta de Login en el `NavHost` de la aplicación.
- [ ] Implementar lógica de redirección si el usuario ya tiene una sesión activa al abrir la app.

### 5. Pruebas y Calidad
- [ ] Escribir pruebas unitarias para el `LoginViewModel`.
- [ ] Realizar pruebas de UI (UI Tests) para verificar el flujo de login fallido y exitoso.
- [ ] Verificar la accesibilidad de los componentes de la pantalla.
