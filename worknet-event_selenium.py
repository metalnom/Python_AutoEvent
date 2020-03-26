from selenium.webdriver import Firefox, FirefoxOptions
import time

USER = "<아이디>"
PASS = "<비밀번호>"

options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

url_login = "https://www.work.go.kr/member/bodyLogin.do"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e = browser.find_element_by_id("custId1")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pwd1")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("button.button.blue")
form.click()
print("로그인 버튼을 클릭합니다.")

browser.get("https://www.work.go.kr/event/eventContent.do?eventNo=533")
while True:
    time.sleep(60)
    try:
        coupon = browser.find_element_by_css_selector("#btnCoupon").click()
    except:
        continue
