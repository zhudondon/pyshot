import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')


headers = {
    'Cookie':'_ga=GA1.1.256335447.1719557693; ARK_ID=JSfae9203b28cc91b6137012cce0c4b2dffae9; FZ_STROAGE.workeredu.com=eyJTRUVTSU9OSUQiOiJiOTRhYjQ2NDY2MTk0ODAyIiwiU0VFU0lPTkRBVEUiOjE3MjA1MTQ3MDY2MDgsIkFOU0FQUElEIjoiOTkxNWNiZTcxNDc1ZTczNCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiLyIsIkZSSVNUREFZIjoiMjAyNDA3MDIiLCJGUklTVElNRSI6dHJ1ZSwiQVJLX0lEIjoiSlNmYWU5MjAzYjI4Y2M5MWI2MTM3MDEyY2NlMGM0YjJkZmZhZTkifQ%3D%3D; _ga_YFKNQX5E65=GS1.1.1722939278.6.1.1722939335.0.0.0; BAO_KAO_CLIENT_ID=A9AD90E0DD8DDDE0B66C936E79B9CED6.130174tomcatB; is_cookies=Y; ADMIN_MANAGER=ee4912624cd34189ae1f9137a49cf151; SMS_CODE_zgjyzx001=882176; JSESSIONID=AB2A0D402E519B4DC98C11286770BCAE.130174tomcatB',
    'Origin':'https://eekao.workeredu.com',
    'Referer':'https://eekao.workeredu.com/organization/records/queryExamRecordList.do?&formMap.RESOURCEID=6252b417a9fe879c01a758cb74b6a7b3&formMap.ROLEID=62a5172aa9fe879c01b67f741b40abd8',
    'User-Agent:':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


cookieJson = {
  "FZ_STROAGE.workeredu.com": "eyJTRUVTSU9OSUQiOiI5NzhjYjg2MDJlZDU5YWI4IiwiU0VFU0lPTkRBVEUiOjE3MTc1NzIyMDk0ODYsIkFOU0FQUElEIjoiOTkxNWNiZTcxNDc1ZTczNCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiLyIsIkZSSVNUREFZIjoiMjAyNDA2MDUiLCJGUklTVElNRSI6dHJ1ZSwiQVJLX0lEIjoiSlMzZWIyZTMyZjU1MzA3MGVkMWQ3ZjgyYWVjZGI3MzEyNjNlYjIifQ%3D%3D",
  "ARK_ID": "JS3eb2e32f553070ed1d7f82aecdb731263eb2",
  "BAO_KAO_CLIENT_ID": "D6B14F4DBFB34D84F6CD7B2AFC7BFAA3.130174tomcatB",
  "is_cookies": "Y",
  "ADMIN_MANAGER": "ee4912624cd34189ae1f9137a49cf151",
  "SMS_CODE_zgjyzx001": "882176"
}



# time.sleep(2)

def goPlan(planId,planName):
    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(options=chrome_options)
    firstPage = 'https://eekao.workeredu.com/organization/records/queryExamRecordList.do?&formMap.RESOURCEID=6252b417a9fe879c01a758cb74b6a7b3&formMap.ROLEID=62a5172aa9fe879c01b67f741b40abd8'
    browser.get(firstPage)
    for key in cookieJson.keys():
        browser.add_cookie({'name': str(key), 'value': str(cookieJson.get(key)), 'path': '/'})

    refresh = browser.refresh()
    browser.set_window_size(1920, 1080)

    # print(refresh)
    get = browser.get(firstPage)
    # time.sleep(2)
    # print(get)
    #
    # # browser.find_element(by="id,term_select")
    # 假设driver是你的WebDriver实例

    # 假设driver是你的WebDriver实例
    # jquery_url = 'https://code.jquery.com/jquery-3.6.0.min.js'  # 可以替换为你需要的jQuery版本
    # browser.execute_script(f"var script = document.createElement('script'); script.src = '{jquery_url}'; document.getElementsByTagName('head')[0].appendChild(script);")
    # print(f"{browser.page_source}")

    print(planName)
    browser.execute_script(open('jquey.js').read())
    browser.find_element(by=By.ID, value="term_select").find_element(by=By.XPATH,
                                                                     value="//option[@value='"+ planId+"']").click()
    browser.execute_script('$("#current").val("1");$("#pageCount").val("200");loadpageno();')



    browser.execute_script("initBodyContext();")

    # , 'document.getElementById("current").value = 1; document.getElementById("pageCount").value = 200;'
    element = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.ID, "selPageCount"))
    )
    # browser.execute_script('	document.getElementById("current").value = 1; document.getElementById("pageCount").value = 100;loadpageno();')
    #
    element.find_element(by=By.XPATH, value="//option[@value='100']").click()

    time.sleep(2)
    # getExamRecordDetail('3728c391f3fb48d6910bdce0132b57ef')

    elements = browser.find_element(by=By.ID, value="examRecordHtml").find_elements(by=By.XPATH, value="//td/a")
    allChooseId = []
    for ele in elements:
        if ele.get_dom_attribute("data-original-title") == "查看详情":
            attribute = ele.get_dom_attribute("onclick")
            attribute = attribute.replace("getExamRecordDetail(", "")
            attribute = attribute.replace(")", "")
            attribute = attribute.replace("'", "")
            print(attribute)
            allChooseId.append(attribute)

    savePath = "D:/Users/Administrator/python/pythonProject/images/"
    targetUrl = "https://eekao.workeredu.com/organization/records/detail.do?formMap.CHOOSE_ID="

    for chooseId in allChooseId:
        curUrl = targetUrl + chooseId
        # 进入页面
        browser.get(curUrl)
        time.sleep(2)
        if os.path.isdir(savePath + planName) == False:
            os.mkdir(savePath + planName)
        element = browser.find_element(by=By.ID, value="bodyContext")
        if element is not None and not element.text.__contains__("暂无考试记录"):
            elementDt = element.find_element(by=By.XPATH, value="//dl/dt")
            if elementDt is not None:
                fileName = elementDt.text
                browser.save_screenshot(savePath + planName + "/" + fileName + ".png")

# browser.save_screenshot("D:/Users/Administrator/python/pythonProject/images/one.png")


planMap = {
    "e2b1e08df6c240f79947050c219ce8ae":"粤华物业管理员四级(15-16日)",
    # "bb998e0e14814f2bb2a95dee827107c6":"粤华物业管理员三级（15-16日）", ok
    # "30ebd4cce4a5461b88b95ff064bd48a0":"粤华客户服务管理员三级（15-16日）",ok
    "07f4747bc134419b8ae22a9f9ec8cc42":"2023.05.19-05.20粤华物业管理员四级",
    "009600afb6864cdab2869ea69c20b967":"2023粤华保洁员四级",
    # "96f853fa5ef0486e80e96aa9370f3868":"2023粤华保洁员五级", ok
    # "503250cbf1b14247ab8402de19414390":"2023粤华客户服务管理员三级", ok
    # "74609af4837943c58a62611760ea2ef8":"2023粤华物业管理员三级",ok
    "afe6a5eb4af941cf91c1d202a38772c0":"2023粤华物业管理员四级",
    "d95e8ee79cc84aedaf0a7cd122febef3":"粤华物业管理员四级",
    "7e28febc872342fa99f5379f76ab8513":"粤华物业管理员三级",
    "537861ae143f49098ed04147833524fb":"粤华客户服务管理员客观题三级"
}

for key in planMap:
    goPlan(key, planMap.get(key))







browser.quit()