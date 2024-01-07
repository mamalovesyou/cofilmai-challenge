## TikTok Trends Storage and Management Application

This application fetches the latest google trends and convert them into trending hastags, stores them in a PostgreSQL database using prisma, and manages the data retrieval and update process using a FastAPI application. You will find a basic FastAPI application in `services/trends` that you will modify.

No schema are imposed, you are free to come up with your own DB schema as long as you can justify your choices. Prisma is here to simplify your life, it comes with everything you need. Don;t over complicate things.

A docker-compose is provided so you don't have to install postgres on your machine and otehr dependencies.

If something isn't clear feel free to email at matthieu@mentium.io

We will evluate code clarity and good practices.

Bonuses aren't required but are highly encouraged, pick one of them.

## Challenge

- Update api code to generate a `openapi/api.cofilmai.yaml` file using FastAPI
- Uncomment swagger-ui service in the `docker-compose.yml` and make sure your swagger-ui is running properly
- Fetch and store trending posts from TikTok  by country
  1. Create a free account here https://serpapi.com/ and fetch google trends by country
  2. Create an endpoint that list and save trends for a given keyword (Create a Trends model to store trends 
  3. Make trends unique to a user
  4. Create a hastag for each trends and list those hastags for each user (for instance if a trend is real estate, create #realestate)
  5. Add a search endpoint to search trending hashtags

## Bonus
- Come up with a feature of your own!

## Submission
- Fork this repo on your own github
- Once done push your code and email at matthieu@mentium.io

## Getting Started

### Prerequisites

- Python 3.10+
- Docker compose
- [Prisma](https://prisma-client-py.readthedocs.io/en/stable/)
- [Tikntok-Api](https://github.com/davidteather/TikTok-Api)

## Setup virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

## Install requirements

```sh
pip install -r requirements.txt
```

## Start Docker
```sh
docker-compose up
```

## Generate Prisma Client

```sh
prisma generate
```

## Create new Prisma migration schema

Make sure your ddb is running in docker.
```sh
prisma migrate dev --name <migration_name>
```

## Apply migration
```sh
prisma migrate --dev
```

## Start api

```sh
cd services/trends
uvicorn main:app --reload
```