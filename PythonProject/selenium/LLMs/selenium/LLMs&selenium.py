from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 配置 Chrome WebDriver
service = Service(r'D:\prog\chrome\chromedriver-win64\chromedriver.exe')  # 这里需要替换为你的 chromedriver 路径
driver = webdriver.Chrome(service=service)

try:
    # 访问登录页面
    driver.get("http://192.168.56.101:8080/suthr/logon")
    driver.maximize_window()

    # 等待用户名输入框加载
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginBtn")

    # 输入用户名和密码
    username_input.send_keys("hrteacher")
    password_input.send_keys("123456")

    # 点击登录按钮
    login_button.click()

    # 等待页面跳转并确认登录是否成功
    wait.until(EC.url_changes("http://192.168.56.101:8080/suthr/logon"))
    print("登录成功！")

    sleep(3)
except Exception as e:
    print(f"登录过程中发生错误: {e}")

finally:
    # 关闭浏览器
    driver.quit()
