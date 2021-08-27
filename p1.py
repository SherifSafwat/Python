from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\home\.wdm\drivers\chromedriver\win32\92.0.4515.43\chromedriver.exe") 
driver.implicitly_wait(5)
#driver.get("https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx")
driver.get("file:///E:/work/vc/h3.html")

elem = driver.find_element_by_name("health-profession")
elem.send_keys("Medical Practitioner")
elem = driver.find_element_by_name("name-reg")
elem.send_keys("mikhail")

#elem.send_keys(Keys.RETURN)

#time.sleep(100)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

#name_elem = driver.find_elements_by_class_name("search-results-table-col")
#name_elem1 = driver.find_elements_by_class_name("search-results-table-col-wrap")
name_elem2 = driver.find_elements_by_class_name("search-results-table-row")

with open("test.txt", "a") as myfile:

    for i,e2 in enumerate(name_elem2): 
        if(i!=0):
            myfile.write(e2.text  +" 2" +'\n')        


print ("done..")


#elem.clear()
#elem.send_keys(Keys.RETURN)
#print (elem.getTagName())




#print (elem.getTagName())
#print (elem.getText())

#elem1.click()
#elem.send_keys(Keys.RETURN)

#print (elem.source)

#print (driver.page_source)

##########################################################

'''
elements = driver.find_elements('p') # By.ID
for e in elements:
    print(e.text)

#elem.set_attribute("value", "Medical Practitioner")

#driver.find_element_by_xpath("//input[ @name='health-profession'][@name='value' and @value='Medical Practitioner']").click()
#driver.find_element_by_xpath("//input[@class='star star-5' and @id='star-5'][@name='star' and @value='5']").click()


#select = Select(driver.find_element_by_id("health-profession"))
#select.SelectByText("Medical Practitioner")
#select.Submit()



'''

'''
#save to file
elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")
with open('./r1', 'wb') as f:
    f.write(source_code.encode('utf-8'))
'''

#assert "No results found." not in driver.page_source

#driver.close()