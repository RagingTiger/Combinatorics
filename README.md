## Description
Python program for recursively generating all **combinations** of numbers in
**range 1 to n**.

## Usage
<p align="center">
  <img src="https://github.com/RagingTiger/gifs/raw/master/combinatorics.gif"/>
</p>

As can be seen above, the combinatorics program can be passed an argument
**n** that will be the number used to generate a **list of numbers** from
1 to n:

```
n = 3 --> [1, 2, 3]
n = 4 --> [1, 2, 3, 4]
n = 5 --> [1, 2, 3, 4, 5]
.
.
.
n = x --> [1, 2, 3, ..., x]
```

This list of numbers is then used to generate every possible combination of
ordering of the elements from the list. If **n = 3**, the resulting
list **[1, 2, 3]** will have **n!** possible combinations (i.e. **3! = 6**):

```
                  1  - - - - - - - - (l0) level
                  |
                  |
                 / \
                /   \
               /     \
              /       \
            21         12 - - - - - - (l1) level
           /            \
          |              |
         /|\            /|\
        / | \          / | \
     321 231 213    312 132 123 - - - (l2) level
```

The tree shown above depicts these combinations as they are generated from
traversing the tree to its leaf nodes. We can now begin to understand why
combinatorial problems are **n!** for generating all possible combinations: the
number of leaf nodes (i.e. combinations) is the product of all the tree levels
**l** plus one. For **n = 3**, we have 3 levels: **l0 = 0**, **l1 = 1**,
and **l2 = 2**. In this case **(0+1) x (1+1) x (2+1) = 6** combinations.

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
