import requests


def check_connectivity():
    request = requests.get("http://www.google.com")
    return request.status_code == 200


print(check_connectivity())
