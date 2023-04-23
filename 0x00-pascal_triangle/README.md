# Pascal Triangle
The Pascal triangle is a mathematical construct named after the 17th century French mathematician Blaise Pascal, who explored its features. It is a triangular array of integers with a single number 1 in the first row and each successive row created by adding the adjacent numbers in the preceding row.

# Algorithm
```
C(n, k) = n! / (k! * (n-k)!)
```
where `n` is the row number (starting from 0), `k` is the element number within that row (also starting from 0), and ! denotes the factorial function. The value `C(n, k)` represents the number of ways to choose `k` items from a set of n distinct items, without regard to order.

# Code
 ```

def pascal_triangle(n):
    """_summary_

    Args:
        n (int): number of rows in Pascal Triangle

    Returns:
        list: a list containing Pascal Triangle of int row n
    """

    if n <= 0:
        return []

    P_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(P_triangle[i-1][j-1] + P_triangle[i-1][j])
        row.append(1)
        P_triangle.append(row)
    return P_triangle

 ```

# FAQs
Feel free to contact me.

[![Twitter Badge](https://img.shields.io/badge/Twitter-Profile-informational?style=flat&logo=twitter&logoColor=white&color=1CA2F1)](https://twitter.com/That_Blakie)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/samuel-theophilus/)
