# ----------------------------------------------------
# Problem Statement:
# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, print the numbers from 1 to n
# as a single string without spaces.
#
# Input Format:
# A single integer, n.
#
# Output Format:
# Print the list of integers from 1 through n as a single string, without spaces.
#
# Example:
# Input:
# 3
# Output:
# 123
# ----------------------------------------------------

def main():
    # Reading input
    print("Enter a number")
    n = int(input())
    
    # Printing numbers from 1 to n without spaces
    for i in range(1, n + 1):
        print(i, end="")

if __name__ == "__main__":
    main()
