# 2 Keys Keyboard
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

1. Method to solve task
  - Prototype: def minOperations(n)
  - Returns an integer
  - If n is impossible to achieve, return 0

# Algorithm
The function takes `n` numbers of `H` characters by copying and pasting the existing `H's`. Below is a simple approach or pseudocode:
1. Initialize a variable `count` to 0 and a variable `factor` to 2.
2. While `n` is greater than 1:
   -  If `n` is divisible by `factor`, divide `n` by `factor` and add `factor` to `count`.
   -  Otherwise, increment `factor` by 1.
3. Return `count`

# FAQs
Feel free to contact me.

[![Twitter Badge](https://img.shields.io/badge/Twitter-Profile-informational?style=flat&logo=twitter&logoColor=white&color=1CA2F1)](https://twitter.com/That_Blakie)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/samuel-theophilus/)
