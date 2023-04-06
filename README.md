# python-selenium-framework

This Selenium framework is created using python as a language and pytest as a unit testing framework.

## Follow below Steps to create a similar project
Step 1 : Create a new project and install required packages/plugins.

  * Selenium : Selenium libraries 
  * WebDriverManager : Browser extensions 
  * Pytest : Unit Test Framework 
  * pytest-html : HTML Reports 
  * pytest-xdist : Run Tests in Parallel 
  * Allure-pytest : to generate allure- reports

Step 2 : Create a folder structure

  * Project Name  
  * pageObject(package)
  * components(package)
  * tests(package)
  * services(package) - will contain all the utilities files 
  * logs(folder)
  * screenshots(folder)
  * reports(folder)


## To run the test cases ,type below command on terminal
````
py.test -v -s --html=reports\report.html --browser_name chrome
