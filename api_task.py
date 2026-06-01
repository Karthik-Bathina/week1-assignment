import requests

print("===== CAT FACT API =====")

url = "https://catfact.ninja/fact"

response = requests.get(url)
data = response.json()

print("\nRandom Cat Fact:")
print(data["fact"])

print("\nLength:", data["length"])