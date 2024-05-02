from helper.action import Action
from selenium.webdriver.common.by import By

class CareersPage:

    careers_page_title = "Ready to disrupt? | Insider Careers"
    find_your_calling_section = (By.XPATH, "//section[@id='career-find-our-calling']")
    see_all_teams_button = (By.XPATH, "//section[@id='career-find-our-calling']//a[contains(text(),'See all teams')]")
    team_members = (By.XPATH,"//div[contains(@class,'job-item')]")
    our_locations_section = (By.XPATH, "//section[@id='career-our-location']")
    life_at_insider_section = (By.XPATH, "//h2[normalize-space()='Life at Insider']")
    qa_job = (By.XPATH,"//div[contains(@class,'job-title')]/a[contains(@href,'quality-assurance')]")
    
    def __init__(self, browser):
        self.action = Action(browser)

    def check_careers_page_is_opened(self):
        self.action.check_title(self.careers_page_title)

    def check_find_your_calling_section_is_present(self):
        self.action.scroll_to_element(self.find_your_calling_section)
        self.action.check_element_is_visible(self.find_your_calling_section)

    def click_see_all_teams_button(self):
        self.action.scroll_to_element(self.see_all_teams_button)
        self.action.hard_wait(1)
        self.action.click_element(self.see_all_teams_button)
        self.action.hard_wait(1)

    def check_see_all_teams_opened(self):
        self.action.check_element_number_more_than(self.team_members,3)

    def check_our_locations_block_is_present(self):
        self.action.scroll_to_element(self.our_locations_section)
        self.action.hard_wait(1)
        self.action.check_element_is_visible(self.our_locations_section)

    def check_life_at_insider_section_is_present(self):
        self.action.scroll_to_element(self.life_at_insider_section)
        self.action.hard_wait(1)
        self.action.check_element_is_visible(self.life_at_insider_section)
    
    def click_qa_job(self):
        self.action.scroll_to_element(self.qa_job)
        self.action.hard_wait(1)
        self.action.click_element(self.qa_job)
        self.action.hard_wait(1)
