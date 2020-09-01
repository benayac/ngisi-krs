from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tkinter
import time

def KRSAN(username, password, kode_matkul = []):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://simaster.ugm.ac.id/ugmfw/signin_simaster/signin_proses")
    
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(username)
    
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(password)

    driver.find_element_by_name("submit").click()

    driver.get("https://simaster.ugm.ac.id/sia_krs/input_krs/")
    driver.find_element_by_class_name("btn-warning").click()

    time.sleep(2)
    for matkul in kode_matkul:
        driver.find_element_by_xpath('//*[@id="1_{matkul}"]/table/tbody/tr[1]/td[1]/input').click()