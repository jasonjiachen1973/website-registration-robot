# 功能：

#  负责 登录 RHCC 网站，找到 网球场选项，进行 自动化订场
#  使用 selenium 自动化网页交互
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_book(username, password, date, court, court_time):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 无头模式，不打开浏览器
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www9.tennisclubsoft.com/rhcc")

        # **等待登录框可见，最多等待 5 秒**
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter email']")))

        # **登录**
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'LOG IN TO YOUR ACCOUNT')]").click()

        # **等待跳转到主页，最多等待 5 秒**
        WebDriverWait(driver, 5).until(EC.url_contains("home"))

        # **等待 Indoor Court 页面可点击，最多等待 5 秒**
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Indoor Court"))).click()

        # **等待日期按钮可点击**
        date_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//td[contains(text(), '{date}')]")))
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
