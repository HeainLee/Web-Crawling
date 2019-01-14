#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import requests



#중요 태그 : div, li 

driver = webdriver.Chrome('C:/Users/Heain/Desktop/2018_FastCampus/Python/Intermediate/chromedriver.exe')
#windows에서 실행할 경우 실행파일의 모든 경로를 작성해야함
#my_query = 'SAMSUNG'

try : 
    driver.get('https://naver.com') #사이트로 이동

    elem = driver.find_element_by_id('query')
    elem.send_keys('LG CNS') #searching for
    elem.send_keys(Keys.RETURN) #enter

    try:
        print('-'*10,'BLOG TITLES','-'*10)
        elem = driver.find_element_by_class_name('_blogBase')
        lis = elem.find_elements_by_tag_name('li')
        for li in lis:
            atag = li.find_element_by_class_name('sh_blog_title')
            print(atag.get_attribute('title')) #get_attribute 속성값에 있는 '값'을 가지고 오는 기능
            print(atag.get_attribute('href')) #link 주소 가져오기 
    except Exception as e:
        print('None')

    try:
        print('\n', '-'*10,'NEWS TITLES','-'*10)
        elem = driver.find_element_by_class_name('news')
        #lis = elem.find_elements_by_tag_name('li') #div하위 모든 li 정보까지 수집 (관련뉴스 포함)
        lis = elem.find_elements_by_xpath('./ul/li') #./현재 위치의 하위 ul/ 하위 li만 가져오기
        for li in lis:
            atag = li.find_element_by_class_name('_sp_each_title')
            print(atag.get_attribute('title'))
            print(atag.get_attribute('href'))
    except Exception as e:
        print('None')

    try:
        print('\n','-'*10,'CAFE TITLES','-'*10)
        elem = driver.find_element_by_class_name('_cafeBase')
        lis = elem.find_elements_by_tag_name('li')
        for li in lis:
            atag= li.find_element_by_class_name('sh_cafe_title')
            title = atag.get_attribute('title') 
            if not title: #속성으로 찾을 수 없을 경우
                title = atag.text
            print(title)
            print(atag.get_attribute('href'))
    except Exception as e:
        print('None')

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
