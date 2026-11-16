# Investigación: HU-001 - Registro de Usuario (Backend)

Este documento contiene los hallazgos de la investigación técnica previa a la implementación.

## Temas de Investigación

### 1. Seguridad de Contraseñas (Hashing)
- **Tecnología:** `bcrypt`.
- **Por qué:** Es el estándar de la industria para resistir ataques de fuerza bruta mediante el uso de "salts" y un factor de costo ajustable.
- **Referencia:** [bcrypt.js documentation](https://www.npmjs.com/package/bcrypt).

### 2. Validación de Entrada de Datos
- **Tecnología:** `express-validator`.
- **Enfoque:** Validar el formato de correo electrónico, longitud mínima de contraseña y sanitizar cadenas de texto para prevenir inyecciones.
- **Referencia:** [express-validator guide](https://express-validator.github.io/docs/).

### 3. Persistencia en MongoDB (Polyglot Persistence)
- **Decisión:** Siguiendo el ADR-002, los perfiles de usuario se almacenan en MongoDB debido a su flexibilidad.
- **Estructura del documento:** Se investigó la mejor forma de indexar el campo `email` para búsquedas rápidas durante el registro.

### 4. Manejo de Errores Global
- **Estrategia:** Implementar un middleware de Express para capturar errores de base de datos (como duplicados de clave única) y devolver códigos HTTP semánticos al frontend.

### 5. Estándares de Respuesta API
- **Formato:** Investigar el uso de JSend o formatos JSON estandarizados para asegurar que el frontend reciba respuestas predecibles tanto en éxito como en fallo.
