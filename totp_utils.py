import pyotp


def generate_secret():
    return pyotp.random_base32()


def get_uri(secret, email):

    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(
        name=email,
        issuer_name="TerminalAuthApp"
    )

    return uri


def verify_otp(secret, otp):

    totp = pyotp.TOTP(secret)

    return totp.verify(otp, valid_window=1)