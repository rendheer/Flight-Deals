import requests
from pprint import pprint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_get_endpoint = "https://api.sheety.co/66e1a1a2a0da5b97a65bbfa068faea73/flightDeals/prices"
        self.sheety_post_endpoint = "https://api.sheety.co/66e1a1a2a0da5b97a65bbfa068faea73/flightDeals/prices"
        self.sheety_users_get_endpoint = "https://api.sheety.co/66e1a1a2a0da5b97a65bbfa068faea73/flightDeals/users"
        self.sheety_users_post_endpoint = "https://api.sheety.co/66e1a1a2a0da5b97a65bbfa068faea73/flightDeals/users"
        self.user_list = []
    # Get data from Google Sheets using Sheety
    def get_data(self):
        sheety_response = requests.get(url=self.sheety_get_endpoint)
        sheety_result = sheety_response.json()
        # print(sheety_result["prices"])
        # pprint(sheety_result)
        return sheety_result["prices"]


    # Write data to Google sheets using Sheety. Data is written to a specific row
    def write_data(self, rownum, value):
        sheet_inputs = {
        "price": {
            "iataCode": value
            }
        }
        sheety_post = f"{self.sheety_post_endpoint}/{rownum}"
        print(sheety_post)
        print(value)
        sheety_post_response = requests.put(url=sheety_post, json=sheet_inputs)
        print(sheety_post_response.text)

    # get data from sheets users tab using Sheety
    def get_user_data(self):
        user_response = requests.get(url=self.sheety_users_get_endpoint)
        user_result = user_response.json()
        print(user_result)

    # Put user data in sheets using Sheety after user validation
    def add_user(self, f_name, l_name, email):
        sheet_inputs = {
            "user":{
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }
        print(sheet_inputs)
        sheety_user_post_response = requests.post(url=self.sheety_users_post_endpoint, json=sheet_inputs)
        print(sheety_user_post_response.text)

    # Getting user emails from sheety

    def get_user_data(self):
        user_data_response = requests.get(url=self.sheety_users_get_endpoint)
        results = user_data_response.json()
        # print(type(results))
        # print(results)
        # print(len(results["users"]))
        return results
        # for row in range(len(results["users"])):
        #     for key, value in results.items():
        #         print(value[row]["firstName"])
        #         print(value[row]["lastName"])
        #         print(value[row]["email"])
        #         print(key)
        #         user_data = {
        #             "user": {
        #                 "firstname": value[row]["firstName"],
        #                 "lastname": value[row]["lastName"],
        #                 "email": value[row]["email"]
        #             }
        #         }


        # print(results["users"][0]["firstName"])
        # for row, value in results["users"].items():
        #     print(value)
        #     user_data = {
        #         "firstname": row["firstName"],
        #         "lastname": row["lastName"],
        #         "email": row["email"]
        #     }
        #     self.user_user_list = user_data
        # return self.user_user_list

