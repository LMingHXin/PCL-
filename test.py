from selenium import webdriver
import random
driver = webdriver.Chrome()
driver.get('https://www.wjx.cn/jq/22452252.aspx') 
answers = driver.find_elements_by_css_selector('.div_question')
for i in range(5):
    for answer in answers:
        try:
            ####先滑到标签再去点击
            driver.execute_script("arguments[0].scrollIntoView();",answer)
            ### 找到标签
            ans=answer.find_elements_by_css_selector('li')
            if not ans:
                text=answer.find_element_by_css_selector('textarea')
                text.send_keys('没有')
                continue
            lsans=random.choice(ans)
            lsans.click()
        except Exception as e:
            print(e)
    am=driver.find_element_by_css_selector('#submit_button')
    #am.click()     
#driver.quit()
    
    
