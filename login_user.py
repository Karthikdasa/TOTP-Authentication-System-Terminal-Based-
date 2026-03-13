from database import get_user
from totp_utils import verify_otp

MAX_ATTEMPTS = 5


def login():

    email = input("Email: ")
    password = input("Password: ")

    user = get_user(email)

    if user is None:
        print("User not found")
        return

    db_password = user[2]
    secret = user[3]

    if password != db_password:
        print("Invalid password")
        return

    print("\nEnter OTP from authenticator app")

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        otp = input("OTP: ")

        if verify_otp(secret, otp):

            print("\nLogin Successful")
            return

        else:
            attempts += 1
            print("Invalid OTP")

    print("\nToo many failed attempts")