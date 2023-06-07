from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import speedtest

PROMISED_DOWN = "YOUR INTERNET DOWNLOAD EXPECTED"
PROMISED_UP = "YOUR INTERNET UPLOAD EXPECTED"
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"
TWITTER_USERNAME = "YOU TWITTER USERNAME"
MY_OPERATOR = "YOUR INTERNET OPERATOR"
service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.st = speedtest.Speedtest()

    def get_speed(self):
        print("Fetching speeds...")
        dwnld = round(self.st.download() / 1000000, 2)
        upld = round(self.st.upload() / 1000000, 2)
        return [dwnld, upld]

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        self.driver.implicitly_wait(2)

        #Completing email field
        self.user = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        self.user.send_keys(TWITTER_EMAIL)
        self.user.send_keys(Keys.TAB)
        self.user.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(2)

        #Completing username field
        self.username = self.driver.find_element(By.XPATH, '//input[@autocomplete="on"]')
        self.username.send_keys(TWITTER_USERNAME)
        self.username.send_keys(Keys.TAB)
        self.username.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(2)

        #Completing password field
        self.passw=self.driver.find_element(By.NAME,'password')
        self.passw.send_keys(TWITTER_PASSWORD)
        self.passw.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)
        self.driver.implicitly_wait(2)

        #Twetting to the provider
        self.tweet=self.driver.find_element(By.XPATH,"//div[@class = 'public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        self.tweet.send_keys(f'Hey{MY_OPERATOR}.My down speed is {self.down} and up is {self.up} instead of {PROMISED_DOWN}down & {PROMISED_UP}up')
        self.button=self.driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]').click()
        self.driver.implicitly_wait(2)
        self.driver.quit()
        







