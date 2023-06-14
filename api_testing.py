import requests


def call_api(url):


    response = requests.get(url)

    if response.status_code == 200:
        data = response.history
        # Process the data or perform other actions
        print(data)
    else:
        print(f"Failed to call API. Error: {response.status_code}")


def main():
    api_url = "https://fakestoreapi.com/products"
    call_api(api_url)


if __name__ == "__main__":
    main()
