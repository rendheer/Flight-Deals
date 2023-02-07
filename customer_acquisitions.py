
class CustomerAcquisitions:

    def __init__(self):
        print("Welcome to IonServ Flight Club")
        print("We find the best flight deals and email you.")
        self.fname = input("What is your first name?: ").lower()
        self.lname = input("What is your last name?: ").lower()
        self.email = input("What is your email?: ").lower()
        self.email_val = input("Type your email again: ").lower()
        # self.validate_email()

    def validate_email(self):
        if self.email == self.email_val:
            print("You're in the club!")
            return True
        else:
            print("emails do not match. Please try again.")
            return False
