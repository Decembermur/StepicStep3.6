import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_on_add_in_korziza(browser):
    addInKorzina=browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    addInKorzina.click()
    
    time.sleep(3)
    
    checkOfAdding=browser.find_element_by_css_selector("#messages > div:nth-child(1) > .alertinner ")
    assert checkOfAdding is not None , "Не добавился"