# CSV Web Application
A Full Stack Web Application that handle CSV data

## Technology
### Front End
- React - Front End View Framework.
- React Virtualized - Front End library to render large lists and tabular data.
- Axios - Front End Interface With a Backend REST API.
- BootStrap - Styling Pages.

### Back End
- Flask-Restful - Object Oriented Programming(OOP) Backend REST API.
- Flask-SQLAlchemy - Object-Relational Mappers(ORM), high-level abstraction that transfer database data into objects.
- SQLite or PostgreSQL - Setup to work with the Relational Database SQLite or PostgreSQL.  


# Requirements
The application have the ability to:
- [x] Upload a CSV file 
- [x] List uploaded CSV files  
- [x] Download the previously uploaded CSV file 
- [x] Display the CSV content showing at least all column headers and content
- [ ] Provide statistics on the number of people with the same year in the “date” field.



# Testing
To run the testing script, run the command below in the terminal. 
``` sh
$ cd src
$ chmod 777 ./test/test.sh
$ ./test/test.sh
```
The ./test.sh will run the `test_suite.py` which contains unit, integration and system tests. The results of these tests are reported in the Terminal.

# Code Coverage Testing
You can test to see how much of the orchestration code is run via `test_suite.py` by generating a coverage report.
First, install coverage in Terminal using
``` sh
$ pip install coverage
```
Next, run the following commands:
``` sh
$ coverage run test/test_suite.py
$ coverage report
$ coverage html
```
`coverage run test/test_suite.py` will run all tests with `coverage`.

`coverage report` will print a coverage report in Terminal.

`coverage html` will create an interactive html file that you can open in a web browser. This html file is stored
in the path `src/htmlcov/index.html`. Find this in your file explorer and double-click it to open it in your 
default browser. You can use this file to see exactly which lines of code have been run, and which have not.