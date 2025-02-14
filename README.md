# 00 Data parsing server - Part II

**Type**: Individual

This is a continuation of the assignment: Data Parsing.

In the previous assignment you created scripts that can parse files. In this assignment you should expose the data from a server.

Create a single server. Using one of the langauges from the data parsing assignment would make sense. 
Remember, at this level it is your job to make decision such as language, libraries and frameworks. 

Create endpoints for each data parsing task that serves the data. 

There should be an endpoint for each: XML, CSV YAML, TXT and JSON. 

<img src="./Data_parsing_server_Part_II.png">


I decided to make a data parsing server A in Python and the data parsing server B in JavaScript. 
Remember to start start both servers to be able to communicate with them both.


# Python
https://github.com/Marcus-K-Thorsen/02a._Data_parsing_server_part_2/blob/main/py_server_a/README.md

**Base Python URL**: localhost:8000


# Endpoints to get the data from Server A (Python_Server)

* **/csv/py**
* **/json/py**
* **/txt/py**
* **/xml/py**
* **/yaml/py**


# Endpoints to get data through Server B (JavaScript_Server)

* **/csv/js**
* **/json/js**
* **/txt/js**
* **/xml/js**
* **/yaml/js**

# JavaScript
https://github.com/Marcus-K-Thorsen/02a._Data_parsing_server_part_2/blob/main/js_server_b/README.md

