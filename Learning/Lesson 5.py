Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numbers = [20, 50, 29, 87, 45]
>>> numbers[2]
29
>>> numbers[2] = 43
>>> numbers
[20, 50, 43, 87, 45]
>>> numbers + [47, 33, 99]
[20, 50, 43, 87, 45, 47, 33, 99]
>>> numbers
[20, 50, 43, 87, 45]
>>> numbers.append(28)
>>> numbers
[20, 50, 43, 87, 45, 28]
>>> numberns.append(99)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    numberns.append(99)
NameError: name 'numberns' is not defined
>>> numbers.append(99)
>>> numberns
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    numberns
NameError: name 'numberns' is not defined
>>> numbers
[20, 50, 43, 87, 45, 28, 99]
>>> numbers[:3]
[20, 50, 43]
>>> numbers[:2] - [0, 0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    numbers[:2] - [0, 0]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> numbers[:2] = [0, 0]
>>> numbers
[0, 0, 43, 87, 45, 28, 99]
>>> numbers[:2] = [0, 0]
>>> numbers
[0, 0, 43, 87, 45, 28, 99]
>>> numbers[:2] = []
>>> numbers
[43, 87, 45, 28, 99]
>>> numbers [:] = []
>>> numbers
[]
>>> 
