from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=s)
driver.get('http://idojarasbudapest.hu/archivalt-idojaras')

f = open("weather_data.csv", "a")

for i in range(1, 11):
    for j in range(12):
        ev = Select(driver.find_element(By.ID, 'ev'))
        ho = Select(driver.find_element(By.ID, 'ho'))
        button = driver.find_element(By.ID, "button")
        ev.select_by_index(i)
        ho.select_by_index(j)
        button.click()

        table_id = driver.find_element(By.XPATH, "/html/body/div[@class='tartalom'][2]/table")
        rows = table_id.find_elements(By.TAG_NAME, "tr")

        for k in range(1, len(rows)):
            cols = rows[k].find_elements(By.TAG_NAME, "td")
            nap = cols[0].text.split('\n')[0]
            f.write(f"{nap}\t{cols[1].text}\t{cols[2].text}\n")

f.close()

driver.quit()
