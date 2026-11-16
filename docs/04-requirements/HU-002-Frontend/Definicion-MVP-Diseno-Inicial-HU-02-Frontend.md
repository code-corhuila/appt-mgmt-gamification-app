# Definición del MVP y Diseño Inicial: HU-002 - Login (Frontend)

Este documento define la estructura visual mínima y los estados de la interfaz para el MVP.

## Componentes de la Interfaz (Compose)
- **Cabecera:** Logo de "Salud Activa" o "GestionTurnosApp".
- **Formulario:**
    - `OutlinedTextField` para Email (KeyboardType.Email).
    - `OutlinedTextField` para Contraseña (VisualTransformation.Password).
    - Botón "Iniciar Sesión" (Primary Button).
- **Acciones Secundarias:**
    - Texto interactivo "¿Olvidaste tu contraseña?".
    - Texto interactivo "¿No tienes cuenta? Regístrate".

## Estados de la UI (UI State)
```kotlin
data class LoginUiState(
    val email: String = "",
    val password: String = "",
    val isLoading: Boolean = false,
    val errorMessage: String? = null,
    val isLoginSuccessful: Boolean = false
)
```

## Paleta de Colores y Estilo
- Seguir las guías de Material 3 definidas en el proyecto.
- Uso de colores primarios para botones de acción.
- Feedback de error en color `error` de la paleta del tema.

## Wireframe Conceptual
1. [Logo Central]
2. [Input: Email]
3. [Input: Password]
4. [Button: Login]
5. [Link: Register]
