from helper.action import Action
from selenium.webdriver.common.by import By

class MainPage:

    main_page_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    company_menu_button = (By.XPATH, "//a[contains(text(),'Company')]")
    dropdown_menu = (By.XPATH, "//li[@class='nav-item dropdown show']")
    careers_menu_button = (By.XPATH, "//a[@class='dropdown-sub' and contains(text(),'Careers')]")
    accept_all_cookie = (By.LINK_TEXT, "Accept All")

    def __init__(self, browser,config):
        self.action = Action(browser)
        self.url = config['base_url']

    def go_to_home_page(self):
        self.action.go_to_page(self.url)

    def check_main_page_is_opened(self):
        self.action.check_title(self.main_page_title)

    def click_company_button(self):
        self.action.click_element(self.accept_all_cookie)
        self.action.hard_wait(2)
        self.action.click_element(self.company_menu_button)

    def check_drop_down_menu_is_opened(self):
        self.action.check_element_is_visible(self.dropdown_menu)

    def click_careers_menu_button(self):
        self.action.click_element(self.careers_menu_button)
