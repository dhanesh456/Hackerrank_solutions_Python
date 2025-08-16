"""
Task:
-----
Given an integer n, perform the following conditional actions:

- If n is odd, print "Weird"
- If n is even and in the inclusive range of 2 to 5, print "Not Weird"
- If n is even and in the inclusive range of 6 to 20, print "Weird"
- If n is even and greater than 20, print "Not Weird"

Input Format:
-------------
A single line containing a positive integer, n.

Constraints:
------------
1 <= n <= 100

Output Format:
--------------
Print "Weird" if the number is weird. Otherwise, print "Not Weird".

Sample Input 0:
---------------
3

Sample Output 0:
----------------
Weird

Explanation 0:
--------------
n = 3 → odd → print "Weird"

Sample Input 1:
---------------
24

Sample Output 1:
----------------
Not Weird

Explanation 1:
--------------
n = 24 → even and > 20 → print "Not Weird"
"""


# Solution
def main():
    n = int(input().strip())

    if n % 2 != 0:          # odd
        print("Weird")
    elif 2 <= n <= 5:       # even and 2-5
        print("Not Weird")
    elif 6 <= n <= 20:      # even and 6-20
        print("Weird")
    else:                   # even and > 20
        print("Not Weird")


if __name__ == "__main__":
    main()
