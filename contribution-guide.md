##Contribution Guide

**Implemetation Language**: Python 2.x

###3rd Party Libraries Used

These are the libraries that you'll need to work with while contributing to Code Analyser

- lizard
- watchdog
- pyYAML
- argh
- pathtools
- plyj
- slimit


####Lizard
A code analyzer which without caring about the dependencies gives the metrics. It works with Java, C/C++, JavaScript, Python. Metrics includes cyclomatic complexity number, token count of functions, parameter count of functions etc.


####Watchdog

Python API library and shell utilities to monitor file system events.
It is used to detect any changes made on the server.

####pyYAML

YAML is a data serialization format designed for human readability and interaction with scripting languages. PyYAML is a YAML parser and emitter for Python.

####Pathtools

Python API library for common path and pattern functionality.

####Plyj

Plyj is a Java parser written in Python using PLY. It is used to parse java code and traverse its AST.

####Slimit

SlimIt is a JavaScript parser and minifier written in Python. It is used to traverse and modify js AST.



###Modules

####SCA

Sca is responsible for static code analyser. It uses lizard (3rd party app) for this. It contains :

 - **sca.py** It calculates metrics for code written in python, java and javascript.
 - **requirements.txt** It contains requirements required by the sca.py
 - **example** This directory contains example code in python, java and javascript on which sca.py can be tested.

#####Directory Structure
```
    -|/sca/
           -|/requirements.txt
           -|/sca.py
           -|/example/
	           -|/javaex.java
	           -|/jsex.js
	           -|/pythonex.py

```


####DCA
Dca is responsibe for Dynamic Code Analysis.It contains :

 - **dca.py** It uses watchdog (3rd party app). It checks the any change made by the running program and give the url of the file or directory where change is made.
 - **dca_timetravel.py** This implements time travel debugging on the file whose path is entered.
 - **example.py** Example python program which implements time travel debugging.
 - **requirements.txt** It conatins requirements required by the dca.py
 - **timetravelpdb.py** This main python package for time travel debugging.
 - **example** This directory contains python script to test dca.py


#####Directory Structure

```
    -|/dca/
           -|/dca.py
           -|/dca_timetravel.py
           -|/example.py/
           -|/requirements.txt
           -|/timetravelpdb.py/
           -|/example/
	           -|/script.py

```



