import requests
from bs4 import BeautifulSoup

url='https://movie.douban.com/chart'

res=requests.get(url)
res.encoding='utf-8'
html=res.text
#print(html)
soup=BeautifulSoup(html,'html.parser')

def getMovieDetail(movieurl):
    result={}
    resl=requests.get(movieurl)
    resl.encoding='utf-8'
    soup=BeautifulSoup(resl.text,'html.parser')
    result['导演：']=soup.select('.info span a[class="name"]')[0].text
    result['类型：']=soup.select('#info span[property="v:genre"]')[0].text
    result['time：']=soup.select('#info span[property="v:initialReleaseDate"]')[0].text
    result['片长:'] =soup.select('#info span[property="v:runtime"]')[0].text
    result['剧情简介：']=soup.select('#link-report span[property="v:summary"]')[0].text.strip()
    print (result)


def Movie():
    for movie in soup.select('div[class="pl2"]'):
        a1=(movie.select('a')[0].text.strip())
        aurl= (movie.select('a')[0]['href'])
        score=(movie.select('span[class="rating_nums"]')[0].text)
        number=(movie.select('span[class="pl"]')[0].text)
        print('电影：'+a1,'网址'+aurl,'评分：'+score,'评价人数：'+number)
        getMovieDetail(aurl)

Movie()
