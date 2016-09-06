## Usage Guide

This analyser has two main parts static code analyser (SCA) and dynamic code analyser (DCA).

###Static Code Analyser (SCA)

It is very simple to use the Static Code Analyser.



 - Run the sca.py python file at `../sca/sca.py`
 - Enter the path of the code to be scanned (only python, java and javascript code is allowed)
 - It will produce the output.

#### Output Format
```

Enter file location : example/pythonex.py
-----Functional Analysis-----
---function number 1---
cyclomatic_complexity   1
token_count     13
name    sum
parameters      ['a', 'b']
fan_out 0
top_nesting_level       0
filename        example/pythonex.py
nloc    2
long_name       sum( a , b )
length  2
end_line        7
start_line      6
general_fan_out 0
fan_in  0
---function number 2---
cyclomatic_complexity   1
token_count     22
name    __init__
parameters      ['self', 'arg']
fan_out 0
top_nesting_level       1
filename        example/pythonex.py
nloc    3
long_name       __init__( self , arg )
length  3
end_line        18
start_line      16
general_fan_out 0
fan_in  0
---function number 3---
cyclomatic_complexity   1
token_count     9
name    di
parameters      ['self']
fan_out 0
top_nesting_level       1
filename        example/pythonex.py
nloc    2
long_name       di( self )
length  2
end_line        21
start_line      20
general_fan_out 0
fan_in  0
```


###Dynamic Code Analyser (DCA)

Dynamic Code Analyser contains two parts:

 - Change Detector
 - Time Travel Debugger

 ####Change Detector

 - Run the dca.py python file at `../dca/dca.py`
 - Enter the path of the directory to be checked for channge
 - Enter the path of the file to be analysed (only python, java and javascript code is allowed)
 - It will produce the outout giving the path of the file or directory which is changed



   ##### Output Format
```
 Enter the path of directory to be checked => .
Enter path of file to be tested => example/script.py
3         //output of the analysed code
2	  //output of the analysed code
1	  //output of the analysed code

on_modified
.\emample.txt  //example.txt is modified by the analysed code
```

#### Time Travel Debugger

Time travel debugger is used to check the value of a variable at any instant in the program.

    It works only in linux.
    It works only for python2.x



 - Copy the python file `timetravelpdb.py` at `../dca/timetravelpdb` to `../python2x/Lib`
 - Add these code in top of your pyhton code

> import timetravelpdb
  timetravelpdb.set_trace()

Enter the following commands to use it:

```
 n => for executing next statement
 ulist => for listing the previous universe exist
 ujump => for jumping to any existing universe
 print {vaiable name} = > to check the value of the   variable name
 uup => for coming back to current universe
```




