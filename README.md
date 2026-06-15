### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

- [FastAPI](https://fastapi.tiangolo.com)
- [Uvicorn](https://uvicorn.dev/)
- [Psycopg](https://www.psycopg.org/)
- [Python-multipart](https://github.com/Kludex/python-multipart)
- [PostgreSQL](https://www.postgresql.org/)
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
### Prerequisites

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
## Acknowledgments

Principalement fait en utilisant ce tutoriel:


- [FastAPI Backend with PostgreSQL: Step By Step Guide for Beginners](https://sharajman.com/blogs/fastapi-backend-with-postgresql-step-by-step-guide-for-beginners/)
