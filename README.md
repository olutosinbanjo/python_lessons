# python_lessons

### Python Traceback in General

A Python traceback is composed of several sections of relevance. The diagram below helps visualize these different parts.

{% img 'python-traceback-diagram' centered=True %}

When debugging a Python code, it is best to read the traceback output using a **Bottom-Up** approach. In the diagram, the last line of the traceback is the error message line- it contains the exception name (outlined in blue),  which indicates the type of error that occurred. Next to the exception name is the error message (outlined in green), which provides information for understanding why the exception occurred.  

Moving up the traceback are the different function calls (outlined in yellow) arranged from the most recent to the least recent call. These function calls are indicated by two line entries. The first line provides information such as the file name, line number, and module name, which specifies the location of the code. On the other hand, the second line specifies the actual code that was executed (underlined in red). 

There are a few differences between traceback outputs when executing your code in the command line and running code in the REPL. Below is an example of the same code from the previous section executed in a REPL and the resulting traceback output. 

\```pycon
>>> def greet( someone ):
>>>
...   print('Hello, ' +someon)
... 
>>> greet("Chad")

Traceback (most recent call last):
  File "", line 1, in 
  File "", line 2, in greet
NameError: name 'someon' is not defined
```
