# Lockboxes
In this task, `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

1. Method to solve task
     - Prototype: `def canUnlockAll(boxes)`
     - `boxes` is a list of lists
     -  Assuming all keys will be positive integers
        - There can be keys that do not have boxes
     - The first box `boxes[0]` is unlocked
     - Returns `True` if all boxes can be opened, else return `False`


# Algorithm
The function takes a list of lists `boxes` as input and returns `True` if all the boxes can be unlocked, else it returns `False`. The `open_boxes` list keeps track of which boxes have been unlocked, and the `keys` list keeps track of the keys that have been collected. The function starts with the first box (index 0) unlocked and adds the keys from that box to the `keys` list. It then checks each box in order and tries to unlock it using the keys in the `keys` list. If a box can be unlocked, the function adds the keys from the newly unlocked box to the `keys` list. The function continues until all boxes have been checked or all boxes have been unlocked.

# FAQs
Feel free to contact me.

[![Twitter Badge](https://img.shields.io/badge/Twitter-Profile-informational?style=flat&logo=twitter&logoColor=white&color=1CA2F1)](https://twitter.com/That_Blakie)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/samuel-theophilus/)
