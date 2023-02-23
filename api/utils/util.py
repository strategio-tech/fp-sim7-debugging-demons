import crypt

def hash_password(password):
    # Generate a salt for the password hash
    salt = crypt.mksalt(crypt.METHOD_SHA512)

    # Hash the password using the salt and return the hashed value
    hashed_password = crypt.crypt(password, salt)
    return hashed_password

def authenticate_password(password, hashed_password):
    # Hash the provided password with the same salt as the stored hashed password
    hashed_input_password = crypt.crypt(password, hashed_password)

    # Compare the hashed input password with the stored hashed password
    if hashed_input_password == hashed_password:
        return True
    else:
        return False
