# TOTP Authentication System (Terminal Based)

## Overview

This project demonstrates a **Two-Factor Authentication (2FA)** system using **Time-based One-Time Password (TOTP)**.

The system allows users to:

* Register with **email and password**
* Generate a **TOTP secret**
* Scan a **QR code using an authenticator app**
* Login using **email + password + OTP**

The project runs entirely in the **terminal** and stores data in a **SQLite database**.

Common authenticator apps supported:

* Google Authenticator
* Microsoft Authenticator
* Authy

---

# Project Structure

```
totp-terminal-auth/
│
├── main.py
├── register_user.py
├── login_user.py
├── totp_utils.py
├── database.py
│
├── qr_codes/
│
├── users.db
```

File description:

| File             | Description                          |
| ---------------- | ------------------------------------ |
| main.py          | Entry point of the application       |
| register_user.py | Handles user registration            |
| login_user.py    | Handles login and OTP verification   |
| totp_utils.py    | Generates and verifies TOTP          |
| database.py      | Manages SQLite database              |
| qr_codes/        | Stores QR codes for user setup       |
| users.db         | SQLite user database                 |

---

# Authentication Flow

## User Registration

```
User enters email and password
        ↓
TOTP secret is generated
        ↓
QR code is created
        ↓
User scans QR code with authenticator app
        ↓
Secret stored in database
```

## User Login

```
User enters email and password
        ↓
User enters OTP from authenticator app
        ↓
OTP verified using TOTP secret
        ↓
Login successful
```

---

# Installation

## 1. Clone Repository

```
git clone https://github.com/yourusername/totp-terminal-auth.git
cd totp-terminal-auth
```

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install pyotp qrcode[pil] cryptography
```

Libraries used:

* **pyotp** – TOTP generation and verification
* **qrcode** – QR code generation
* **sqlite3** – Database storage (built-in)

---

# Running the Application

Start the system:

```
python main.py
```

Menu:

```
1 Register
2 Login
3 Exit
```

---

# Registration Example

```
Enter Email: user@example.com
Enter Password: mypassword

Scan QR using authenticator app
QR saved at: qr_codes/user@example.com.png

User registered successfully
```

Scan the QR using:

* Google Authenticator
* Microsoft Authenticator

---

# Login Example

```
Email: user@example.com
Password: mypassword

Enter OTP from authenticator app
OTP: 483921

Login Successful
```

---

# Security Features

* Password authentication
* TOTP based second factor
* QR code provisioning
* Limited OTP attempts

---

# Future Improvements

Possible improvements:

* Password hashing using **bcrypt**
* OTP expiration checks
* Email or SMS fallback OTP
* Account lock after multiple failures
* Web-based interface
* Audit logging

---

# Technologies Used

* Python
* SQLite
* TOTP Authentication
* QR Code Generation
* Encryption

---

# License

This project is for **educational and demonstration purposes**.
