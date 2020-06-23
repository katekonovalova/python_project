from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(
            executable_path="geckodriver"
        )
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()
