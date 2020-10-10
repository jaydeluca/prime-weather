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
There is an included script to build image, bootstrap a minikube cluster, deploy the app, and setup port forwarding for port 5000
```bash
./minikube-startup.sh
```

## API
Endpoints:

* [GET] /version
    * Return a JSON dictionary with the version of the application.
* [POST] /api/is_prime 
    * Takes a number and returns true if the provided number is prime or false if not prime.
* [POST] /api/weather 
    * Takes a US zipcode and returns the current weather. 
    