# 功能：

#  负责 登录 RHCC 网站，找到 网球场选项，进行 自动化订场
#  使用 selenium 自动化网页交互
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def format_date(date):
    dt = datetime.strptime(date, "%Y-%m-%d")  # 转换成 datetime 对象
    return dt.strftime("%a, %b %d").upper()  # 变成 "WED, MAR 12"

def login_and_book(username, password, date, court, court_time):
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # 无头模式，不打开浏览器
    #driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www9.tennisclubsoft.com/rhcc")

        # **等待登录框可见，最多等待 5 秒**
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter email']")))

        # **登录**
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter password']").send_keys(password)
        # 等待按钮加载完成，最多 5 秒
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='submit']"))
        )
        login_button.click()

        # **等待跳转到主页，最多等待 5 秒**
        WebDriverWait(driver, 5).until(EC.url_contains("home"))

        # **转换日期格式**
        formatted_date = format_date(date)  # "WED, MAR 12"
        
        # **等待 Indoor Court 页面可点击，并滚动到它**
        indoor_court_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Indoor Courts')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", indoor_court_link)
        indoor_court_link.click()

        # **等待日期按钮可点击**
        date_xpath = f"//a[contains(text(), '[ {formatted_date} ]')]"
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        date_element.click()

        # **等待场地 + 时间按钮可点击**
        court_time_xpath = f"//td[contains(text(), '{court_time}')]/following-sibling::td[contains(text(), '{court}')]/..//a[contains(text(), 'Book')]"
        book_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, court_time_xpath)))
        book_button.click()

        # **等待确认按钮可点击**
        confirm_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]")))
        confirm_button.click()

        return f"✅ 订场成功: {court} - {court_time}"

    except Exception as e:
        return f"⚠️ 订场失败: {str(e)}"

    finally:
        driver.quit()
