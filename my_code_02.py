#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import requests
import datetime
import pandas as pd
import numpy as np
import re

driver = webdriver.Chrome('C:/Users/Heain/Desktop/2018_FastCampus/Python/Intermediate/chromedriver.exe', keep_alive=False)
#windows에서 실행할 경우 실행파일의 모든 경로를 작성해야함

my_query = '인공지능'
start_date = '20181201'
end_date = '20181231'
todays_date = datetime.datetime.now().date()


news = str('https://search.naver.com/search.naver?where=news&query='+my_query+'&field=1&nso=so%3Ar%2Cp%3Afrom'+start_date+'to'+end_date+'%2Ca%3At&start=')

try:
    driver.get(news+'1')
    is_next = driver.find_element_by_class_name('title_desc')
    num_article = is_next.find_element_by_tag_name('span').text[-4:-1]
    print('num_article:', num_article)
    num_page = int(int(num_article)/10)+1
    print('num_page:', num_page)

    i = 1
    page_list = []
    page_list.append(i)

    while i < int(num_article):
        i = i+10
        page_list.append(i)
    else:
        pass
    #print(page_list)

except Exception as e:
    page_list = ['1']



columns = ['query','date','title', 'link']
collected = pd.DataFrame(data=None, columns=columns)

try:
    i = 0
    for pages in page_list:
        i = i+1
        driver.get(news+str(pages))

        elem = driver.find_element_by_class_name('news')
        lis = elem.find_elements_by_xpath('./ul/li')
        try:
            for li in lis:
                atag = li.find_element_by_class_name('_sp_each_title')
                title = atag.get_attribute('title')
                link = atag.get_attribute('href')
                w_date = li.find_element_by_class_name('txt_inline')
                W_date = re.findall('([0-9]{4}.[0-9]{2}.[0-9]{2})', w_date.text)

                collect = [my_query, W_date[0], title, link] #;print(collect)
                print(collect)
                collected = collected.append(pd.DataFrame(np.array(collect).reshape(1,4), columns=columns))
            print('collecting',len(lis), 'articles finished!', 'page', i, '/', len(page_list))
        except Exception as e:
            print(e, 'PASS --> page', i, '/', len(page_list))

    save_data = my_query+'_'+'from'+start_date+'to'+end_date+'_'+str(todays_date)+'.csv'
    collected.to_csv(save_data, sep=',', index=False, header=True, encoding = 'cp949')
    print('SAVE!')

    input()
except Exception as e:
    print(e)    
finally:
    driver.quit()



