# Module M5 — API principale et orchestration

## Objectif

Le module M5 sert d’API principale pour le projet d’analyse de propositions citoyennes.

Son rôle est d’orchestrer les autres modules du projet et d’exposer des endpoints centralisés pour les tests Swagger ou pour un futur dashboard.

M5 ne recrée pas les tables de la base de données.
La base PostgreSQL et le schéma sont gérés par le module M1.

## Modules intégrés

Le module M5 orchestre actuellement :

* M1 : base PostgreSQL et données des contributions
* M2 : recherche sémantique avec pgvector
* M3 : analyse NLI entre deux propositions

## Structure du projet

```text
ProjetStageM5-main/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   └── routers/
│       ├── __init__.py
│       ├── health.py
│       ├── semantic_search.py
│       └── nli.py
│
├── .env.example
├── requirements.txt
└── README_M5.md
```

## Variables d’environnement

Créer un fichier `.env` à partir de `.env.example`.

Exemple de `.env.example` :

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/consultation_db

M2_API_URL=http://127.0.0.1:8000
M3_API_URL=http://127.0.0.1:8001
```

## Installation

Depuis le dossier M5 :

```bash
pip install -r requirements.txt
```

## Lancement des modules

Avant de lancer M5, la base M1 doit être active.

Depuis le dossier M1 :

```bash
docker compose up -d postgres
```

Lancer ensuite M2 sur le port 8000 :

```bash
python -m uvicorn src.search_api:app --reload --port 8000
```

Lancer M3 sur le port 8001 :

```bash
python -m uvicorn src.main:app --reload --port 8001
```

Puis lancer M5 sur le port 8002 :

```bash
python -m uvicorn app.main:app --reload --port 8002
```

Swagger M5 est disponible ici :

```text
http://127.0.0.1:8002/docs
```

## Endpoints disponibles

### Racine

```http
GET /
```

Réponse :

```json
{
  "message": "API principale M5",
  "status": "running"
}
```

### Santé de l’API

```http
GET /health
```

Réponse :

```json
{
  "status": "ok",
  "module": "M5 API orchestration"
}
```

### Santé de la base PostgreSQL

```http
GET /health/db
```

Réponse :

```json
{
  "status": "ok",
  "database": "connected"
}
```

## Recherche sémantique via M2

```http
POST /semantic-search/search
```

Body :

```json
{
  "query": "lutter contre le spam et les publicités abusives",
  "k": 5
}
```

Réponse attendue :

```json
{
  "query": "lutter contre le spam et les publicités abusives",
  "k": 5,
  "results": [
    {
      "id": "uuid",
      "source_id": "529",
      "titre": "Titre de la proposition",
      "corps": "Texte de la proposition",
      "categorie": "Catégorie",
      "distance": 0.35,
      "similarite": 0.64
    }
  ]
}
```

Cette route M5 appelle le module M2 à l’adresse définie dans `M2_API_URL`.

## Analyse NLI via M3

```http
POST /nli/analyze
```

Body :

```json
{
  "proposal_a_id": "f013cc90-5efb-4298-bcc0-34bd6124e415",
  "proposal_b_id": "304b61a4-0d2e-477d-a329-cc30fee48bc8"
}
```

Réponse attendue :

```json
{
  "proposal_a_id": "f013cc90-5efb-4298-bcc0-34bd6124e415",
  "proposal_b_id": "304b61a4-0d2e-477d-a329-cc30fee48bc8",
  "relation": "neutre",
  "score": 0.99,
  "similarity_m2": 0.0,
  "model": "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli",
  "latency_ms": 23742
}
```

Cette route M5 appelle le module M3 à l’adresse définie dans `M3_API_URL`.

## État actuel

* API M5 fonctionnelle
* Swagger disponible
* Connexion PostgreSQL testée
* Endpoint `/health` fonctionnel
* Endpoint `/health/db` fonctionnel
* Intégration M2 fonctionnelle
* Intégration M3 fonctionnelle
* M5 joue le rôle d’API centrale d’orchestration

## Points d’attention

M5 doit être lancé après M1.

Pour tester les routes M2 et M3 via M5, il faut aussi que les APIs M2 et M3 soient lancées :

```text
M2 → http://127.0.0.1:8000
M3 → http://127.0.0.1:8001
M5 → http://127.0.0.1:8002
```

Ne pas inclure dans le rendu :

```text
.env
.venv/
venv/
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
```
