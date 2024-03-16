import json

class Account:
    def __init__(self):
        self.display_choices()

    def display_choices(self):
        while (True):
            print("""
                Choices:
        
                1. Registration
                2. Login
        
            """)

            choice = input('Choose an option: ')
            if choice == '1':
                self.registrationMethod()
                break
            elif choice == '2':
                self.user = self.loginMethod()
                break
            print("Invalid choice. Please choose either '1' or '2'.")


    def loginMethod(self):
        all_accounts = self.read_from_json("accounts.json")
        no_account = True

        while(no_account):
            enteredInfo = self.input_data()
            print(enteredInfo)
            for account in all_accounts:
                print(account)
                if account["email"] == enteredInfo["email"]:
                    print("Email is Good")
                    if account["password"] == enteredInfo["password"]:
                        print("Password is GOod")
                        no_account = False
                        break

        return enteredInfo



    def read_from_json(self, path):
        file = open(path)
        data = json.loads(file.read())
        return data

    def write_to_json(self, path, account_data):
        try:
            with open(path, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(account_data)
        with open(path, 'w') as file:
            json.dump(existing_data, file)

    def input_data(self):
        email = str(input("Enter Email: "))
        password = str(input("Enter Password: "))

        return {'email': email, 'password': password}

    def registrationMethod(self):
        all_accounts = self.read_from_json("accounts.json")
        duplicate_account = True

        while(duplicate_account):
            entered_data = self.input_data()
            duplicate_account = False
            for account in all_accounts:
                if entered_data["email"] == account["email"]:
                    print("Dupe FOund")
                    duplicate_account = True
                    break

        self.write_to_json("accounts.json", entered_data)
        self.display_choices()

    def give_user(self):
        return self.user


#
