import http.client
import ssl
import json
import os
    

def get_lockfile_port():
    # Path to the lockfile
    lockfile_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Riot Games', 'Riot Client', 'Config', 'lockfile')

    # Check if the lockfile exists
    if os.path.exists(lockfile_path):
        # Using 'with' statement to read the lockfile
        with open(lockfile_path, 'r') as file:
            lockfile_content = file.read().strip()

        # Split the content by colon to extract the values
        parts = lockfile_content.split(':')
        
        if len(parts) == 5:
            name, pid, port, password, protocol = parts
            print("port number:", port)
            return port
        else:
            return "Unexpected lockfile format"
    else:
        return"Lockfile not found"


def get_entitlement_token(port_number):
    # Path to .pem file

    pem_file_path = r"C:\Users\phamh\Desktop\coding\testapi\riotgames.pem"

    # Create an SSL context and load the .pem file
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(pem_file_path)

    # Establish HTTPS connection with the SSL context
    conn = http.client.HTTPSConnection("127.0.0.1", port_number, context=ssl_context)

    payload = ""

    headers = {'Authorization': "Basic cmlvdDo4SXNQVEJxNGdPWUt1cDVWN0h1eWpR"}

    # Send the request
    conn.request("GET", "/entitlements/v1/token", payload, headers)

    # Get the response
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data_info = json.loads(data)
    token = data_info.get("accessToken", "")
    # Print the response data
    access_token = "Bearer " + token
    print("access_token: ", access_token)
    return access_token

#example of functions 
# port =  get_lockfile_port()
# get_entitlement_token(port)