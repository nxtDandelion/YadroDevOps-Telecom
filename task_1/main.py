import requests
from requests.exceptions import HTTPError


def get_request(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        response_body = response.text
        if 400 > status_code >= 100:
            logs(url, status_code, response_body)
        response.raise_for_status()
    except HTTPError as err:
        print("ERROR:")
        logs(url, status_code, err)


def logs(url, status_code, response_body):
    print(f"Url: {url}")
    print(f"Status Code: {status_code}")
    print(f"Response Body: {response_body}")
    print("\n")


def main():
    urls = [
        "https://httpstat.us/101",
        "https://httpstat.us/200",
        "https://httpstat.us/300",
        "https://httpstat.us/400",
        "https://httpstat.us/500",
    ]
    for url in urls:
        get_request(url)


if __name__ == "__main__":
    main()
