#Dependencias Selenium
from selenium import webdriver
#Pages importadas
from pages.pages.SubmarinoPage import Submarino
from Pyautomators import fixture
from Pyautomators.contrib.scenario_autoretry import scenario_retry

def before_all(context):
    context.driver=webdriver.Chrome('driver/chromedriver.exe')
    context.subP=Submarino(context.driver)	
    
def after_all(context):
	#context.driver.quit();
    pass

