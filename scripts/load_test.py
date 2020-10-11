import requests


def health_request():
    req = requests.get("http://localhost:5000/health")
    print("Health endpoint: " + str(req.status_code))


def version_request():
    req = requests.get("http://localhost:5000/version")
    print("Version endpoint: " + str(req.status_code))


def is_prime():
    req = requests.post("http://localhost:5000/api/is_prime", json={"number": 88})
    print("Is Prime endpoint: " + str(req.text))


while True:
    health_request()
    version_request()
    is_prime()
