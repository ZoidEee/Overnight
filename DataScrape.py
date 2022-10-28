from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep
import xlsx


class DataScrape:
    def __int__(self):
        pass

    def network(self, netw, driver):
        netBtnImg = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div/header/div/div[1]/div[3]/div[1]/div/div/div/div/div[2]')
        netBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/header/div/div[1]/div[3]/div[1]/div/div/div/i')

        optimismSValue = 'background-image: url("https://app.overnight.fi/img/op.9e269110.svg"); background-position: center center;'
        polygonSValue = 'background-image: url("https://app.overnight.fi/img/polygon.06292905.svg"); background-position: center center;'
        binanceSValue = 'background-image: url("https://app.overnight.fi/img/bsc.e3e2e95f.svg"); background-position: center center;'
        avalancheSValue = 'background-image: url("https://app.overnight.fi/img/avalanche.66754a5f.svg"); background-position: center center;'
        ethereumSValue = 'background-image: url("https://app.overnight.fi/img/ETH.3d2ae028.svg"); background-position: center center;'

        net = [
            'OPT', 'MATIC', 'BNB', 'AVA', 'ETH'
        ]

        '''
        
        The below if ---> elif statements check the network that is being displayed
        on the website.
        
        '''
        if netw == net[0]:
            if netBtnImg.get_attribute(optimismSValue):
                pass
            else:
                netBtn.click()
                optNetBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]')
                sleep(0.5)
                optNetBtn.click()
        elif netw == net[1]:
            if netBtnImg.get_attribute(polygonSValue):
                pass
            else:
                netBtn.click()
                polNetBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]')
                sleep(0.5)
                polNetBtn.click()
        elif netw == net[2]:
            if netBtnImg.get_attribute(binanceSValue):
                pass
            else:
                netBtn.click()
                binNetBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]')
                sleep(0.5)
                binNetBtn.click()
        elif netw == net[3]:
            if netBtnImg.get_attribute(avalancheSValue):
                pass
            else:
                netBtn.click()
                avaNetBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[4]')
                sleep(0.5)
                avaNetBtn.click()
        elif netw == net[4]:
            if netBtnImg.get_attribute(ethereumSValue):
                pass
            else:
                netBtn.click()
                ethNetBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[5]')
                sleep(0.5)
                ethNetBtn.click()
        elif netw != any(net):
            print(f'-----ERROR----- Please try again. Network {netw} not available.')

    def get_data(self, driver, filename):
        dates = []
        time = []
        amount = []
        apy = []

        table_id = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div/main/div/div/div/div[3]/div/div[2]/div[1]/div[1]/div/table/tbody')
        rows = table_id.find_elements(By.TAG_NAME, "tr")

        for row in rows:

            dates.append(row.text[:10])
            time.append(row.text[11:16])
            amount.append(row.text[17:27].replace(" ", ""))

            if '\n' in row.text[28:33]:
                apy.append(row.text[28:33].replace('\n', '  ').strip())

            else:
                apy.append(row.text[28:33])

        del apy[-1]
        apy.append('0%')
        dates = list(reversed(dates))
        time = list(reversed(time))
        amount = list(reversed(amount))
        apy = list(reversed(apy))

        xlsx.xlsxWriter(dates, time, amount, apy, filename)

        # print(dates)
        # print(time)
        # print(amount)
        # print(apy)


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path='/snap/bin/chromium.chromedriver')
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(15)
driver.get("https://app.overnight.fi/stats")

run = DataScrape()
run.network('MATIC', driver)
run.get_data(driver, 'Matic')
