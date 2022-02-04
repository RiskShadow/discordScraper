import logic as l
import time as t
from selenium.webdriver.common.keys import Keys
def scrape(chat, message):
    url = 'https://discord.com/login'
    email = input('Email: ')
    pwd = input('Password: ')
    username = '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input'
    password = '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input'
    loginB = '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]'
    nsfwcheck = '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div[4]/button[2]'
    baseUrl = 'https://cdn.discordapp.com/attachments/'

    driver = l.createDriver()
    driver.set_window_position(0, 0)  # Centers the browser
    driver.set_window_size(1200, 1200)  # Forces browser to open at proper size
    driver.get(url)

    driver.find_element_by_xpath(username).send_keys(email)
    driver.find_element_by_xpath(password).send_keys(pwd)

    driver.find_element_by_xpath(loginB).click()
    t.sleep(5)
    driver.get(chat)
    t.sleep(5)
    driver.find_element_by_xpath(nsfwcheck).click()
    t.sleep(5)

    driver.find_element_by_id(message).click()
    i = 0
    icp = 0
    ird = 0
    while True:
        driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_UP)
        i = i + 1
        if i == 50:
            links = []
            pageSource = driver.page_source
            for item in pageSource.split('"'):
                if len(item) >= 39:
                    if item[0:39] == baseUrl:
                        links.append(item)
            f = open('url.txt', 'a')
            for link in links:
                f.write(link + '\n')
            f.close()
            icp = icp + 1
            ird = ird + 1
            i = 0
            print("Backups: " + str(icp))
        if ird == 100:
            raw = open('url.txt', 'r').read().split('\n')
            res = []
            [res.append(x) for x in raw if x not in res]
            f = open('url.txt', 'w')
            f.write('\n'.join(res))
            print('Dupes Removed')
            ird = 0