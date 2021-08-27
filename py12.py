import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager

with open(r"./10first.txt") as f:
    first = f.read().splitlines()
with open(r"./10last.txt") as f:
    last = f.read().splitlines()    

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=r"C:\Users\home\.wdm\drivers\chromedriver\win32\92.0.4515.43\chromedriver.exe") 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx")


elem = driver.find_element_by_name("health-profession")
driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);",  elem,  "value", "Medical Practitioner")

with open("test3000111.txt", "a") as myfile:

    #for i, e in enumerate(code):
    for i in range(2312, 2313):
        
        elem = driver.find_element_by_name("name-reg")
        #elem.clear()
        #time.sleep(2)

        driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);",  elem,  "value", first[i] +" "+ last[i])

        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        name_elem = driver.find_elements_by_class_name("search-results-table-row")
        #time.sleep(5)
            
        #with open("test150011.txt", "a") as myfile:
        myfile.write("zzz" + '\n')
        myfile.write(str(i) + '\n')
        myfile.write(first[i] + '\n')
        myfile.write(last[i] + '\n')
        myfile.write(name_elem[1].text +'\n')

        
        print (i)       

print ("done..")
                
    
