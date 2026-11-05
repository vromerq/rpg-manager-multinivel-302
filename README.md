# RPG Manager - Arquitectura multinivel

Aplicación Flask para gestionar personajes de un RPG, organizada por capas:

- `app.py`: controlador (rutas)
- `services/`: validaciones y reglas de negocio
- `repository/`: acceso a datos
- `models/`: clases del dominio
- `templates/`: vistas HTML
- `db/`: scripts de MySQL y MongoDB