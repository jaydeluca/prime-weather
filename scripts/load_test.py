import requests

host = "http://127.0.0.1:57585/"

def health_request():
    req = requests.get(host + "health")
    print("Health endpoint: " + str(req.status_code))


def version_request():
    req = requests.get(host + "/version")
    print("Version endpoint: " + str(req.status_code))


def is_prime():
    req = requests.post(host + "api/is_prime", json={"number": 88})
    print("Is Prime endpoint: " + str(req.text))


while True:
    health_request()
    version_request()
    is_prime()
