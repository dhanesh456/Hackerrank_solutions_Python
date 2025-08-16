"""
Task:
-----
The provided code stub reads two integers from STDIN, a and b.  
Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (a - b).
3. The third line contains the product of the two numbers.

Example:
--------
Input:
3
2

Output:
5
1
6
"""

# Solution
def main():
    a = int(input().strip())
    b = int(input().strip())
    
    # Printing results
    print(a + b)   # Sum
    print(a - b)   # Difference
    print(a * b)   # Product


if __name__ == "__main__":
    main()
