from selenium import webdriver
from selenium.webdriver import Chrome
from string import ascii_uppercase
from pathlib import Path

import chromedriver_binary
import os
import sys

def char_range(c1, c2):
    #"""Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

options=webdriver.ChromeOptions()
options.headless=True
driver = Chrome(options=options)

driver.implicitly_wait(10)

contest_number=sys.argv
#print(contest_number)
url='https://codeforces.com/contest/%s/' % contest_number[1]
#print(url)
driver.get(url)
contest_directory='./'+contest_number[1]
Path(contest_directory).mkdir(parents=True,exist_ok=True)

#shift +tab for indenting back
#tab for indenting forward

for c in char_range('A','F'):
    try:
        problem=driver.find_element_by_link_text(c)
        problem.click()
            
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
        continue

