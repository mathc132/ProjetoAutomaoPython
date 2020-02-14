import json

class Submarino():

    def __init__(self, driver):
        self.driver = driver
        self.URL="https://www.submarino.com.br/";
    
    
    def acessarSite(self):
        self.driver.get(self.URL);

    
    def sendText(self, element, text):
        campo = self.driver.find_element_by_id(element)
        campo.send_keys(text)
                      
    def clickButton(self, element):
        bt = self.driver.find_element_by_css_selector(element)
        bt.click()
    
    def lerPage(self):
        with open('ProjetoAutomação\data\massa.json', 'r') as json_file:
            data = json.load(json_file)
            return data['produto'] 
    
    def clickItem(self, number):
        css = "#content-middle > div:nth-child(6) > div > div > div > div.row.product-grid.no-gutters.main-grid"
        tableList = self.driver.find_element_by_css_selector(css)
        linkList = tableList.find_elements_by_tag_name("a")
        for a in linkList:
            print(a)