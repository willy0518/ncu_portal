import smtplib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




base_url = 'https://portal.ncu.edu.tw/login'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')


def tosendemail(msg):
    SUBJECT = '中央大學人事系統 '+ msg
    TEXT = '中央大學人事系統 ' + msg
    content = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    
    
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('willy008093@gmail.com','xskxtyiiwmqhejyn')
    mail.sendmail('willy008093@gmail.com','willy008093@gmail.com',content.encode('utf-8'))
    mail.close()


if __name__ == '__main__':

    print('開始簽到.....')
    try:
        browser.get(base_url)
        browser.find_element_by_name('j_username').send_keys('107423052')
        browser.find_element_by_name('j_password').send_keys('Willy23052!')
        browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/form/fieldset/div[3]/div/button').click()

        browser.get(browser.current_url+'/system/143')
        browser.get(browser.current_url+'/student/stdSignIn')

        browser.find_element_by_xpath('//*[@id="table1"]/tbody/tr[3]/td[6]/a[1]').click()
        browser.get(browser.current_url)

        if browser.find_element_by_xpath('//*[@id="signin"]'):
            #browser.find_element_by_xpath('//*[@id="signin"]').click()
            print('簽到成功......')
            tosendemail('簽到成功......')
            browser.close()
        else:
            tosendemail('簽到失敗......')
    except Exception:
        tosendemail('簽到失敗......')







