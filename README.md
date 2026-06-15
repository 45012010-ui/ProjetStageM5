### Frameworks et extensions utilisées

- [FastAPI](https://fastapi.tiangolo.com)
- [Uvicorn](https://uvicorn.dev/)
- [Psycopg](https://www.psycopg.org/)
- [Python-multipart](https://github.com/Kludex/python-multipart)
- [PostgreSQL](https://www.postgresql.org/)

### Étapes

Créez un environnement virtuel dans la racine du fichier.

  ```sh
  python -m venv venv
  ```

Lancez l'environnement virtuel.
- Sur macOS/Linux
  ```sh
  source venv/bin/activate
  ```

- Sur Windows
  ```sh
  venv\Scripts\activate
  ```

Installez les dépendences du programme dans le fichier   ```requirements.txt```.

  ```sh
  pip install -r requirements.txt
  ```

Lancez l'application.
  ```sh
  uvicorn app.main:app --reload
  ```

Ouvrez la page ```http://127.0.0.1:8000/docs``` pour voir la documentation du projet.

Quand vous avez fini d'utiliser l'application, utilisez cette commande pour fermer l'environnement virtuel.
  ```sh
  deactivate
  ```
## Sources

Principalement fait en utilisant ce tutoriel:


- [FastAPI Backend with PostgreSQL: Step By Step Guide for Beginners](https://sharajman.com/blogs/fastapi-backend-with-postgresql-step-by-step-guide-for-beginners/)
