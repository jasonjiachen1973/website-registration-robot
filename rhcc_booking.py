# 功能：

#  负责 登录 RHCC 网站，找到 网球场选项，进行 自动化订场
#  使用 selenium 自动化网页交互
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_and_book(username, password, date, court, court_time):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 无头模式，不打开浏览器
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www9.tennisclubsoft.com/rhcc")
        time.sleep(2)

        # 登录
        driver.find_element(By.NAME, "email").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'LOG IN TO YOUR ACCOUNT')]").click()
        time.sleep(3)

        # 进入 Indoor Court 页面
        driver.find_element(By.LINK_TEXT, "Indoor Court").click()
        time.sleep(2)

        # 选择日期
        date_element = driver.find_element(By.XPATH, f"//td[contains(text(), '{date}')]")
        date_element.click()
        time.sleep(2)

        # 选择场地 + 时间
        court_time_xpath = f"//td[contains(text(), '{court_time}')]/following-sibling::td[contains(text(), '{court}')]/..//a[contains(text(), 'Book')]"
        book_button = driver.find_element(By.XPATH, court_time_xpath)
        book_button.click()
        time.sleep(1)

        # 确认预定
        driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()
        time.sleep(2)

        return f"成功订场: {court} - {court_time}"
    except Exception as e:
        return f"订场失败: {str(e)}"
    finally:
        driver.quit()

