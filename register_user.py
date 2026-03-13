import qrcode

from totp_utils import generate_secret, get_uri
from database import add_user


def register():

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    secret = generate_secret()

    uri = get_uri(secret, email)

    img = qrcode.make(uri)

    file_path = f"qr_codes/{email}.png"
    img.save(file_path)

    print("\nScan QR using authenticator app")
    print("QR saved at:", file_path)

    add_user(email, password, secret)

    print("\nUser registered successfully")