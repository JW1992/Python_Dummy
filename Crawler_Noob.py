#Kudos to: https://zhuanlan.zhihu.com/p/29663747
#Baidu forum

# coding:utf-8

import re,requests
from bs4 import BeautifulSoup

headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}  #Request header

s = requests.session() #Save the request session

def re_test(text):

    # https://imgsa.baidu.com/forum/w%3D580/sign=20bec30aa0ec8a13141a57e8c7029157/2508562c11dfa9ecfd81b1f26bd0f703938fc180.jpg
    img_url = re.findall('https://imgsa.baidu.com/forum/.*?jpg',text)
    return  img_url


def bs_test(text):
    # <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=44312fe1a5af2eddd4f149e1bd110102/1c3477094b36acaf1ce5c71b75d98d1000e99c2f.jpg" size="201260" width="479" height="852">
    soup = BeautifulSoup(text, "lxml")
    img_urls = soup.find_all('img',{'class':'BDE_Image'})
    img_url = [i.get('src') for i in img_urls]
    return  img_url

def img_size(content):
    # PIL: python imaging library
    from PIL import Image
    from io import BytesIO
    img = Image.open(BytesIO(content))
    # Get the size of the image
    return img.size

def save_img(url):
    #[-1]: Negative indices in a list access the list backwards from the end. [-1] means the LAST element.
    img_name = url.strip().split('/')[-1]
    print(img_name)
    url_re = s.get(url.strip(),headers=headers)
    if url_re.status_code == 200:  # 200 http response, if the connection is working
        print('Starting to save ...')
        import os
        if not os.path.exists('baidu_img'):
            os.mkdir('baidu_img')
        if img_size(url_re.content)[0] > 400 and img_size(url_re.content)[1] > 600:  # Only save images with size>600
            print('Image size large enough to be saved')
            open('baidu_img/' + img_name, 'wb').write(url_re.content)

if __name__ == '__main__':
    for i in range(2) : # Only test two pages
        url = 'https://tieba.baidu.com/p/5033202671?pn='+str(i+1)
        req_text = s.get(url).text
        # print(re_test(req_text)) #
        # urls = re_test(req_text)
        # print(bs_test(req_text)) # BS
        urls = bs_test(req_text)
        for img_url in re_test(req_text):
            save_img(img_url)