from importlib.resources import contents
import requests
import selectorlib 
import smtplib, ssl
import time

URL = "http://programmer100.pythonanywhere.com/tours/" 
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} # It is needed to display the webpage´s info


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source): 
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["tours"] 
    return value


def send_email(message):
    host = "smtp.gmail.com" 
    port = 465

    username = "your gmail account" 
    password = "your password"

    receiver = "your gmail account" 
    context = ssl.create_default_context() 

    with smtplib.SMTP_SSL(host, port, context = context) as server: 
        server.login(username, password) 
        server.sendmail(username, receiver, message) 


message = f"""\
Subject: "New date on the tour, buy the tickets!

Go to the website to reserve them as soon as possible
"""

def store(extracted):
    with open("data.txt", "a") as file: 
        file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted) 
                send_email(message)

    time.sleep(2) 
