#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Get data from Google sheets
sheet_data = DataManager()
sheet_results = sheet_data.get_data()
print(sheet_results)

# Search for IATA Codes
search_flights = FlightSearch()
# search_flight_code = search_flights.search_flight()

# Search for lowest price
flight_price_search = FlightData()

# Notification class instance
notify = NotificationManager()


# Get users from sheet
user_data = sheet_data.get_user_data()
user_list = []


def get_emails():
    user_list.clear() # Adding this other the list will grow with each call in a loop
    for row in range(len(user_data["users"])):
        for key, value in user_data.items():
            # print(value[row])
            name = f"{value[row]['firstName']} {value[row]['lastName']}"
            email = value[row]['email']
            # print(name)
            # print(email)
            user_list.append(email)
    print(user_list)
    return user_list

row = 1
for results in sheet_results:
    # print(f"row is now {row}")
    # print(sheet_results[0])
    # print(len(sheet_results))
    # print(f"results value is {results}")
    # print(len(results["iataCode"]))
    row += 1
    # print(f"row is now {row}")
    city = results["city"]
    if len(results["iataCode"]) == 0:
        # print("no data")
        # Populate IATA Codes for each city
        search_flight_code = search_flights.search_flight(city)
        results["iataCode"] = search_flight_code
        sheet_data.write_data(row, search_flight_code)
    else:
        print(results["iataCode"])
        to_city = results["iataCode"]
        price_result = flight_price_search.get_flight_price(to_city)
        print(f"price_result when no direct flights- {price_result}")
        # print(price_result["price"])
        if price_result != None:
            price = price_result["price"]
            print(f"{to_city}: {price}")
            print(results["lowestPrice"])
            low_price_set = results["lowestPrice"]
            if price < low_price_set:
                msg = f"Low price alert! Only {price} to fly from {price_result['city_from']}-{price_result['fly_from']} to {price_result['city_to']}-{price_result['fly_to']}"
                print (f"Low price - {msg}")
                notify.send_notification(msg_body=msg)
                emails = get_emails()
                for email in emails:
                    notify.send_emails(email, msg)
            else:
                msg = f"Price alert! Only {price} to fly from {price_result['city_from']}-{price_result['fly_from']} to {price_result['city_to']}-{price_result['fly_to']}"
                print(f"Current price - {msg}")
                # notify.send_notification(msg_body=msg)
                emails = get_emails()
                for email in emails:
                    notify.send_emails(email, msg)
        else:
            continue


print(sheet_results)
# print(city)
# flight_price_search.get_date_from()

