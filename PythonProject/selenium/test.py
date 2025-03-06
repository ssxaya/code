from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


from selenium.webdriver.support.wait import WebDriverWait

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(service=Service(r'D:\prog\chrome\chromedriver-win64\chromedriver.exe'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')

driver.find_element(By.LINK_TEXT,"即刻体验 AI搜索DeepSeek-R1满血版").click()

driver.find_element(By.CSS_SELECTOR,"#chat-input-box").send_keys(key)
# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序')