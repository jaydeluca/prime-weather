# Kyruus Interview Exercise
* Python 3 Flask API

## Setup
Manually Running the App
```
python3 -m venv env
source env/bin/activate
pip install -e .
python wsgi.py
```
Access the App via: http://127.0.0.1:5000/ 


## API
Endpoints:

* [GET] /version
    * Return a JSON dictionary with the version of the application.
* [POST] /is_prime 
    * Takes a number and returns true if the provided number is prime or false if not prime.
* [POST] /weather 
    * Takes a US zipcode and returns the current weather. 
    