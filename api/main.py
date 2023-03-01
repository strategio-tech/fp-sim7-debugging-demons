from flask import Flask, request, jsonify
from decouple import config
from flask_cors import CORS
import requests
from utils.util import generate_token, decode_token
from utils.dbConnect import dbConnect
from utils.util import authenticate_password, hash_password

TOKEN = config('API_TOKEN')
ADMIN_PASS = config('ADMIN_PASS')

app = Flask(__name__)
CORS(app)   

@app.route('/')
def welcome_screen():
   return 'Hello, Penny!'

@app.route('/signup', methods=['POST'])
def signup():
    
    # Get the data from the POST request
    data = request.get_json()
    user = data['user'].lower()

    if not authenticate_password(data['admin_password'], ADMIN_PASS):
      response = {"message": "Invalid admin password"}
      return jsonify(response), 401

    hash = hash_password(data['password'])

    # check name doesn't exist in db
    mydb = dbConnect()
    mycursor = mydb.cursor()

    sql = "SELECT user FROM users WHERE user = %s"
    val = (user,)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchone()

    if myresult != None:
      response = {"message": "This user already exists."}
      return jsonify(response), 400

    # store in db
    sql = "INSERT INTO users (name, user, password) VALUES (%s, %s, %s)"
    val = (data['name'], user, hash)
    mycursor.execute(sql, val)

    mydb.commit()

    # retrieve search history
    mycursor.execute("SELECT prompt FROM history")

    result = mycursor.fetchall()

    # create token
    token = generate_token(user)

    # Return a response
    response = {"name": data['name'], "promptHistory": result, "token": token}
    return jsonify(response)

@app.route('/login', methods=['POST'])
def login():
    # Get the data from the POST request
    data = request.get_json()
    user = data['user'].lower()

    # request password from db
    mydb = dbConnect()
    mycursor = mydb.cursor()

    sql = "SELECT * FROM users WHERE user = %s"
    val = (user,)

    mycursor.execute(sql, val)

    # tuple(id, name, user, password)
    result = mycursor.fetchone()

    if result == None:
      response = {"message": "Invalid credentials"}
      return jsonify(response), 401
    
    id, name, user, hash = result

    # Process the data
    isValid = authenticate_password(data['password'], hash)

    if not isValid:
      response = {"message": "Invalid credentials"}
      return jsonify(response), 401

    # If valid retrieve search history
    mycursor.execute("SELECT prompt FROM history")

    history = mycursor.fetchall()

    # Generate token
    token = generate_token(user)

    # Return a response
    response = {"name":name, "promptHistory": history, "token": token}
    return jsonify(response)

# Route to handle POST requests to /api/second_route
@app.route('/prompt', methods=['POST'])
def handlePrompt():
    # Get the data from the POST request
    data = request.get_json()
    user = data['user'].lower()
    topic = data['topic'].lower()

    #connect to db
    mydb = dbConnect()
    mycursor = mydb.cursor()

    # Decode token
    try:
        _user = decode_token(data['token'])

        if _user != user:
           return jsonify({"message": "Invalid token."}), 401
    except:
       return jsonify({"message": "Invalid token."}), 401
    
    # store in db
    sql = "SELECT prompt FROM history WHERE prompt = %s"
    val = (topic,)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchone()

    if myresult == None:
      sql = "INSERT INTO history (prompt) VALUES (%s)"
      val = (topic,)
      mycursor.execute(sql, val)

      mydb.commit()

    # Generate prompt
    talking_points = []

    if len(data['key_points']) > 0:
      for point in data['key_points']:
        talking_points.append(point)
    
    ", ".join(talking_points)

    prompt = f"Starting with the title, write a technical blog from the point of view of a technologist in training about {data['topic']}. Include the following talking points: {talking_points}. Make sure the end has a call to action to subscribe to your blog."
    
    # Make request to GPT
    url = 'https://api.openai.com/v1/completions'
    body = {
    "model": "text-ada-001",
    "prompt": prompt,
    "max_tokens": 12,
    "temperature": 1
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=body, headers=headers)
    response = response.json()

    # Return a response
    response = {"completion": response['choices'][0]['text']}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3030,debug=True)
