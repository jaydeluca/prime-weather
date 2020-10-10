# Kyruus Interview Exercise
* Python 3 Flask API


## Setup
#### Environment Variables
You will need an api key for [OpenWeather](https://home.openweathermap.org/api_keys)
```bash
# Copy and then Populate the .env file
cp example.env .env
```

#### Manually Running the App
```bash
python3 -m venv env
source env/bin/activate
pip install -e .
export FLASK_ENV=dev
python wsgi.py
```
Access the App via: http://127.0.0.1:5000/ 

#### Docker
Build and Run the app via a docker container:
```bash
docker-compose up -d
```
Access the App via: http://127.0.0.1:5000/ 

#### Kubernetes
```bash
kubectl apply -f kubernetes/deployment.yml
```

#### Minikube
There is an included script to build image, setup elasticsearch, and deploy the app
```bash
eval $(minikube docker-env)
./minikube-startup.sh
```
Port forward the api to allow access on http://localhost:5000
```
./scripts/minikube-open-api.sh
```

Port forward Kibana to allow access on http://localhost:5601
```
./scripts/minikube-open-kibana.sh
```


## API
Endpoints:

#### [GET] /health
Return a JSON dictionary with the name and version of the application.

#### [GET] /version
Return a JSON dictionary with the version of the application.

#### [POST] /api/is_prime 
Takes a number and returns true if the provided number is prime or false if not prime.

#### [POST] /api/weather 
Takes a US zipcode and returns the current weather.

Example Response:
```
{
  "coord": {
    "lon": -71.32,
    "lat": 41.84
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 294.48,
    "feels_like": 288.97,
    "temp_min": 293.15,
    "temp_max": 296.15,
    "pressure": 1012,
    "humidity": 64
  },
  "visibility": 10000,
  "wind": {
    "speed": 9.8,
    "deg": 210,
    "gust": 13.4
  },
  "clouds": {
    "all": 20
  },
  "dt": 1602363393,
  "sys": {
    "type": 1,
    "id": 5441,
    "country": "US",
    "sunrise": 1602327138,
    "sunset": 1602367899
  },
  "timezone": -14400,
  "id": 0,
  "name": "Seekonk",
  "cod": 200
}
``` 
    