import string

MUST_HAVE = {
            "numbers" : [[str(x) for x in range(10)], 0],
            "lower case character" : [[char for char in string.ascii_lowercase], 0],
            "upper case characters" : [[char for char in string.ascii_uppercase], 0],
            "symbols" : [[], 0],
        }

def get_data():

    registered = {}

    with open("passwords", "r") as file:
        data = file.read()
        data = data.split("\n")
        try:
            for row in data:
                row = row.split(",")
                registered[row[0]] = row[1]

        except:
            pass

    return registered


def validate_password(password):
    valid = False
    if not (8 <= len(password) <= 15):
        print("Password must be between 8 and 15 characters.")

    else:
        for char in password:
            symbol = True
            for char_type in MUST_HAVE:
                if char in MUST_HAVE[char_type][0]:
                    symbol = False
                    MUST_HAVE[char_type][1] += 1

            if symbol:
                MUST_HAVE["symbols"][1] += 1

        valid = True
        for char_type in MUST_HAVE:
            if MUST_HAVE[char_type][1] == 0:
                valid = False
                print(f"You must include {char_type}.")

    return valid


def main():
    print("1. Register")
    print("2. Login")
    validated = False
    while not validated:
        ans = input("Please choose an option(1/2): ")

        if ans not in ["1","2"]:
            print("Invalid input.")

        else:
            validated = True

    if ans == "1":
        registered = get_data()

        validated = False
        while not validated:
            username = input("Please enter your username: ")

            if username in registered:
                print("Username already in use, please try again.")

            else:
                validated = True

        validated = False


        while not validated:
            password = input("Please enter your password: ")

            if "," in password:
                passwords = password.split(",")
                for password in passwords:
                    if not validate_password(password):
                        passwords.remove(password)

                if len(passwords) > 0:
                    validated = True
                    print(f"Valid passwords: {passwords}")


            else:
                validated = validate_password(password)

                with open("passwords", "a") as file:
                    file.write(username + "," + password)
                    file.write("\n")

        print("Registered succesfully")




if __name__ == "__main__":
    main()