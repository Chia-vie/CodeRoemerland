import requests
print("Hallo!")
Name = input("Whats your Name?")
Username = input("Whats your Minecraft username?")
print("Hello " + Name + " aka " + Username)
response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + Username)
Minecraft = input("Do you want to see your Minecraft UUID?")
print(response.json())
