"""
Task:
-----
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines:
1. The first line should contain the result of integer division (a // b).
2. The second line should contain the result of float division (a / b).

No rounding or formatting is necessary.

Example:
--------
Input:
4
3

Output:
1
1.33333333333
"""

# Solution
def main():
    a = int(input().strip())
    b = int(input().strip())
    
    # Integer division
    print(a // b)
    
    # Float division
    print(a / b)


if __name__ == "__main__":
    main()
