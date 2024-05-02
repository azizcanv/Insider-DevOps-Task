import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Action:

    max_wait = 20
   
    def __init__(self, browser) -> None:
        self.browser = browser
        self.wait = WebDriverWait(self.browser, self.max_wait)

    def go_to_page(self,url):
        self.browser.get(url)

    def find_element(self, by):
        try:
            element = self.wait.until(EC.presence_of_element_located(by))
            return element 
        except Exception as e:
            raise Exception("No element is present")
    
    def find_elements(self, by):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(by))
            return elements
        except Exception as e:
            raise Exception("No elements are present")

    def wait_clickable(self, by):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by))
            return element
        except Exception as e:
            raise Exception(f"Element is not clickable")

    def check_element_is_visible(self, by):
        element = self.find_element(by)
        assert element.is_displayed()

    def check_title(self, title):
        current_title = self.browser.title
        assert title == current_title

    def click_element(self, by):
        element = self.find_element(by)
        element.click()

    def scroll_to_element(self, by):
        element = self.find_element(by)
        script = "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});"
        self.browser.execute_script(script, element)

    def hard_wait(self,sec):
        time.sleep(sec)

    def check_element_number_more_than(self, by, number):
        elements = self.find_elements(by) 
        assert len(elements) > number, f"Expected more than {number} elements, but found {len(elements)} elements."

    def select_from_list(self, by, text):
        element = self.find_element(by)
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

    def check_elements_text_contains(self, by, expected_text):
        elements = self.find_elements(by) 
        misscontained_elements = [element for element in elements if expected_text not in element.text]
        assert not misscontained_elements, f"Element text does not contain expected text '{expected_text}' for the following elements: {', '.join(element.text for element in misscontained_elements)}"

    def hover_over_element(self, by):
        element = self.find_element(by) 
        action = ActionChains(self.browser)
        action.move_to_element(element).perform()

    def switch_to_auto_opened_window(self):
        main_window = self.browser.window_handles[0]
        self.wait.until(lambda x: len(x.window_handles) == 2)
        new_window = [window for window in self.browser.window_handles if window != main_window][0]
        self.browser.switch_to.window(new_window)

    def check_title_not_equal(self, title):
        current_title = self.browser.title
        assert title != current_title