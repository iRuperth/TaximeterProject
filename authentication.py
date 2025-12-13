def driver_auth():
    print("Welcome to our digital Taxi")
    print("We will now ask you to enter your user ID and Password")

    while True:
        print("Please enter your user ID:")
        user_id = input().strip()
        print("Please enter your password:")
        if user_id == "Maui" or user_id == "Maple":
            password_user = input().strip()
            if password_user == "password":
                print("Correct password.")
                return True
            else:
                print("Incorrect password, try again.")
        else:
            print("Incorrect user ID, try again.")

