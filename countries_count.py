# ------------------------------------------------------------
# Problem: Set .add() — Distinct Country Stamps
#
# Task:
#   Rupal has a huge collection of country stamps. Count the
#   total number of DISTINCT country stamps in her collection.
#
# Input Format:
#   Line 1: An integer n — number of country stamps.
#   Next n lines: One country name per line.
#
# Output Format:
#   A single integer — the number of distinct country stamps.
#
# Notes:
#   - Use a set to store unique country names.
#   - The sample includes a trailing space in "France ".
#     We use .strip() so "France" and "France " are treated the same.
# ------------------------------------------------------------

def main():
    n = int(input().strip())
    print(f"Total number of stamps to process: {n}")  # debug print
    
    stamps = set()

    for i in range(n):
        country = input().strip()  # remove leading/trailing spaces
        print(f"Reading country {i+1}: '{country}'")  # debug print
        before_size = len(stamps)
        stamps.add(country)
        after_size = len(stamps)
        
        if after_size > before_size:
            print(f"  -> Added '{country}' to set.")
        else:
            print(f"  -> '{country}' already in set, not added again.")

        print(f"  Current set: {stamps}")
        print(f"  Distinct count so far: {after_size}\n")

    # Print the number of distinct countries
    print("Final Result:")
    print(len(stamps))


if __name__ == "__main__":
    main()
