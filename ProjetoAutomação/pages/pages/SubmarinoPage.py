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
    
    