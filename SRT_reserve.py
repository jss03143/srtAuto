import pyautogui
import winsound
import time as t
import random
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

ID = "회원번호"                # 회원번호 (숫자 10자리)
PW = "비밀번호"                # 비밀번호

subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

url    = "https://etk.srail.kr/cmc/01/selectLoginForm.do"
# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
driver.implicitly_wait(15) 
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.find_element(By.ID,'srchDvNm01').send_keys(ID)
driver.find_element(By.ID,'hmpgPwdCphd01').send_keys(PW)
driver.find_element(By.XPATH,'//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()

driver.implicitly_wait(15)

driver.find_element(By.ID,'arvRsStnCd').click()
driver.find_element(By.XPATH,'//*[@id="dptRsStnCd"]/option[옵션 코드]').click()                # 출발지
driver.find_element(By.XPATH,'//*[@id="arvRsStnCd"]/option[옵션 코드]').click()                 # 도착지
# 출발지 도착지 코드 :                수서 02 / 동탄 03 / 평택지제 04 / 천안아산 32 / 오송 06 / 대전 07 / 김천(구미) 08 / 서대구 09 / 동대구 10
# option 숫자를 변경해주세요          신경주 11 / 울산(통도사) 12 / 부산 13 / 공주 14 / 익산 15 / 정읍 27 / 광주송정 17 / 나주 18 / 목포 19

date_ele = driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/div[3]/div/input[1]')  
driver.execute_script("arguments[0].setAttribute('value','2025.07.24')", date_ele)              # 날짜 (한 자릿수일 경우 꼭 0을 붙일 것)
driver.find_element(By.XPATH,'//*[@id="dptTm"]/option[출발시간]').click()                              # 출발시간 0시 1 / 2시 2 / 4시 3 / 6시 4 .... 18시 / 10 (원하는 짝수 시간 / 2 + 1)
driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/a').click()
driver.implicitly_wait(30)
t.sleep(5)
i = 0
find = 0

########## SRT만 체크 ##########
element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/form/fieldset/div[1]/div/ul/li[4]/div[2]/label[2]')
driver.execute_script("arguments[0].click();", element)
###############################

while True:
    try:
        i += 1
        nowtime = datetime.datetime.now()
        print(f"{nowtime} - {i}번째 시도...")
        driver.find_element(By.XPATH,'//*[@id="search_top_tag"]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(30)
        t.sleep(3)
        # 원하는 시간의 위치로 바꿀 것. 18시의 18시 4분, 19시 40분의 기차에서 19시 40분만 원할 경우 for n in range(2, 3)으로 변경
        for n in range(1, 2):                 # 1페이지 기차 수. 돌리기 전 미리 (1, 11)에서 11의 숫자를 바꿔놓아야 함. 
            print(n)
            if driver.find_element(By.XPATH,f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[7]/a').text == "예약하기":
                driver.find_element(By.XPATH,f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{n}]/td[7]/a').send_keys(Keys.ENTER)
                find == 1
                break

        if find == 1:
            break


        t.sleep(random.uniform(1.5, 4))
    except:
        winsound.PlaySound('game_levelup.wav', winsound.SND_FILENAME)
        pyautogui.alert("!!예매에 성공했습니다. 10분안에 결재해주세요.!!\n\n◎ 이미 예매된 좌석이라고 나올 경우 프로그램을 다시 실행해주세요.")
        t.sleep(3600)
