# 멀티 프로세싱으로 웹 스크래핑
# https://beomi.github.io/beomi.github.io_old/

import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_links():    # a tag의 주소를 읽기
    data = requests.get("https://beomi.github.io/beomi.github.io_old/").text
    soup = bs(data, 'html.parser') # 일반적으로 html.parser를 많이 씀
    #print(soup)
    my_titles = soup.select(
        'h3 > a'
    )
    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
    
    return data # 긁은 정보를 리턴
    
def get_content(link):  # a tag에 의한 해당 사이트 문서 내용 중 일부 문자값 읽기.
    abs_link = 'https://beomi.github.io' + link
    print(abs_link)


if __name__ == '__main__':
    start_time = time.time()
    # print(get_links())
    # print(len(get_links())) #잘 긁어오는지 확인
    for link in get_links():
        get_content(link) #주소를 들고 옴
        
        # 직렬처리 1.66
    """
    for link in get_link():
        get_content(link)
    """   
     
    pool = Pool(processes= 4) #병렬처리 / 직렬처리보자 빠름. 0.58
    pool.map(get_content, get_links())

    print('처리 시간 : {}'.format(time.time() - start_time))