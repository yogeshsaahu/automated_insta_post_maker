import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
import wget
import demo


"""scrap news form website"""
def get_news(title,title2,title3):
    newlist = []
    count = 0
    for i,j,k in zip(title,title2,title3):
        t = i.getText()
        s = j.getText()
        g = k.getText()
        img = ""
        count += 1
        newlist.append({"count": count,"heading": t, "tag": s, "details": g, "img": img})
        pprint(newlist)
    return newlist

"""get links of pages so we can get img links"""
def get_links(title4):
    links = []
    for l in title4:
        v = l['href']
        findURL = re.findall('https:.*indiatoday.*interactive', v)
        if findURL != []:
           links.append(None)
        else:
            add = "https://www.indiatoday.in"
            add += v
            links.append(add)
    pprint(links)
    return links



"""get link of img"""
def get_img_links(links):
    data = []
    for l in links:
        if l == None:
            data.append(None)
        else:
            res = requests.get(f'{l}')
            soup = BeautifulSoup(res.text, 'html.parser')
            title = soup.find_all('img', {'width': '690'})

            if title == []:
                    data.append(None)
            else:
                temp = []
                for i in title:
                    fill = i.get('src')
                    temp.append(fill)
                data.append(temp[0])

    pprint(data)
    return data

'''download images'''
def download_img(data):
    img_names = []

    for i in data:

        if i == None:
            img_names.append(None)
        else:
                url = i
                output_directory = "C:\\Users\\abc\\PycharmProjects\\mp_transport\\headline_bot\\images"
                file_name = wget.download(url, out=output_directory)
                print('Image Successfully Downloaded: ', file_name)
                name = file_name
                img_names.append(name)

    print(img_names)
    return img_names


def connect(newlist,img_names):
    for i, m in zip(newlist, img_names):
        i['img'] = m
    return newlist


if __name__ == "__main__":
    res = requests.get('https://www.indiatoday.in/')
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('.B1S3_content__wrap__9mSB6 a')
    title2 = soup.select('.B1S3_cat__title___NXs1')
    title3 = soup.select('.B1S3_story__shortcont__inicf')

    title4 = soup.select('.B1S3_content__wrap__9mSB6 a')

    newlist = get_news(title, title2, title3)
    links = get_links(title4)
    data = get_img_links(links)
    img_names = download_img(data)
    connect = connect(newlist,img_names)
    pprint(connect)

    cls = demo.PostMaker()
    cls.maker(connect)















