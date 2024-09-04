import requests

response = requests.get("https://api.github.com/repos/manmeet1515/ResumeWebsite/commits")

#print(response)
#print(response.json())
detail = response.json()

#print(detail[0]["author"]["login"])

for i in range(len(detail)):
    print(detail[i]["commit"]["author"]["name"])