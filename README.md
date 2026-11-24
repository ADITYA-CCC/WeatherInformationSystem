# Weather Information System 🌦️

## 1. Project Overview

The Weather Information System is a web-based application developed using Python and Flask. It allows users to search for a city and view its current weather information and forecast details.

The application retrieves weather information using the Open-Meteo API and displays the results through a simple web interface.

The application is containerized using Docker, making it easier to build, run and deploy across different environments.

## 2. Technologies Used

- Python 3.11
- Flask
- HTML and CSS
- Open-Meteo API
- Docker
- Git and GitHub
- Docker Hub

## 3. Features

- Search weather information by city.
- Retrieve geographical coordinates using Open-Meteo Geocoding API.
- Fetch weather forecast information.
- Display weather details through a web interface.
- Docker containerization for portability.
- Easy application deployment using a Docker image.

## 4. Project Structure

```text
WeatherInformationSystem/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

## 5. Running the Application Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/ADITYA-CCC/WeatherInformationSystem.git
```

### Step 2: Navigate to the project directory

```bash
cd WeatherInformationSystem
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open the application

Open your browser and visit:

```text
http://localhost:5000
```

## 6. Docker Implementation

The application is containerized using Docker.

### Build the Docker image

```bash
docker build -t weather-app .
```

### Run the Docker container

```bash
docker run -d -p 5000:5000 --name weather-container weather-app
```

### Verify the running container

```bash
docker ps
```

### Stop the container

```bash
docker stop weather-container
```

## 7. Docker Hub

The Docker image is available on Docker Hub.

**Docker Hub Repository:**

https://hub.docker.com/r/adityaq3q3q3/weather-app

### Pull the Docker image

```bash
docker pull adityaq3q3q3/weather-app:latest
```

### Run the downloaded image

```bash
docker run -d -p 5000:5000 --name weather-container adityaq3q3q3/weather-app:latest
```

Access the application at:

```text
http://localhost:5000
```

## 8. GitHub Repository

Source code and Docker configuration:

https://github.com/ADITYA-CCC/WeatherInformationSystem

## 9. Conclusion

The Weather Information System demonstrates the development of a Python Flask web application and its containerization using Docker.

The project covers application development, dependency management, Docker image creation, container execution, and publishing the Docker image to Docker Hub.

It also uses GitHub for source code management and version control.
