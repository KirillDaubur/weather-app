# 🌦️ FastAPI Weather Service

This is a simple **Weather Service API** built with **FastAPI**. The service fetches current weather data for a given city using an external weather API (like OpenWeatherMap). It is wrapped in **Docker** for easy deployment and managed using **Docker Compose**.

---

## **Features**
- 🧩 FastAPI framework for API development.
- 🌍 Retrieve current weather data for a given city.
- 🐳 Dockerized application for easy deployment.
- ⚙️ Environment-based configuration using `.env` files.
- 🚀 Manage services using Docker Compose.

---

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
# Replace placeholders with actual values
OPENWEATHERMAP_APP_ID=     # your OpenWeatherMap API key;
MEMCACHED_HOST=            # Memcached host (use value memcached to run locally)
MEMCACHED_PORT=            # Memcached port (use value 11211 to run locally)</pre>
Note: Replace the placeholders with your own values.

### 4. Build and Run the Services
Use Docker Compose to build and start the FastAPI application:

<pre>
docker-compose up --build</pre>