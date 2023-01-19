import selenium
import pyperclip
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 자동화 시동
chrome_option = Options()#브라우저 꺼짐 방지
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option) #크롬 드라이버 최신버전 자동설치
# driver = webdriver.Chrome(options=options)
driver.maximize_window() #화면 최대화
driver.implicitly_wait(5) #사이트 로딩시간 5초 대기
# chrome_option.add_argument("User_Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
# naver_url = 'http://localhost:8080/'
url= 'http://naver.com'
userid='yuoijn08'
userpw='dbwlssla20!'
driver.get(url)
time.sleep(5)
# def nlog_bt():
#     nelem=driver.find_element(By.CLASS_NAME,'link_login')
#     nelem.click()

# nlog_bt()
# parsing > log

elem = driver.find_element (By.CLASS_NAME, 'link_login')
elem.click()

# def remove_html_tags(data):
#     p=re.compile(r'<.*?')
#     return p.sub('',str(data))

# def get_crawl(URL):
#     response = driver.get(URL)
#     html = driver.page_source
#     soup7 = BeautifulSoup(html,'html.parser')
#     ex_log_divs = soup7.find('div, {id : view_content}')
#     crawl_data = remove_html_tags(ex_log_divs)
#     return crawl_data
    
# elem = driver.find_element(By.XPATH,'//*[@id="account"]/a').click()

#로그인 아이디, 비밀번호 입력 및 로그인 성공
def insert_id(id):
    id = driver.find_element(By.ID,'id')
    id.click()
    pyperclip.copy(userid)
    id.send_keys(Keys.CONTROL,'v')
    time.sleep(2)
insert_id(userid)

def insert_pw(pw):
    pw = driver.find_element(By.ID,'pw')
    pw.click()
    pyperclip.copy(userpw)
    pw.send_keys(Keys.CONTROL,'v')
    time.sleep(2)
insert_pw(userpw)

def log_bt():
    print(1)
    lo_bt = driver.find_element(By.ID,'log.login').click()

log_bt()

time.sleep(10)