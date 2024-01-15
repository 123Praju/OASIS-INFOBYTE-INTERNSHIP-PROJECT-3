from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class InfoW:
    def __init__(self,speak):
        # Install ChromeDriver
        ChromeDriverManager().install()

        # Create Chrome options
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(options=options, service=Service())

        self.speak = speak
  

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")

        # Wait for the search input field to be present
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]'))
        )
        search_input.click()
        search_input.send_keys(query)

        # Wait for the 'Search' button to be clickable
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/fieldset/button'))
        )
        search_button.click()

        # Wait for the page content to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]'))
        )

        # Get the first paragraph element
        first_paragraph_element = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p')

        # Get the text of the first paragraph
        first_paragraph_text = first_paragraph_element.text

        # Speak the first paragraph
        self.speak("Here is some information about {}: {}".format(query, first_paragraph_text))