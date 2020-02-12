class PageUtils:
    
    def __init__(self, driver):
        self.driver = driver

    def sendText(self, element, text):
        campo = self.driver.find_element_by_cssSelector(element)
        campo.sendKeys(text);
    
   
        