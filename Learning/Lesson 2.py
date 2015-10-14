Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
Roger Santos
SyntaxError: invalid syntax
>>> "Roger Santos"
'Roger Santos'
>>> 'Roger Santos'
'Roger Santos'
>>> 'I don't like onion'
SyntaxError: invalid syntax
>>> "I don't like onion"
"I don't like onion"
>>> 'I said "What"'
'I said "What"'
>>> 'I don\'t like onion'
"I don't like onion"
>>> print("Hey now brown cow")
Hey now brown cow
>>> print('C:\Workspace')
C:\Workspace
>>> print('C:\Workspace\SomeThing')
C:\Workspace\SomeThing
>>> print('C:\Workspace\SomeThing\SomeElse')
C:\Workspace\SomeThing\SomeElse
>>> print('C:\Workspace\someThing')
C:\Workspace\someThing
>>> print(r'C:\Workspace\SomeThing')
C:\Workspace\SomeThing
>>> firts = 'Roger'
>>> first  = 'Roger '
>>> first = 'Santos'
>>> print(first)
Santos
>>> first = 'Roger '
>>> first + 'Santos'
'Roger Santos'
>>> first * 10
'Roger Roger Roger Roger Roger Roger Roger Roger Roger Roger '
>>> 
first / 10
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    first / 10
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
