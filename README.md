# E-Commerce Altron<br>-----------------------
# Introduction 
This is an Automation Framework to test an E-Commerce Web Portal( Back-End ).

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:

1.	Installation process:
		Intsall Pycharm and then go to settings , then Python interpreter and add pytest , selenium , pytest-html ,allure-pytest,
		allure-pytest-commons,html-test-reports,openxyl,pytest xdist,pytest-metadata
2.	Software dependencies
			- Python and Pytest
			- Pycharm

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

- Run the command in terminal to run specific test 
  python -m pytest -v -s testCases/test_login.py --browser chrome 
- testCeses/test_login.py is the path of the file you want to run
- " --browser chrome " is the browser you want to run tests on
- The test can run on Firefox , Chrome and Edge.

# Run TESTS IS PARALLEL
TODO: to run test in parallel execute the following command
- python -m -n=3 pytest -v -s testCases/test_login.py --browser chrome
- -n=2 means 2 test will run in parallel.

# Generate HTML Report
TODO: Run The following Command
- python -m pytest -v -s -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome
- This is generate the html report in desire folder.

# Run DATA DRIVEN TEST CASE
TODO: Execute the following command to execute data driven test case
-  python -m pytest -v -s testCases/test_login_data-driven.py --browser chrome 
