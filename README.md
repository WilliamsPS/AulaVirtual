# AulaVirtual

Este proyecto es un esqueleto de un aula virtual compuesto por:

- **Backend:** API REST en Flask con acceso a PostgreSQL y MongoDB.
- **Frontend:** Aplicación Angular CLI.
- **Bases de datos:** PostgreSQL y MongoDB.
- **Docker:** Todo el stack se ejecuta con Docker mediante `docker-compose`.

## Uso rápido

1. Construir y levantar los contenedores:
   ```bash
   docker-compose up --build
   ```

2. Acceder al frontend en [http://localhost:4200](http://localhost:4200) y al backend en [http://localhost:5000](http://localhost:5000).

Este es solo un punto de partida mínimo. Se deben implementar la lógica de autenticación, las operaciones sobre la base de datos y las vistas de la aplicación.
