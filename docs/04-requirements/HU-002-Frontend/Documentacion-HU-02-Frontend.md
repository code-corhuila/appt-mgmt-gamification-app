# Documentación: HU-002 - Login (Frontend)

Documentación técnica sobre la arquitectura y patrones utilizados en el módulo de Login.

## Arquitectura (MVVM)
- **View:** `LoginScreen.kt` (Composables). Observa el estado del ViewModel.
- **ViewModel:** `LoginViewModel.kt`. Gestiona la lógica de UI y llamadas al repositorio mediante Coroutines.
- **Model/Repository:** `AuthRepository.kt`. Abstrae la fuente de datos (Retrofit).

## Integración con API
- **Endpoint:** `POST /api/auth/login`.
- **Headers:** `Content-Type: application/json`.
- **Manejo de Errores:** 
    - 401: Credenciales incorrectas.
    - 400: Datos mal formados.
    - 500: Error de servidor.

## Persistencia de Sesión
- Se utilizará **Jetpack DataStore** para almacenar el `access_token` de forma asíncrona y segura.
- Se implementará un `AuthInterceptor` en OkHttp para adjuntar automáticamente el token a futuras peticiones protegidas.

## Navegación
- Uso de `androidx.navigation.compose`.
- Ruta: `login_route`.
- Al autenticar, se utiliza `popUpTo` para eliminar el Login del historial.
