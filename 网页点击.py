from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Edge()
driver.maximize_window()
#driver.get('https://www.baidu.com/')
#driver.find_element(By.ID, "kw").send_keys("向宇翔")
#driver.find_element(By.ID, "su").click()

driver.get('https://weibo.com')
sleep(5)

driver.find_element(By.LINK_TEXT, "热搜榜").click()

for i in range(2,7):
    sleep(1)
    print(f'此时此刻热搜第{i-1}名为：'+driver.find_element(By.XPATH,f'//*[@id="scroller"]/div[1]/div[{i}]/div/div/div/div/div/div[1]/a').text)
    
while 1 :
    pass

print('main add')