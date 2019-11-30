from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait, Select
import csv
import time
from PIL import Image
import pytesseract
from io import BytesIO
import urllib.request as ul



list = ["A-Motorcycle, Scooter, Moped",
"B-Car, Jeep, Delivery Van",
"C-Tempo, Autorickshaw",
"C1-ERickshaw",
"D-Powertiller",
"E-Tractor, Trailer Tractor (Low Bed)",
"H-Road Toller, Dozer",
"H1-DOZER",
"H2-ROAD ROLLER",
"I-Crane, Fire brigade, Loader",
"I1-CRANE, MOBILE CRANE, CRANE MOUNTED TRUCK",
"I2-FIRE BRIGAD",
"I3-LOADER",
"J1-EXCAVATOR",
"J2-BACKHOE LOADER",
"J3-GRADER",
"J4-FORKLIFT",
"J5-Other",
"K-Scooter, Moped"]
a = 1

for i in list:
    print(a,":  ",i)
    a +=1


choice = str(input("Choose the type of liscence you want (1-19):\t"))

front = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
back = [1,2,3,23,4,5,8,21,22,9,14,15,16,17,18,19,20,10,50]
for (fr, bk) in zip(front, back):
    if choice == str(fr):
        choice = str(bk)
        break




driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver.get("https://onlineedlreg.dotm.gov.np/dlNewRegHome")
driver.maximize_window()
driver.implicitly_wait("10")

ele = driver.find_element_by_id("newDlApplicationEntry__statusType")
drp = Select(ele)
drp.select_by_visible_text("NEWLICENSE")
time.sleep(3)
driver.find_element(By.ID, "confirmBox").click()
time.sleep(3)


#function to screenshot of captche


first_name = "Roman"
middle_name =" "
last_name = "Kc"
gender= "Male"
occupation = "Student"
education = "Bsc Csit"
blood_group = "A+"
citizenship_no = '21-333432-33'
citizenship_district = "Rupandehi"
witness_first_name = "Devendra"
witness_middle_name = "Bahadur"
witness_last_name = "Kc"
witness_relationship = "Father"
pe_zone = "Lumbini"
pe_district = "Rupandehi"
pe_village = "Farena"
pe_ward_no = 1
pe_tole = "Thutipipal"
pr_zone = "Lumbini"
pr_district = "Rupandehi"

pr_village = "Padsari"
pr_ward_no = 1
pr_tole = "Lakhanchowk"
mobile = 9817458494

#creating explict wait
wait = WebDriverWait(driver, 10)

ele = driver.find_element(By.NAME, "dlOnlineReg.firstname")
ele.clear()
ele.send_keys(first_name)

ele = driver.find_element(By.NAME, "dlOnlineReg.middlename")
ele.clear()
ele.send_keys(middle_name)

ele = driver.find_element(By.NAME, "dlOnlineReg.lastname")
ele.clear()
ele.send_keys(last_name)


#for handling date of birth
driver.find_element(By.XPATH, "/html/body/div[4]/div/form/div[4]/table/tbody/tr[2]/td[4]/div[2]/div/div/img").click()
ele = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/select[2]")
actions = ActionChains(driver)
actions.double_click(ele).perform()
time.sleep(1)
ele = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/input")

ele.send_keys('2057') #enter years

ele = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/select[1]")
ele.click()
time.sleep(2)
ele = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/select[1]")
drp = Select(ele)
drp.select_by_visible_text("Baisakh") #enter month
time.sleep(3)

ele = driver.find_element(By.LINK_TEXT, "1") #enter day
time.sleep(1)
actions = ActionChains(driver)
time.sleep(1)
actions.move_to_element(ele).click().perform()
time.sleep(3)





element = driver.find_element_by_id("appEntry_dlOnlineReg_gender_id")
drp = Select(element)
drp.select_by_visible_text(gender)

ele = driver.find_element(By.NAME, "dlOnlineReg.occupation")
ele.clear()
ele.send_keys(occupation)

ele = driver.find_element(By.NAME, "dlOnlineReg.education")
ele.clear()
ele.send_keys(education)

