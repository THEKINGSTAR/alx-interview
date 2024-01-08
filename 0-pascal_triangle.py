#!/usr/bin/python3
"""
function pascal_triangle
that
returns a list of lists of integers representing the Pascal’s triangl of n.
"""

def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    pascal = []
    if (n <= 0):
        return (pascal)
    else:
        # Use a loop to iterate through each row from 0 to the desired number of rows (n).
        for row in range(n):
            # For each row, initialize a list (row) with 1 repeated i + 1 times, where i is the current row index.
            row_list = [1] * (row + 1)
            
            # Use another loop to calculate the values inside the row.
            # Start the loop from the second element (j = 1) up to the second-to-last element (i - 1).
            for v in range(1, row):
                # Set row[j] to the sum of the values from the previous row: triangle[i - 1][j - 1] + triangle[i - 1][j].
                row_list[v] = pascal[row -1][v -1] + pascal[row -1][v]
        
            # Append the completed row to the list storing Pascal's Triangle.        
            pascal.append(row_list)
    
    return(pascal)
        
        















