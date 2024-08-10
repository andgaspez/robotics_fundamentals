import requests

# Replace with your actual values
client_id = '' # The one obtained from https://dev.mendeley.com/myapps.html
client_secret = '' # The one generated in https://dev.mendeley.com/myapps.html
redirect_uri = 'http://localhost:8080/callback'
authorization_code = '' #The one obtained from executing oauth_server succesfully

# Exchange the authorization code for an access token
response = requests.post('https://api.mendeley.com/oauth/token', data={
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
})

# Check if the request was successful
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print(f"Access token: {access_token}")
else:
    print(f"Failed to get access token: {response.status_code} - {response.text}")