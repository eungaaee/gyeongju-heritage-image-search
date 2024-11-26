from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

if not os.path.exists("training_images"):
    os.makedirs("training_images")

heritages = ["경주남산일원", "경주남산미륵곡석조여래좌상", "경주남산용장사곡삼층석탑", "경주남산용장사곡석조여래좌상", "경주남산용장사지마애여래좌상", "경주남산천룡사지삼층석탑", "경주남산사지당간지주", "남간사지석정", "경주남산동동서삼층석탑", "경주배동석조여래삼존입상", "경주남산불곡마애여래좌상", "경주남산신선암마애보살반가상", "경주남산칠불암마애석불", "경주남산탑곡마애조상군", "경주남산삼릉계석조여래좌상", "삼릉계곡마애관음보살상", "삼릉계곡선각육존불", "경주남산입곡석불두", "경주침식곡석불좌상", "경주열암곡석불좌상", "경주약수계곡마애입불상", "삼릉계곡마애석가여래좌상", "삼릉계걱선각여래좌상", "경주배리윤을곡마애불좌상", "경주첨성대", "경주분황사모전석탑"]

for name in heritages:
    if not os.path.exists(f"training_images/{name}"):
        os.makedirs(f"training_images/{name}")

interval = 1

opt = webdriver.EdgeOptions()
# opt.add_argument("headless")
opt.add_experimental_option("detach", True)

driver = webdriver.Edge(options=opt)

for name in heritages[-2:]:
    driver.get(f"https://www.google.com/search?sca_esv=c6b59d112dad26b9&q={name}&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ96qP8jk59Ek0sz1u1YABeO8HG8dr9Z0pIiXpKYIhEwOJ2k8lQbNlrF2IBe5Y93_wn8pG_PEsMWwa_WmaMASzob4DYwPWA8njTkq3v27FhvFu_b6hyq9oa1yNQJcgWZrzcjHeQrg1Pz9V32WGoewbvPANMBJ11FcLNrUuoz3OzHZuXlKNVA&sa=X&ved=2ahUKEwjXwuS-77mJAxWnjK8BHazyHpQQtKgLegQIFBAB&biw=1220&bih=670&dpr=2")
    time.sleep(2)

    firstImage = driver.find_element(By.CSS_SELECTOR, "#rso > div > div > div.wH6SXe.u32vCb > div > div > div:nth-child(1) > div.czzyk.XOEbc > h3 > a")
    firstImage.click()

    for i in range(100):
        try:
            time.sleep(interval)
            
            img = driver.find_element(By.CSS_SELECTOR, "#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.FyHeAf.iPVvYb")
            src = img.get_attribute("src")

            urllib.request.urlretrieve(src, f"./training_images/{name}/{i+1}.png")
        except Exception as e:
            print(f"{i+1}번째 이미지 다운로드 실패: {e}")
        finally:
            nextButton = driver.find_element(By.CSS_SELECTOR, "#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.XQEEtd.VTMWGb > div > div.HJRshd > button:nth-child(2)")
            nextButton.click()

driver.quit()