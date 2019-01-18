from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time

'''
instagram.com과 같이 브라우저 사이즈 크기에 따라 
표현되는 형태가 변화하는 사이트의 경우
실행될 화면을 default해서 사용 
Dock side(우측상단) 조절해서 사용
'''

driver = webdriver.Chrome('C:/Users/Heain/Desktop/2018_FastCampus/Python/Intermediate/chromedriver.exe')

try:
    driver.get('https://instagram.com')
    
    elem = driver.find_element_by_link_text('로그인')
    elem.click() #tag에게 클릭을 전달하는 방법 

    time.sleep(1) #반응시간 

    elem = driver.find_element_by_name('username') #속성값이 변할 수도 있음(로그인의 id속성값) 따라서 불변 속성값을 찾아서 들어감
    elem.send_keys(ID)
    elem = driver.find_element_by_name('password')
    elem.send_keys(PW)
    elem.send_keys(Keys.RETURN)
    
    time.sleep(3) #반응시간

    elem = driver.find_element_by_class_name('HoLwm') #팝업제거
    elem.send_keys(Keys.RETURN)    
    
    '''
    class 속성값은 보통 의미가 없는 문자열로 되어 있으며
    자꾸 변경된다는 단점이 존재한다
    '''
    elem = driver.find_element_by_xpath("//span[text()='검색']/..")
    ac = ActionChains(driver) #찾고자하는 태그가 덮어져 있을 수 있음. <div>는 key를 전달할 수 없음
    '''위치에서 태그 찾기 --> 마우스 클릭 // 태그가 있는 위치 찾기 --> ActionChains사용'''
    ac.move_to_element(elem) #동작등록
    ac.click() #그 위치로 이동해서 클릭(like human behaving)
    ac.key_down('#파이썬')
    ac.perform() #실행

    time.sleep(2)

    ac.reset_actions() #이전 actions 초기화
    ac.move_by_offset(0, 50) #좌표 이동 x축, y축
    ac.click()
    ac.perform()
    
    time.sleep(5)

    elem = driver.find_element_by_class_name('EZdmt')
    divs = elem.find_elements_by_class_name('v1Nh3')
    ac = ActionChains(driver) #페이지 전환이 있었으므로 새로 AC 생성
    
    for div in divs:
        ac.reset_actions() #iterate
        ac.move_to_element(div)
        ac.click()
        ac.perform()
        
        time.sleep(2)
        
        ac.reset_actions()
        elem = driver.find_element_by_xpath("//*[contains(@aria-label,'좋아요')]")
        ac.move_to_element(elem)
        ac.click()
        ac.perform()
        
        ac.reset_actions()
        ac.send_keys(Keys.ESCAPE)
        ac.perform()

        time.sleep(3)
        
    input()
except Exception as e:
    print(e)

finally:
    driver.quit()
