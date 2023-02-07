import requests
import datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.departure_airport_code = "LON"
        self.departure_city = "London"
        self.tequila_flight_price_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.api_key = ""

        self.headers = {
            "apikey": self.api_key
        }

    # Generate date from for the flight search
    def get_date_from(self):
        today = datetime.datetime.now()
        from_date = (today + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        # print(from_date)
        return from_date

    # Generate Date To for the flight search
    def get_date_to(self):
        today = datetime.datetime.now()
        to_date = (today + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
        # print(to_date)
        return to_date


    # Get the lowest price for the flight for a destination
    def get_flight_price(self, fly_to_dest, stops=1):
        date_from_value = self.get_date_from()
        date_to_value = self.get_date_to()
        self.parameters = {
            "fly_from": self.departure_airport_code,
            "fly_to": fly_to_dest,
            "date_from": date_from_value,
            "date_to": date_to_value,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "adults": "4",
            "partner_market": "us",
            "curr": "GBP",
            "max_stopovers": stops,
            "vehicle_type": "aircraft",
            "sort": "price",
            "asc": "1",
            "limit": "10"
        }
        flist_price_response = requests.get(url=self.tequila_flight_price_search_endpoint, params=self.parameters, headers=self.headers)
        results = flist_price_response.json()
        print(results)
        try:
            city_from = results["data"][0]["cityFrom"] # From City Name
            fly_from = results["data"][0]["flyFrom"] # From Airport code
            city_to = results["data"][0]["cityTo"] # To City Name
            fly_to = results["data"][0]["flyTo"] # To Airport Code
            city_code_to = results["data"][0]["cityCodeTo"]
            nights_in_dest = results["data"][0]["nightsInDest"]
            price = results["data"][0]["price"]
            print(results["data"][0]["price"])
        except IndexError:
            print(f"No flights found for {fly_to_dest}")
            return None
        else:
            results = {
                "price": price,
                "city_from": city_from,
                "fly_from": fly_from,
                "city_to": city_to,
                "fly_to": fly_to
            }
        return results
