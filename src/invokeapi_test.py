import requests

payload = {
    "name":'Raj'
}

url = "http://127.0.0.1:5000/greet"

# response = requests.post(url, json=payload)

# if response.status_code == 200:
#     text = (response.json())
#     print(text['message'])

# response = requests.get(url, params=payload)

# if response.status_code == 200:
#     text = (response.json())
#     print(text)

try:
    response = requests.get(url, params=payload)

    if response.status_code == 200:
        name = response.json()
        print (f"Response is {name['Time']}")
    else:
        print("There is an error with url get request")

except requests.exceptions.ConnectionError as errc:
    print(f"HTTP Connection error {errc}")