from helper.action import Action
from selenium.webdriver.common.by import By

class JobPage:

    job_link = "/quality-assurance/"
    job_page_title = "Insider quality assurance job opportunities"
    location_text = "Istanbul, Turkey"
    department_text = "Quality Assurance"
    see_all_qa_jobs_button = (By.XPATH,"//a[contains(text(),'See all QA jobs')]")
    location_filter = (By.CSS_SELECTOR, "select[id='filter-by-location']")
    department_filter = (By.CSS_SELECTOR, "select#filter-by-department")
    location_bar = (By.XPATH,"//span[contains(text(),'All')]")
    selected_location = (By.XPATH,"//span[contains(text(),'"+location_text+"')]")
    selected_department = (By.XPATH,"//span[contains(text(),'"+department_text+"')]")
    jobs_item = (By.XPATH, "//div[contains(@class,'position-list-item-wrapper')]")
    first_job_item = (By.XPATH, "(//div[contains(@class,'position-list-item-wrapper')])[1]")
    jobs_location = (By.XPATH, "//div[contains(@class,'position-location')]")
    jobs_department = (By.XPATH, "//span[contains(@class,'position-department')]")
    first_job_view_role_button = (By.XPATH,"(//div[contains(@class,'position-list-item-wrapper')]/a[contains(text(),'View Role')])[1]")
    apply_button = (By.XPATH,"(//a[contains(text(),'Apply for this job')])[1]")
    all_select = (By.XPATH,"//span[contains(text(),'All')]")
    location_selectedd = (By.XPATH,"//li[contains(text(),'Istanbul, Turkey')]")

    def __init__(self, browser,config):
        self.action = Action(browser)
        self.url = config['base_url'] + self.job_link

    def go_to_job_page(self):
        self.action.go_to_page(self.url)

    def check_job_page_open(self):
        self.action.check_element_is_visible(self.selected_department)
        self.action.check_title(self.job_page_title)

    def click_see_all_qa_jobs_button(self):
        self.action.click_element(self.see_all_qa_jobs_button)

    def select_location(self):
        self.action.check_element_is_visible(self.selected_department)
        self.action.click_element(self.all_select)
        self.action.click_element(self.location_selectedd)
        self.action.check_element_is_visible(self.selected_location)

    def select_department(self):
        self.action.select_from_list(self.department_filter,self.department_text)
        self.action.check_element_is_visible(self.selected_department)
        self.action.hard_wait(1)

    def check_jobs_list_present(self):
        self.action.scroll_to_element(self.first_job_item)
        self.action.hard_wait(1)
        self.action.check_element_number_more_than(self.jobs_item,0)

    def check_jobs_location(self):
        self.action.check_elements_text_contains(self.jobs_location,self.location_text)

    def check_jobs_department(self):
        self.action.check_elements_text_contains(self.jobs_department,self.department_text)

    def click_first_view_role_button(self):
        self.action.hover_over_element(self.first_job_item)
        self.action.hard_wait(3)
        self.action.click_element(self.first_job_view_role_button)
        self.action.switch_to_auto_opened_window()
        self.action.check_title_not_equal(self.job_page_title)
        self.action.check_element_is_visible(self.apply_button)



    
