# Vezetos Assignment
FastAPI application that acts as a data warehouse, collecting and synchronizing data from multiple external APIs, handling webhook inputs, and providing efficient data retrieval. The application is managing background tasks for data synchronization without relying on Celery with inbuild FastAPI Background Job Functionality.

# Pre-requisites

- Install [Python] version 3.10.0

# Getting started

- Clone the repository

```
git clone https://github.com/TanV060892/vezetos.git
```

- Install dependencies

```
pip install -r requirements.txt
```

- Build and run the project

```
On Windows :
python -m venv venv
.\venv\Scripts\activate
uvicorn main:app --reload
```


- Health Check

  Endpoint : http://localhost:8000/

## API Documentation

```
https://documenter.getpostman.com/view/29641974/2sAXqs7N6E

```

- `POST /webhook`: Receives webhook data.
- `GET /data`: Retrieves CRM and Marketing data with pagination.
- `GET /sync/{source}`: Triggers sync for CRM or Marketing.
- `GET /tasks`: Lists running tasks.
- `POST /tasks/cancel`: Cancels a background task.
