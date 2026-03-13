import os

from database import init_db
from register_user import register
from login_user import login


os.makedirs("qr_codes", exist_ok=True)

init_db()

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break