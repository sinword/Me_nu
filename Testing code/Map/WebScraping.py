from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化 Chrome 瀏覽器
service = Service('/path/to/chromedriver')  # 替換為 ChromeDriver 的路徑
driver = webdriver.Chrome(service=service)

# 打開 Google Maps 並搜索餐廳
driver.get('https://www.google.com/maps')
search_box = driver.find_element(By.ID, 'searchboxinput')
search_box.send_keys('Your Restaurant Name')
search_box.send_keys(Keys.RETURN)

# 等待搜索結果加載並選擇第一個結果
wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'section-result')))
first_result.click()

# 滾動評論區域以加載更多評論
reviews_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[1]/div[2]/button')))
reviews_tab.click()

time.sleep(2)
reviews_scroll = driver.find_element(By.CLASS_NAME, 'section-layout.section-scrollbox.scrollable-y.scrollable-show')
for _ in range(10):  # 滾動多次以加載更多評論
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', reviews_scroll)
    time.sleep(1)

# 抓取評論
reviews = driver.find_elements(By.CLASS_NAME, 'section-review-text')
for review in reviews:
    print(review.text)

# 關閉瀏覽器
driver.quit()
