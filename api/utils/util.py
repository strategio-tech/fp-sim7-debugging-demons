from decouple import config
import crypt
import jwt

SALT=config('SALT')

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

# Generate a token from a user ID
def generate_token(user):
    # Define the token payload containing the user ID and custom salt
    payload = {
        'user': user,
        'salt': SALT
    }

    # Generate the token using the JWT library
    token = jwt.encode(payload, SALT, algorithm='HS256')

    return token

# Decode a token to retrieve the user ID
def decode_token(token):
    # Try to decode the token using the JWT library
    try:
        decoded = jwt.decode(token, SALT, algorithms=['HS256'])

        # Check that the decoded token contains the correct salt
        if decoded['salt'] != SALT:
            raise ValueError('Invalid token salt')
    except (jwt.InvalidTokenError, KeyError, ValueError):
        # If decoding fails or the salt is invalid, return None
        return None

    # Return the user ID from the decoded token
    return decoded['user']

