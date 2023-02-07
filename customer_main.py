from customer_acquisitions import CustomerAcquisitions
from data_manager import DataManager
from notification_manager import NotificationManager

acquisitions = CustomerAcquisitions()
email_validation_result = acquisitions.validate_email()

user_data = DataManager()

fname = acquisitions.fname
lname = acquisitions.lname
email = acquisitions.email
if email_validation_result:
    print("Start to add user record")
    print (f"{fname}-{lname}-{email}")
    # user_data.add_user(f_name=fname, l_name=lname, email=email)
    # user_data.get_user_data()
else:
    print("Emails did not match, user need to re-register.")


user_data = user_data.get_user_data()
# print(user_data["users"][0])

# print(len(user_data["users"]))


