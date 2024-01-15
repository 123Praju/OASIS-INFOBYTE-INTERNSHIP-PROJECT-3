
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class youtube_vid:
    def __init__(self):
        # Install ChromeDriver
        ChromeDriverManager().install()

        # Create Chrome options
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(options=options, service=Service())

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        video=self.driver.find_element('xpath', '//*[@id="video-title"]/yt-formatted-string')
        video.click()

