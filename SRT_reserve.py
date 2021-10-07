import pyautogui
import time as t
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

ID = "회원번호 입력"                # 회원번호 (숫자 10자리)
PW = "비밀번호 입력"                # 비밀번호

url    = "https://etk.srail.kr/cmc/01/selectLoginForm.do"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(15) 
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.find_element_by_id('srchDvNm01').send_keys(ID)
driver.find_element_by_id('hmpgPwdCphd01').send_keys(PW)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()

driver.implicitly_wait(15)

driver.find_element_by_id('arvRsStnCd').click()
driver.find_element_by_xpath('//*[@id="dptRsStnCd"]/option[15]').click()                # 출발지
driver.find_element_by_xpath('//*[@id="arvRsStnCd"]/option[5]').click()                 # 도착지
# 출발지 도착지 코드 :                수서 02 / 동탄 03 / 평택지제 04 / 천안아산 05 / 오송 06 / 대전 07 / 김천(구미) 08 / 동대구 09 / 신경주 10 /
# option 숫자를 변경해주세요          울산(통도사) 11 / 부산 12 / 공주 13 / 익산 14 / 정읍 15 / 광주송정 16 / 나주 17 / 목포 18

date_ele = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[3]/div/input[1]')  
driver.execute_script("arguments[0].setAttribute('value','2021.09.22')", date_ele)              # 날짜
driver.find_element_by_xpath('//*[@id="dptTm"]/option[1]').click()                              # 출발시간
driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/a').click()
driver.implicitly_wait(10)
t.sleep(3)
i = 0
find = 0


while True:
    try:
        i += 1
        print("{}번째 시도...".format(i))
        driver.find_element_by_xpath('//*[@id="search_top_tag"]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        t.sleep(0.5)
        for n in range(1, 11):                 # 1페이지 기차 수. 돌리기 전 미리 (1, 11)에서 11의 숫자를 바꿔놓아야 함.
            print(n)
            if driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[7]/a').text == "예약하기":
                driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[7]/a').send_keys(Keys.ENTER)
                find == 1
                break
                
                # 신청하기 부분은 혹시 예매칸이 다 차서 나올 경우에 주석 빼고 쓰면 됩니다.
                
            # if driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[8]/a').text == "신청하기":
            #     driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[8]/a').send_keys(Keys.ENTER)
            #     find == 1
            #     break
        if find == 1:
            break
        if find == 0:
            driver.find_element_by_xpath('//*[@id="result-form"]/fieldset/div[8]/input').send_keys(Keys.ENTER)
            driver.implicitly_wait(10)
            t.sleep(0.5)
            #try:
            for n in range(1, 10):              # 2페이지 기차 수. 돌리기 전 미리 (1, 10)에서 10의 숫자를 바꿔놓아야 함. 숫자 기준은 +1. 2페이지 기차가 7대라면 10을 8로 변경할 것.
                # 이부분 잘하면 for 말고 try, except를 써서 넘어가게 할 수 있을듯?
                print(n)
                if driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[7]/a').text == "예약하기":
                    driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[7]/a').send_keys(Keys.ENTER)
                    find == 1
                    break
                # if driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[8]/a').text == "신청하기":
                #     driver.find_element_by_xpath(f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[8]/a').send_keys(Keys.ENTER)
                #     find == 1
                #     break
            if find == 1:
                break
            if find == 0:
                driver.find_element_by_xpath('//*[@id="result-form"]/fieldset/div[8]/input[1]').send_keys(Keys.ENTER)
                driver.implicitly_wait(10)
                print("No Search.. Try Again.")

        t.sleep(random.uniform(1.5, 4))
    except:
        pyautogui.alert(("!!예매에 성공했습니다. 10분안에 결재해주세요.!!\n\n◎ 이미 예매된 좌석이라고 나올 경우 프로그램을 다시 실행해주세요.")
        t.sleep(3600)
