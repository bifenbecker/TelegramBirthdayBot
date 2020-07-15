import requests
from bs4 import BeautifulSoup

url = 'http://ru.astrologyk.com/horoscope/birthday'


def get_html(url):
    r = requests.get(url)
    return r.text

def get_links_month(html):
    soap = BeautifulSoup(html, 'html.parser')

    divs = soap.find_all('div',class_='col-3 col-lg-2 d-flex mb-3 px-1 px-md-2')

    links = []
    lim = 1
    for div in divs:
        a = div.find('a').get('href')
        link = 'http://ru.astrologyk.com'+a
        links.append(link)
        lim+=1
        if lim == 13:
            break
    return links

def get_links_day(html):
    nums = [0,1,2,3,4,5,6,7,8,9]
    soap = BeautifulSoup(html, 'html.parser')

    a = soap.find_all('a',class_='card w-100')
    links = []

    for link in a:
        try:
            num = int(link.get('href')[-1])
        except:
            num = -1

        if  num in nums:
            stage_link = 'http://ru.astrologyk.com'+link.get('href')
            links.append(stage_link)


    return links

def get_info(html):
    soap = BeautifulSoup(html,'html.parser')

    title = soap.find('h2').text
    text = soap.find('p').text
    data = {'title':title, 'text':text}
    return data

def main(dd,mm):
    html = get_html(url)
    links = get_links_month(html)
    links_day = get_links_day(get_html(links[int(mm)-1]))
    return get_info(get_html(links_day[int(dd)-1]))



# if __name__ == '__main__':
#     main()
