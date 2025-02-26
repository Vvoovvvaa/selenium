import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def write_into_file(fname, data):
    with open(fname, "a", encoding="utf-8") as f:
        f.write(data + "\n")

options = webdriver.ChromeOptions()
options.add_argument("--incognito")    
options.add_argument("--window-size=800,800")  
options.add_argument("--disable-gpu")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
url = "https://www.youtube.com/"
driver.get(url)

search = driver.find_element(By.NAME, "search_query")
search.send_keys("Armenchik")
search.send_keys(Keys.RETURN)

time.sleep(3)  

videos = driver.find_elements(By.XPATH, "//ytd-video-renderer")[:10]

def logika():
    for video in videos:
        try:
            title = video.find_element(By.XPATH, ".//h3/a").text
            metadata = video.find_elements(By.XPATH, ".//div//span[@class='inline-metadata-item style-scope ytd-video-meta-block']")
            if len(metadata) > 0:
                views = metadata[0].text
                if len(metadata) > 1: 
                    data_video = metadata[1].text 
                else:
                    print("No information")
            else:
                print("No information")    

            output = f"{title}, {views}, {data_video}"
            write_into_file("find_results.txt", output)

        except Exception as e:
            print(f"Ошибка: {e}")

time.sleep(7)  
if __name__=="__main__":
    logika()