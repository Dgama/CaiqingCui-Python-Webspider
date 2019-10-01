from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
import requests
from  urllib.parse import quote

browser= webdriver.Chrome()

# try:
#     browser.get('https://www.baidu.com')
#     input=browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait=WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# browser.get('https://www.taobao.com')
# input_first=browser.find_element_by_id('q')
# input_seconed=browser.find_element_by_css_selector('#q')
# input_third=browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_seconed,input_third)
# browser.close()

# browser.get('https://www.taobao.com')
# input=browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button=browser.find_element_by_class_name('btn-search')
# button.click()

# url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to_frame('iframeResult')
# source=browser.find_element_by_css_selector('#draggable')
# target=browser.find_element_by_css_selector('#droppable')
# actions=ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To bottom")')

# browser.get('https://www.zhihu.com/explore')
# logo=browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

# browser.get('https://www.zhihu.com/explore')
# browser.get('https://www.taobao.com/')
# browser.back()
# browser.forward()
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germy'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())
# browser.execute_script('window.open()')
# browser.switch_to_window(browser.window_handles[1])
# browser.get('http://www.baidu.com')

# function main(splash,args)
#   local get_div_count=splash:jsfunc([[
#     function(){
#     var body=document.body;
#     var divs=body.getElementsByTagName('div');
#     return divs
#   }
#     ]])
#   splash:go("https://www.baidu.com")
#   return get_div_count()
#  end

# function main(splash,args)
#   local snapshots={}
#   local timer= splash:call_later(function()
#     snapshots["a"]=splash:png()
#     splash:wait(1.0)
#     snapshots["b"]=splash:png()
#     end,0.2)
#   splash:go("https://www.taobao.com")
#   splash:wait(3.0)
#   return snapshots
#  end

# url='http://localhost:8050/execute?lua_source='
# lua='''
# function main(splash)
#     return 'hello'
# end
# '''
# url+=quote(lua)
# response=requests.get(url)
# print(response.text)