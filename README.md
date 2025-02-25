# Azure Pricing Dashboard Using API

## Overview
The **Azure Pricing Dashboard** is a web application that fetches real-time pricing data from the Azure API and displays it in a visually appealing dashboard. The project is built using **Flask, MongoDB, and Docker**.

## Features
- Fetches Azure retail pricing data via API
- Stores and updates data in MongoDB
- Displays data in a structured and colorful UI
- Runs inside a Docker container
- Scheduled data refresh every 30 minutes

## Tech Stack
- **Backend**: Flask, MongoDB
- **Database**: MongoDB
- **Containerization**: Docker, Docker Compose

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Python 3.11](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/)

### Clone the Repository
```bash
git clone https://github.com/dharunbalajipalanivel/Azure_Pricing_Dashboard_Using_API.git
cd Azure_Pricing_Dashboard_Using_API
```

### Running with Docker
#### 1. Build and Start the Containers
```bash
docker-compose up --build
```
#### 2. Populate Database with Initial Data
```bash
docker-compose run web python populate_data.py
```
#### 3. Access the Application
- Web Application: [http://localhost:5000](http://localhost:5000)
- MongoDB: [mongodb://localhost:27017](mongodb://localhost:27017)

## License
This project is licensed under the **BSD-3-Clause License**.
