import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_api_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.tequila_api_key = "0D1Lf-IqQODTum1UkVju44YRtnUbpXr_"

    # Search for the IATA Code for a city's airport
    def search_flight(self, city_name):
        self.parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 10,
            "active_only": "true"
        }

        self.headers = {
            "apikey": self.tequila_api_key
        }
        iata_code_search_response = requests.get(url=self.tequila_api_endpoint, params=self.parameters, headers=self.headers)
        results = iata_code_search_response.json()
        print(f"IATA Code Results {results}")
        print(results["locations"][0]["city"]["code"])
        iata_code = results["locations"][0]["city"]["code"]
        return iata_code