ele = driver.find_element_by_id("appEntry_dlOnlineReg_bloodgroup_id")
drp = Select(ele)
drp.select_by_visible_text(blood_group)
time.sleep(2)

ele = driver.find_element(By.NAME, "dlOnlineReg.citizenshipnumber")
ele.clear()
ele.send_keys(citizenship_no)

ele = driver.find_element_by_id("appEntry_dlOnlineReg_districtByIssuedistrictid_id")
drp = Select(ele)
drp.select_by_visible_text(citizenship_district)

ele = driver.find_element(By.NAME, "dlOnlineReg.witnessFirstname")
ele.clear()
ele.send_keys(witness_first_name)

ele = driver.find_element(By.NAME, "dlOnlineReg.witnessMiddlename")
ele.clear()
ele.send_keys(witness_middle_name)

ele = driver.find_element(By.NAME, "dlOnlineReg.witnessLastname")
ele.clear()
ele.send_keys(witness_last_name)

ele = driver.find_element_by_id("appEntry_dlOnlineReg_relationtype_id")
drp = Select(ele)
drp.select_by_visible_text(witness_relationship)

ele = driver.find_element_by_id("permZone")
drp = Select(ele)
drp.select_by_visible_text(pe_zone)

ele = driver.find_element(By.NAME, "dlOnlineReg.districtByPermDistrict.id")
drp = Select(ele)
time.sleep(2)
drp.select_by_visible_text(pe_district)

ele = driver.find_element_by_id("permVillage")
drp = Select(ele)
time.sleep(2)
drp.select_by_visible_text(pe_village)

ele = driver.find_element(By.NAME, "dlOnlineReg.permWardnumber")
ele.clear()
ele.send_keys(pe_ward_no)

ele = driver.find_element(By.NAME, "dlOnlineReg.permTole")
ele.clear()
ele.send_keys(pe_tole)

ele = driver.find_element(By.NAME, "dlOnlineReg.permMobilemumber")
ele.clear()
ele.send_keys(mobile)



ele = driver.find_element_by_id("presZone")
drp = Select(ele)
drp.select_by_visible_text(pr_zone)

ele = driver.find_element(By.NAME, "dlOnlineReg.districtByDistrictId.id")
drp = Select(ele)
time.sleep(2)
drp.select_by_visible_text(pr_district)

ele = driver.find_element(By.NAME, "dlOnlineReg.villagemetrocityByVillagemetrocityId.id")
drp = Select(ele)
time.sleep(2)
drp.select_by_visible_text(pr_village)

ele = driver.find_element(By.NAME, "dlOnlineReg.wardnumber")
ele.clear()
ele.send_keys(pr_ward_no)

ele = driver.find_element(By.NAME, "dlOnlineReg.tole")
ele.clear()
ele.send_keys(pr_tole)

ele = driver.find_element(By.ID, "appEntry_dlOnlineReg_mobilenumber")
ele.clear()
ele.send_keys(mobile)


ele = driver.find_element(By.ID, "cate"+choice)
ele.click()
time.sleep(3)

Select(driver.find_element(By.NAME, "dlOnlineReg.zoneByAppliedZoneoffice.id")).select_by_visible_text("Lumbini")
Select(driver.find_element(By.NAME, "dlOnlineReg.licenseissueoffice.id")).select_by_visible_text("Lumbini,Nepal")
time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(1)


captche = driver.find_element(By.XPATH, '//*[@id="appEntry_jcaptcha"]')
#actions = ActionChains(driver)
#actions.move_to_element(captche).perform()
#driver.execute_script("argument[0].scrollIntoView();", captche)

captche.send_keys("")


def take_ss():
    ele = driver.find_element(By.XPATH, '//*[@id="captcha_image"]')

    size = ele.size
    location = ele.location
    time.sleep(3)
    png = driver.get_screenshot_as_png()


    im = Image.open(BytesIO(png))

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    return [left, top, right, bottom]



time.sleep(2)



print(take_ss())

'''images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))


text = pytesseract.image_to_string(Image.open("filename.png"))
time.sleep(2)
captche.send_keys(text)'''