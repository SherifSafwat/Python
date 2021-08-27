
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


x = 0    


driver = webdriver.Chrome(executable_path=r"C:\Users\home\.wdm\drivers\chromedriver\win32\92.0.4515.43\chromedriver.exe") 
#driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.get("https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx")
driver.get("file:///C:/Users/home/Desktop/joseph.html")


name_elem = driver.find_elements_by_class_name("practitioner")
#label_elem = driver.find_elements_by_class_name("registration-label")
data_elem = driver.find_elements_by_class_name("registration-detail")


with open("test.txt", "a") as myfile:
    for i, e in enumerate(name_elem):
        myfile.write(str(i) + " name " + name_elem[i].text + '\n') 
        #for x in range(12):
        myfile.write(str(x) + " data " + data_elem[x].text + '\n') 
        x=x+1
        while  (len(data_elem) > x) and (data_elem[x].text[:4] != "MED0"): # (len(data_elem[x].text) > 0):
            myfile.write(str(x) + " data " + data_elem[x].text + '\n') 
            x=x+1
            #if (len(data_elem) > x): break 
            
            #myfile.write(str((i*12)+x) + " data " + data_elem[(i*12)+x].text + '\n') 

    myfile.write(str(len(data_elem)) + " count " +  str(len(name_elem)) + '\n')
    
    
    


