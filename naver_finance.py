import os
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
# browser.maximize_window() #maximize window

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="

browser.get(url)

#체크박스 초기화 
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): 
        checkbox.click() 

# 조회 항목 설정 

items_to_select = ["영업이익", "자산총계", "매수총잔량"]
for checkbox in checkboxes: 
    parent = checkbox.find_element(By.XPATH, '..') #Parent Element 
    label = parent.find_element(By.TAG_NAME, 'label')
    # print(label.text) #이름확인 
    if label.text in items_to_select: #선택항목 일치한다면 
        checkbox.click()

# 적용하기 버튼 
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()


for idx in range(1, 41): #1 부터 40페이지까지
    #페이지 이동
    browser.get(url + str(idx)) #page=1, 2 . . .
    
    #데이터 추출 
    df = pd. read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True) #index in this case is row 공간차치하는 부분처리
    df.dropna(axis='columns', how='all', inplace=True) 
    if len(df) == 0: 
        break
#파일 저장 
    f_name = 'sise.csv'
    if os.path.exists(f_name): #If file exists, ignore the header
        df.to_csv(f_name,encoding='utf-8-sig', index=False, mode='a')
    else: #if the file does not exist, include the header
        df.to_csv(f_name,encoding='utf-8-sig', index=False)

    print(f'{idx} Page is complete')

browser.quit()