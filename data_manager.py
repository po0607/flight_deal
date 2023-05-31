import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/4f63b362af289b335ca7ab922fdb46c3/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/4f63b362af289b335ca7ab922fdb46c3/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_email(self):
        customer_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customer_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
