import requests
import time
import json

def send_request():
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Opera GX\";v=\"105\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }

    data = {
        "partnerUserId": "8a02e53a42eabe788ecbe190"
    }

    # Make a POST request using the requests library
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Assuming the response contains a JSON with a "token" field
        token = response.json().get("token")

        # Append the token to a link (adjust the link format as needed)
        link_with_token = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
        print(f"Link with Nitro: {link_with_token}")

        # Write the token and link to a text file
        with open("nitrolinks.txt", "a") as file:
            file.write(link_with_token + "\n")
    else:
        print(f"Request failed with status code {response.status_code}")

# Run the script to send a request every second
while True:
    send_request()
