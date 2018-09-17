from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#this can hopefully help gather the info from merriam-webster website
#made by Queue Huo Sep.17 2018
#CODE STYLE EVEN MORE TERRIBLE( See "code style really bad' from Alan?Liang)

fileRead = open("Wordlist.txt","r")
fileWrite = open("Wordlist-meaningGathered.txt","w")
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_opt)
mainDriver = webdriver.Chrome()

currentWordCounter = 0
keywords = fileRead.readlines()
fileWrite.writelines(keywords)
fileWrite.flush()
for keyword in keywords:
    print("#DEBUG:" + keyword + "\n")
    #fileWrite.write("\n")
    mainDriver.get("https://www.merriam-webster.com/words-at-play/new-words-in-the-dictionary-september-2018")
    inputbar = mainDriver.find_element_by_id("s-term")
    inputbar.send_keys(keyword,Keys.RETURN)
    results = mainDriver.find_elements_by_class_name("sense")
    currentWordCounter += 1
    fileWrite.write(str(currentWordCounter))
    fileWrite.write(" " + keyword)
    fileWrite.write(" : ")
    for result in results:
            fileWrite.write(result.text)
            print(result.text + '\n')
            fileWrite.flush()
    #print(keyword)
fileRead.close()
fileWrite.close()

