from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
PATH="../chromedriver.exe"
import time
import re
import chromedriver_binary
driver=Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")

driver.implicitly_wait(10)
username=driver.find_element_by_id("username")

username.clear()
username_user_input=input("Please Enter your username:")


username.send_keys(username_user_input)

password=driver.find_element_by_id("password")

password.clear()
password_user_input=input("Please Enter your password:")
#you need to enter the password manually by typing. Please be fast as you would have only 5 sec to type the kerberos password

password.send_keys(password_user_input)
#time.sleep(8)

captcha_fillin=driver.find_element_by_id("valuepkg3")                #an xpath cant end with /
captcha_fillin.clear()

captcha_q=driver.find_element_by_xpath('//*[@id="login"]')         #the xpath had text() with it we need to remove that before 
command_list=re.split('[\n ]',captcha_q.text)

#print(command_list)

if command_list[7]=="add":
    value=int(command_list[8])+int(command_list[10])
elif command_list[7]=="subtract":
    value=int(command_list[8])-int(command_list[10])
elif command_list[7]=="enter":
    if command_list[8]=="first":
        value=int(command_list[10])
    elif command_list[8]=="second":
        value=int(command_list[12])
     
value_str=str(value)
captcha_fillin.send_keys(value_str)

#time.sleep(10)
login=driver.find_element_by_id("loginbtn")
login.click()


