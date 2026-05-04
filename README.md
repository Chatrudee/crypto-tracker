# Crypto-Tracker ₿ 📈

A cloud-ready, microservices-based application built to automatically track real-time Bitcoin (BTC) prices and serve the historical data via a REST API. Originally deployed on Google Cloud Platform (GCP).

## 🚀 Features
* **Automated Price Fetching:** A background Python bot continuously fetches live Bitcoin prices.
* **RESTful API:** Provides clean JSON endpoints to access historical cryptocurrency data using Django REST Framework.
* **Robust Database:** Stores price logs securely in a PostgreSQL database.
* **Dockerized Environment:** Fully containerized services (API, Database, and Bot) for seamless deployment.

## 🛠️ Tech Stack
* **Backend:** Python, Django, Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Infrastructure:** Docker, Docker Compose, Google Cloud Platform (GCP)

## ⚙️ Local Setup & Installation

**Prerequisite:** Ensure you have Docker and Docker Compose installed on your system.

**1. Clone the repository**
```bash
git clone [https://github.com/Chatrudee/crypto-tracker.git](https://github.com/Chatrudee/crypto-tracker.git)
cd crypto-tracker
```

**2. Start the Docker containers**
```bash
docker compose up -d
```

**3. Apply database migrations**
```bash
docker compose run --rm web python manage.py makemigrations
docker compose run --rm web python manage.py migrate
```

## 🔍 API Endpoints
Once the containers are successfully running, you can access the JSON data via your browser:

* **Crypto Prices:** `http://localhost:8000/api/prices/`

## 💡 How it Works
The system runs as three independent Docker containers. The `db` container hosts the PostgreSQL database. The `web` container runs the Django API. The `bot` container runs a background Python script that periodically fetches Bitcoin prices from an external API and saves them directly to the database.

## 🚧 Future Improvements
* Add support for tracking multiple cryptocurrencies (Ethereum, Solana, etc.).
* Build a Frontend Dashboard to visualize price trends with candlestick charts.
