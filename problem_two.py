import requests

def number_of_subscribers(subreddit):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    URL = f"https://api.reddit.com/r/{subreddit}/about"
    response = requests.get(URL, headers=header).json()

    print(response["data"]["subscribers"])


number_of_subscribers("minecraft")