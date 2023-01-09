import selenium
# import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


import time
import re
import pyperclip

# 자동화 시동
chrome_option = Options()
chrome_option.add_argument("User_Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
# naver_url = 'http://localhost:8080/'
url= 'http://google.com'
driver = webdriver.Chrome('chromedriver.exe')
time.sleep(3)
driver.get(url)
time.sleep(1)




#parsing > log
def remove_html_tags(data):
    p=re.compile(r'<.*?')
    return p.sub('',str(data))

def get_crawl(URL):
    response = driver.get(URL)
    html = driver.page_source
    soup7 = BeautifulSoup(html,'html.parser')
    ex_log_divs = soup7.find('div, {id : view_content}')
    crawl_data = remove_html_tags(ex_log_divs)
    return crawl_data
    
elem = driver.find_element(By.XPATH,'//*[@id="account"]/a').click()

#로그인 아이디, 비밀번호 입력 및 로그인 성공
id_insert = driver.find_element(By.NAME,'id')
pw_insert = driver.find_element(By.NAME,'pw')
# id_insert = elem.find_element(By.XPATH,'//*[@id="id"]').send_keys('<yuoijn08')
# pw_insert = elem.find_element(By.XPATH,'//*[@id="pw"]').send_keys('<dbwlssla 20!')
# log_success = elem.find_element(BY.XPATH, '//*[@id="log.login"]')
#로그인 아이디, 비밀번호 입력
# id_insert.click()
# pyperclip.copy('yuoijn08')
# id_insert.send_keys 