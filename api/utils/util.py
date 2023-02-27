from decouple import config
import bcrypt
import jwt

SALT=config('SALT')

def hash_password(password):

    # converting password to array of bytes
    bytes = password.encode('utf-8')
  
    # generating the salt
    salt = bcrypt.gensalt()
    
    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)

    return hash.decode('utf-8')

def authenticate_password(password, hashed_password):
    
    # encoding user password
    userBytes = password.encode('utf-8')
    hash = hashed_password.encode('utf-8')
    
    # checking password
    return bcrypt.checkpw(userBytes, hash)

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

