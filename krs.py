from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time

def main():

    top = Tk()
    labelUsername = Label(top, text="Username")
    labelUsername.grid(row=0, column=0, padx=(10,20), pady=(10,10))
    entryUsername = Entry(top, width=30)
    entryUsername.grid(row=0, column=1, padx=(0, 10))

    labelPassword = Label(top, text="Password")
    entryPassword = Entry(top, width=30, show="*")
    labelPassword.grid(row=1, column=0, padx=(10,20), pady=(10,10))
    entryPassword.grid(row=1, column=1, padx=(0, 10))

    labelMatkul = Label(top, text="Matkul : Kelas\ncontoh:\nTKIT16022:A,\nTKIT16023:B")
    labelMatkul.grid(row=2, column=0, padx=(10,20), pady=(10,10))
    entryMatkul = ScrolledText(top, width=20, height=10)
    entryMatkul.grid(row=2, column=1, padx=(0,10), pady=(10,10))

    loginBtn = Button(top, text="Start KRS", command=lambda: KRSAN(entryUsername.get(), entryPassword.get(), getMatkulKelas(entryMatkul.get("1.0", END))))
    loginBtn.grid(row=3, columnspan=2, sticky="nsew", padx=(10,10), pady=(10,10))

    top.mainloop()

def getMatkulKelas(entry):
    matkul_kelas = ("".join(entry.split())).split(',')
    matkul_kelas_dict = {}
    for item in matkul_kelas:
        itm = item.split(':')
        matkul_kelas_dict[itm[0]] = itm[1]
    return matkul_kelas_dict

def KRSAN(username, password, kode_matkul_kelas):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://simaster.ugm.ac.id/ugmfw/signin_simaster/signin_proses")
    
    user = driver.find_element_by_id("username")
    user.clear()
    user.send_keys(username)
    
    passw = driver.find_element_by_id("password")
    passw.clear()
    passw.send_keys(password)

    driver.find_element_by_name("submit").click()

    assert(driver.title == 'SIMASTER UGM: Beranda')
    driver.get("https://simaster.ugm.ac.id/sia_krs/input_krs/")
    driver.find_element_by_class_name("btn-warning").click()

    time.sleep(1)
    for matkul in kode_matkul_kelas:
        if kode_matkul_kelas[matkul].upper() == 'A':
            kelas = 1
        elif kode_matkul_kelas[matkul].upper() == 'B':
            kelas = 2
        elif kode_matkul_kelas[matkul].upper() == 'C':
            kelas = 3
        matkul.strip()
        driver.find_element_by_xpath(f'//*[@id="1_{matkul}"]/table/tbody/tr[{kelas}]/td[1]/input').click()

main()