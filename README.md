# 🌦️ FastAPI Weather Service

This is a simple **Weather Service API** built with **FastAPI**. The service fetches current weather data for a given city using an external weather API (like OpenWeatherMap). It is wrapped in **Docker** for easy deployment and managed using **Docker Compose**.


## **Features**
- 🧩 FastAPI framework for API development.
- 🌍 Retrieve current weather data for a given city.
- 🐳 Dockerized application for easy deployment.
- ⚙️ Environment-based configuration using `.env` files.
- 🚀 Manage services using Docker Compose.


## **Setup Instructions**
### 1. Register at [OpenWeatherMap](https://openweathermap.org/guide)
Complete the registration to obtain API key. 

Note: it might take some time for them to validate your registration, so at first several minutes API key might not work.

### 2. Clone the Repository
<pre>git clone https://github.com/KirillDaubur/weather-app.git
cd weather-app</pre>

### 3. Create the .env File
Create a .env file in the root directory of the project:

<pre>
mkfile .env</pre>

and fill it appropriately:

<pre>
OPENWEATHERMAP_APP_ID=     # your OpenWeatherMap API key;

MEMCACHED_HOST=            # Memcached host (use value memcached to run locally)
MEMCACHED_PORT=            # Memcached port (use value 11211 to run locally)

POSTGRES_HOST=             # Database host (use value db for local setup)
POSTGRES_PORT=             # Database port (use value db for local setup)
POSTGRES_USER=             # Postgres user (use any value for local setup)
POSTGRES_PASSWORD=         # Postgres password (use any value for local setup)
POSTGRES_DB=               # Postgres DB name (use any value for local setup)

S3_BUCKET_NAME=            # S3 bucket name (use any value containing words separated by dashes for local setup)
AWS_ACCESS_KEY_ID=         # AWS access key ID (use value test for local setup)
AWS_SECRET_ACCESS_KEY=     # AWS access key (use value test for local setup)
S3_ENDPOINT_URL=           # S3 base URL (use value http://localstack:4566 for local set up, otherwise leave empty) </pre>


### 4. Build and Run the Services
For local set up appropriate docker containerized services were used, so they should be run before the api.
The services used are:
* *postgres* for database (container is called db)
* *memcached* for cache (container is called memcached)
* *localstack* for S3 storage emulation (container is called localstack)

You can replace any of them. 

#### 4.1 Local setup

Use Docker Compose to build and start the FastAPI application:

<pre>
docker compose up -d db localstack memcached --build
docker compose up -d api --build</pre>

Also if you want to use any 

#### 4.2 Prod setup

In case of production set up you don't need to run support services, so just run api service.

<pre>
docker compose up -d api --build</pre>