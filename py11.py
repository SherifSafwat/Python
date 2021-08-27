from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


with open(r"./10code.txt") as f:
    code = f.read().splitlines()
with open(r"./10first.txt") as f:
    first = f.read().splitlines()
with open(r"./10last.txt") as f:
    last = f.read().splitlines()    

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=r"C:\Users\home\.wdm\drivers\chromedriver\win32\92.0.4515.43\chromedriver.exe") 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(5)
driver.get("https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx")


for i, e in enumerate(code):

    elem = driver.find_element_by_name("name-reg")
    elem.clear()
    elem.send_keys(first[i] +" "+ last[i])
    elem.send_keys(Keys.RETURN)

    name_elem = driver.find_elements_by_class_name("search-results-table-row")
        
    with open("test.txt", "a") as myfile:
        myfile.write("zzz" + '\n')
        myfile.write(code[i] + '\n')
        myfile.write(first[i] + '\n')
        myfile.write(last[i] + '\n')
        myfile.write(str(len(name_elem)-1) + '\n')

        for i,e2 in enumerate(name_elem): 
            if(i!=0):
                myfile.write(e2.text +'\n')       

                
    
