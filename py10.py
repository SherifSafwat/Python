from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


with open(r"./10code.txt") as f:
    code = f.read().splitlines()
with open(r"./10first.txt") as f:
    first = f.read().splitlines()
with open(r"./10last.txt") as f:
    last = f.read().splitlines()    

driver = webdriver.Chrome(executable_path=r"C:\Users\home\.wdm\drivers\chromedriver\win32\92.0.4515.43\chromedriver.exe") 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx")


for i, e in enumerate(code):

    elem = driver.find_element_by_id("content_0_contentcolumnmain_0_ddlProfession")
    elem.send_keys("Medical Practitioner")

    elem = driver.find_element_by_name("content_0$contentcolumnmain_0$txtFamilyName")
    elem.send_keys(last[i])

    elem = driver.find_element_by_name("content_0$contentcolumnmain_0$txtGivenName")
    elem.send_keys(first[i])

    elem.send_keys(Keys.RETURN)

    name_elem = driver.find_elements_by_class_name("practitioner")
    #label_elem = driver.find_elements_by_class_name("registration-label")
    data_elem = driver.find_elements_by_class_name("registration-detail")

        

    x = 0

    with open("test.txt", "a") as myfile:

        myfile.write("zzz" + '\n')
        myfile.write(code[i] + '\n')
        myfile.write(first[i] + '\n')
        myfile.write(last[i] + '\n')
        myfile.write(str(len(name_elem)) + '\n')
        myfile.write(str(len(data_elem)) + '\n')

        for i, e in enumerate(name_elem):
            myfile.write(name_elem[i].text + '\n') 
            myfile.write(data_elem[x].text + '\n') 
            x=x+1
            while  (len(data_elem) > x) and (data_elem[x].text[:4] != "MED0"): 
                myfile.write(data_elem[x].text + '\n') 
                x=x+1
                

    elem = driver.find_element_by_id("content_0_contentcolumnmain_0_lnkSearchResultReload")
    elem.click()        
