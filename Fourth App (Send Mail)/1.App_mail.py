import requests
from send_mail import send_email

topic = "tesla" # The f has to be in the line that has {}
api_key = "bc695baf40a94e91b4717ab771202302"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "sortBy=publishedAt&apiKey=" \
      "890603a55bfa47048e4490069ebee18c"\
      "&language=en" 


# Make request

request = requests.get(url)

# Get a dictionary with data

content = request.json()

# Access the article titles and description

body = "" 
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "Subject: Today´s news" + "\n" + body + article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n" 

body = body.encode("utf-8") 

send_email(body)