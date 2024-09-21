from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
def func(SEHIR="",ILCE="",BITKI="",SAFHA=""):
    SEHIR.capitalize()
    ILCE.capitalize()
    BITKI.upper()
    SAFHA.upper()

    # WebDriver kurulumu
    driver = webdriver.Chrome()
    driver.get("https://zdus.mgm.gov.tr/")

    for i in range(4):
        driver.implicitly_wait(10)
        dropdown_elements = driver.find_elements(By.CLASS_NAME, "css-qc6sy-singleValue")
        actions = ActionChains(driver)
        actions.move_to_element(dropdown_elements[i]).click().perform()
        if i == 0:
            actions.send_keys(SEHIR).perform()  
        elif i == 1:
            actions.send_keys(ILCE).perform() 
        elif i == 2:
            actions.send_keys(BITKI).perform()
        # elif i == 3:
        #     actions.send_keys(SAFHA).perform()
        actions.send_keys("\n").perform()

    driver.implicitly_wait(10)
    sorgula = driver.find_element(By.CLASS_NAME, "queryBtn")
    sorgula.click()


    driver.implicitly_wait(10)
    temp_box_div = driver.find_element(By.CLASS_NAME, "tempBoxs")
    span_elements = temp_box_div.find_elements(By.TAG_NAME, "span")
    span_data = []

    for span in span_elements:
        span_class = span.get_attribute("class")
        span_text = span.text
        span_data.append({"class": span_class[14:], "text": span_text})

    # Listeyi ekrana yazdır
    return span_data
    # for data in span_data:
    #     print(f"Class: {data['class']}, Text: {data['text']}")
if __name__ =="__main__":
    func("İzmir","Karşıyaka","Mısır","")
# def deneme(metin: str):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--incognito")
#     # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     driver = webdriver.Chrome(options=chrome_options)
    
#     try:
#         driver.get("https://www.mgm.gov.tr/tarim/zdus.aspx")
#         driver.implicitly_wait(10)

#         iframe=driver.find_element(By.XPATH, '//*[@id="pages"]/div/iframe')
#         driver.switch_to.frame(iframe)
#         driver.implicitly_wait(10)

#         search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div[1]/div/div/div[1]/div[1]')
#         # print(f"search box ======{search_box.text}============")
#         search_box.send_keys(metin)
#         driver.execute_script("arguments[0].value = arguments[1];", search_box.text, metin)
#         search_box.send_keys(Keys.RETURN)
#         driver.switch_to.default_content()
#         time.sleep(3) 
        
#         # sarki = driver.find_element(By.CSS_SELECTOR, '[class*="mini_card-title"]').text
#         # yazar = driver.find_element(By.CSS_SELECTOR, '[class*="mini_card-subtitle"]').text
        
#         # return sarki, yazar
#     except Exception as e:
#         print(f"Hata: {e}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     sarki = deneme("İzmir")
#     print(f"Şehir: {sarki}")

# from bs4 import BeautifulSoup
# import requests
# url = "https://www.mgm.gov.tr/tarim/zirai-don-uyari-sistemi-harita.aspx?s=takvim#aciklama2"
# page = requests.get(url)
# soup = BeautifulSoup(page.text,"html",features="html.parser")
# #print(soup)
# #<a href="../FILES/ziraat/TrDonHaritasi/don/ilkbahar en gec don tarihleri (0°C).png" target="_blank">
# #İlkbahar en gec don tarihleri (0°C)</a>
# # soup.find("li")
# # soup.find_all("li")[1]
# li = soup.find_all("li")[1]
# soup.find("table", class_ = "jpg")
# print(li)
# # from time import strftime

# # #meteorolojiden gelen veriler
# # mtrljsicak = 23
# # mtrljnem = 50
# # mtrljhava = "bulutlu"
# # randrakim = 0
# # def Dclock():
# #     string = strftime("%H :%M :%S :%p")


# # def ortalama():

# #     # sicak = int(input("Sıcaklık girin: "))
# #     # nem = int(input("Nem girin: "))
# #     # hava = input("Hava nasıl: ")
# #     # rakim = int(input("Rakım kaç: "))
# #     # vakit = int(input("vakit????? "))
# #     sicak = mtrljsicak
# #     nem = mtrljnem
# #     hava = mtrljhava
# #     rakim = randrakim
# #     vakit = Dclock()

# #     # sicak70 = (sicak * 70)/100
# #     # nem30 = (nem * 30)/100
# #     # hava40 = (hava * 40)/100
# #     # rakim25 = (rakim * 25)/100
# #     # vakit20 = (vakit * 20)/100 
# #     print("hava",sicak,"derece")
# #     print("hava",hava)
# #     print("nem oranı % ",nem)
# #     print("rakımınız",rakim,"metre")
# #     print("saat",vakit)



# # ortalama()