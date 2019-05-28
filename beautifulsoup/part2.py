import requests
from bs4 import BeautifulSoup as BS

signup_url = "http://kbd.herokuapp.com/signup"
login_url = "http://kbd.herokuapp.com/login"
news_url = "https://kbd.herokuapp.com/dashboard/news/eng/international"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with requests.session() as client:
    login_form = client.get(login_url, headers=headers)
    soup = BS(login_form.content, 'html.parser')
    csrf_token = soup.find('input', id='csrf_token')['value']

    form_data = {
        "email": "f@f.com",
        'password': "rrrr",
        'csrf_token': csrf_token
    }

    login_post = client.post(login_url, data=form_data, headers=headers)
    print(login_post.text.encode('utf-8'))
