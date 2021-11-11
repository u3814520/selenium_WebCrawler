from selenium import webdriver
import time
card_number= "<卡號>"
birthday="<生日>"

class card:
    def __init__(self):
        self.driver=webdriver.Chrome()
    def run(self):
        self.go_to_website()
        self.enter_car_num()
        self.select_date()
        self.wait_robot()
        self.enter_button()
        self.get_data()
    def go_to_website(self):
        self.driver.get('https://ezweb.easycard.com.tw/search/CardSearch.php')
    def enter_car_num(self):
        card_num_input=self.driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[2]/div/ul/li[1]/input")
        card_num_input.send_keys(card_number)
        card_day_input=self.driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[2]/div/ul/li[2]/input")
        card_day_input.send_keys(birthday)
    def select_date(self):
        self.driver.find_element_by_id("date3m").click()
    def wait_robot(self): # 等待機器人測試
        input("wait robot")
    def enter_button(self):
        self.driver.find_element_by_id("btnSearch").click()
    def get_data(self):
        culcome
        time.sleep(5)
        rows=self.driver.find_elements_by_class_name("r1")

        for row in rows:
            print(row.text)


if __name__ =="__main__":
    c=card()
    c.run()