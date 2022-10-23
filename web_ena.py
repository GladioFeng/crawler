#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support import ui
import subprocess
from web_basic_function import driverBuild, try_elem_click, try_elem_send

#  help = '''
#  options:
    #  -i: biosample list file, one line one record
#  '''
#
#  for i in range(1, len(sys.argv)):
    #  if sys.argv[i] == '-i':
        #  inp = sys.argv[i+1]
    #  elif sys.argv[i] == '-h':
        #  print(help)
        #  sys.exit()

url = "https://www.ebi.ac.uk/ena/browser/search"

driver = driverBuild('y')

wait_time = 60
wait = ui.WebDriverWait(driver, wait_time)
#  biosample = 'PRJNA119571'
inp = '/home/fzr/Downloads/biosample_id.txt'
biosamples = []
with open(inp, 'r') as fn:
    for line in fn:
        l = line.strip()
        biosamples.append(l)

print(biosamples)

for biosample in biosamples:
    driver.get(url)

    if try_elem_send(wait, '//*[@id="topSearchDiv"]/div[2]/form/div/div[1]/input', 'xpath', biosample, driver):
        pass
    else:
        print(f'{biosample} count a error')
        continue
    print('here')
    if try_elem_click(wait, '//*[@id="topSearchDiv"]/div[2]/form/div/div[2]/button', 'xpath', driver):
        pass
    else:
        print(f'{biosample} count a error')
        continue
    # show column selection
    if try_elem_click(wait, '//*[@id="mat-expansion-panel-header-0"]/span[1]/mat-panel-description/span', 'xpath', driver):
        pass
    else:
        print(f'{biosample} count a error')
        continue
    # aspera checkbox
    if driver.find_element(by='xpath', value='//*[@id="mat-checkbox-10-input"]').is_selected():
        pass
    else:
        if try_elem_click(wait, '//*[@id="mat-checkbox-10"]/label/div', 'xpath', driver):
            pass
        else:
            print(f'{biosample} count a error')
            continue
    # download txt file
    if try_elem_click(wait, '//*[@id="view-content-col"]/div[4]/div/div[2]/app-read-file-links/div/div[2]/div[1]/a[2]', 'xpath', driver):
        pass
    else:
        print(f'{biosample} count a error')
        continue
 
# TODO: 需要写一个检测appera 是否勾选的脚本,不然有一半的txt文件下载不到aspera file
