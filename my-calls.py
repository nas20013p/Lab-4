import httpx

url = "https://obscure-winner-x5w6v47wrwwxhvgv4-5000.app.github.dev/"


def make_post_request(endpoint, data):
    response = httpx.post(url + endpoint, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


login_data = {
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

# successful authorization 
auth_data_success_1 = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb",
}

auth_data_success_2 = {
    "text": "How are you?",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

auth_data_success_3 = {
    "text": "How is your day going!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

# failed authorization 
auth_data_fail_1 = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "incorrect_token"
}

auth_data_fail_2 = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "unknown@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

response = httpx.get(url)
print(response.status_code)
print(response)

response = httpx.get(url)
print(response.status_code)
print(response.text)

# Login request
print("\nLogin Request:")
make_post_request("login", login_data)

# Successful POST requests 
print("\nSuccessful POST Requests:")
make_post_request("echo", auth_data_success_1)
make_post_request("echo", auth_data_success_2)
make_post_request("echo", auth_data_success_3)

# Failed POST requests
print("\nFailed POST Requests:")
make_post_request("echo", auth_data_fail_1)
make_post_request("echo", auth_data_fail_2)
