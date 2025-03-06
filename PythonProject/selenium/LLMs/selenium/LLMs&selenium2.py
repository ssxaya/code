from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

# 定义用户名和密码为变量
USERNAME = "hrteacher"
PASSWORD = "123456"

# 设置WebDriver路径，假设你已安装了Chrome浏览器和ChromeDriver
service = Service(r'D:\prog\chrome\chromedriver-win64\chromedriver.exe')  # 这里需要替换为你的 chromedriver 路径
driver = webdriver.Chrome(service=service)

# 打开登录页面
driver.get("http://192.168.56.101:8080/suthr/logon")

# 输入用户名和密码
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# 填充用户名和密码
username.send_keys(USERNAME)
password.send_keys(PASSWORD)

# 点击登录按钮
login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()

# 等待页面加载
time.sleep(3)

# 可以在这里添加断言或其他检查，以验证登录是否成功
# 比如：assert "欢迎" in driver.page_source

# 关闭浏览器
driver.quit()