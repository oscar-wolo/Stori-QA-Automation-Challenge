from selenium import webdriver

class Browser:

  def __init__(self, browserName):
    self.browserName = browserName
    if(browserName == 'chrome'):
      self.driver = webdriver.Chrome('./drivers/chromedriver.exe')
    elif(browserName == 'firefox'):
      self.driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe')
    else:
      print(browserName + " is not recognized!")


  def get_driver(self):
    return self.driver

  def __str__(self):
    return self.browserName;