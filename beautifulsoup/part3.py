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
    news_page = client.get(news_url, headers=headers)
    news_soup = BS(news_page.content, 'html.parser')
    news_list = news_soup.find_all('div', class_='panel-default')

    del news_list[0]

    all_news = []
    for news in news_list:
        news_link = news.div.h3.a['href']
        news_head = news.div.h3.text

        try:
            img_link = news.img['src']
        except:
            img_link = None

        news_body = news.find('div', class_='panel-body')
        date = news_body.div.small.text
        source = news_body.div.span.a.text
        source = source[1:].strip()

        summary_div = news_body.find('div', class_='text-justify')
        summary = summary_div.text

        news_dict = {
            'news_link': news_link,
            'news_head': news_head,
            'img_link': img_link,
            'date': date,
            'source': source,
            'summary':summary,
        }
        all_news.append(news_dict)

print(all_news)
