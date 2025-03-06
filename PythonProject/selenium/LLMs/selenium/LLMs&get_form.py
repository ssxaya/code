from idlelib.mainmenu import menudefs
from attr import attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 配置 Chrome WebDriver
service = Service(r'D:\prog\chrome\chromedriver-win64\chromedriver.exe')  # 这里需要替换为你的 chromedriver 路径
driver = webdriver.Chrome(service=service)

# 登录url
url = "http://192.168.56.101:8080/suthr/logon"
driver.get(url)

forms = driver.find_elements(By.TAG_NAME, "form")

# 遍历获取的from
with open("form_html.txt", "w",encoding="utf-8") as f:
    for form in forms:
        # 获取表单的html
        form_html = form.get_attribute('outerHTML')
        print(f"--------复制以下html代码--------\n\n{form_html}\n\n--------^^^^^^--------",file = f)

    print("生成文件成功")