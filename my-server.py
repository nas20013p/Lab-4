from flask import Flask, request, jsonify

app = Flask(__name__)

valid_tokens = {"nazmus.sakib@uconn.edu": "f99aa8b8573062e9802f4fc0807ae1cb"}

@app.route("/")
def hello():
   return " you called \n"


@app.route("/login", methods=['POST'])
def login():
    token_id = request.form.get('token_id')
    token = request.form.get('token')
    if token_id and token and valid_tokens.get(token_id, None) == token:
        return jsonify({"message": "Login successful", "user": token_id}), 200
    else:
        return jsonify({"error": "Invalid token_id or token"}), 401


# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
    token = request.form.get('token')
    token_id = request.form.get('token_id')
    if token_id in valid_tokens and valid_tokens[token_id] == token:
        return "You said: " + request.form['text']
    else:
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
   app.run(host='0.0.0.0')