## Description
Python program for generating all **combinations** of numbers in
**range 1 to n**.

## Usage
<p align="center">
  <img src="https://github.com/RagingTiger/gifs/raw/master/combinatorics.gif"/>
</p>

As can be seen above, the combinatorics program can be passed an argument
**n** that will be the number used to generate a list of numbers from 1 to n:
```
n = 3 --> [1, 2, 3]
n = 4 --> [1, 2, 3, 4]
n = 5 --> [1, 2, 3, 4, 5]
.
.
.
n = x --> [1, 2, 3, ..., x]
```

##Purpose
This program was developed to simply demonstrate the implementation of a
**recursive** approach to generating all combinations of a list of elements.
This logic can be seen in the [recur_combine()](https://github.com/RagingTiger/combinatorics/blob/464c2c82d839c80ba3ac36ea59a429e7545d5feb/combinatorics.py#L50-L65) function:

```python
def recur_combine(entry, clist, num):
      # if max depth reached, print combo
      if entry == num:
          print ''.join(clist)
          return

      # build combinations recursively
      for i in range(entry + 1):
          # copy and recurse
          copy = clist[:]
          copy.insert(i, numbers[entry])
          recur_combine(entry + 1, copy, num)
```
