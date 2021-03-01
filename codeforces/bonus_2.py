from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from string import ascii_uppercase
from pathlib import Path
PATH="../chromedriver.exe"
import chromedriver_binary
import os
import sys
options=webdriver.ChromeOptions()
options.headless=True
driver = Chrome(PATH,options=options)

driver.implicitly_wait(10)

difficulty=sys.argv
#print(contest_number)
url="https://codeforces.com/problemset"
#print(url)
min_diff=sys.argv[1]
max_diff=sys.argv[2]
driver.get(url)

element_min=driver.find_element_by_name("minDifficulty")
element_max=driver.find_element_by_name("maxDifficulty")

element_min.send_keys(min_diff)
element_max.send_keys(max_diff)

apply=driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[5]/form/div[4]/input')
apply.click()

driver.implicitly_wait(10)

num_of_problems=int(input("Please enter number of problems::::"))
contest_directory='./'+"problemset"
Path(contest_directory).mkdir(parents=True,exist_ok=True)

#shift +tab for indenting back
#tab for indenting forward
for i in range(1,num_of_problems+1):
    try:
        XPATH='//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr['+str(i+1)+']/td[1]/a'
        problem=driver.find_element_by_xpath(XPATH)        
        c=problem.text
        problem.click()
        
        contest_problem=contest_directory+"/"+c
        Path(contest_problem).mkdir(parents=True,exist_ok=True)
        
        try:
            S=lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)
            driver.set_window_size(S('Width'),S('Height'))
            screenshot_dir=contest_problem+'/problem.png'
            driver.find_element_by_class_name('problemindexholder').screenshot(screenshot_dir)
            
            
            elements=driver.find_elements_by_class_name('input')
            
            if len(elements)==1:
                file_input_loc=contest_problem+'/input.txt'
                file_input=open(file_input_loc,"w")
                file_input.write(elements[0].text)
            else:
                for element in elements:
                    file_input_loc=contest_problem+'/input'+str(elements.index(element)+1)+'.txt'
                    file_input=open(file_input_loc,"w")
                    file_input.write(element.text)

            elements=driver.find_elements_by_class_name('output')
            
            if len(elements) ==1:
                file_input_loc=contest_problem+'/output.txt'
                file_input=open(file_input_loc,"w")
                file_input.write(elements[0].text)
            else:
                for element in elements:
                    file_output_loc=contest_problem+'/output'+str(elements.index(element)+1)+'.txt'
                    file_output=open(file_output_loc,"w")
                    file_output.write(element.text)
            driver.back()
            driver.implicitly_wait(10)
        except:
            driver.back()
            driver.implicitly_wait(10)
            continue
    except:
        pagination=driver.find_elements_by_class_name('arrow')[-1]
        pagination.click()
        driver.implicitly_wait(10)
    finally:
        driver.quit()            
    #driver.quit()

