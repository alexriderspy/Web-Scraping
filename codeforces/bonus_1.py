from selenium import webdriver
from selenium.webdriver import Chrome
from string import ascii_uppercase
from pathlib import Path
PATH="../chromedriver.exe"
import chromedriver_binary
import os
import sys

def char_range(c1, c2):
    #"""Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

options=webdriver.ChromeOptions()
options.headless=True
driver = Chrome(PATH,options=options)

driver.implicitly_wait(10)

num_of_contests=int(sys.argv[1])
#print(contest_number)
url='https://codeforces.com/contests'
#print(url)
driver.get(url)
contest_directory_parent='./contests'
Path(contest_directory_parent).mkdir(parents=True,exist_ok=True)

#shift +tab for indenting back
#tab for indenting forward
for i in range(1,num_of_contests+1):
    try:
        XPATH='//*[@id="pageContent"]/div[1]/div[2]/div[1]/div[6]/table/tbody/tr['+str(i+1)+']/td[1]/a[1]'
        contest=driver.find_element_by_xpath(XPATH)        
        contest.click()
        contest_identity=driver.current_url.split('/')[-1]
        contest_directory=contest_directory_parent+'/'+contest_identity
        for c in char_range('A','F'):
            try:
                try:
                    problem=driver.find_element_by_link_text(c)
                    problem.click()
                except:
                    continue
                contest_problem=contest_directory+"/"+c
                Path(contest_problem).mkdir(parents=True,exist_ok=True)
                
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
                driver.implicitly_wait(5)
            except:
                driver.back()
                driver.implicitly_wait(5)
                
                continue

        driver.back()
        driver.implicitly_wait(5)
    except:
        pagination=driver.find_elements_by_class_name('arrow')[-1]
        pagination.click()
    finally:
        driver.quit()