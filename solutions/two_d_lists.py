# TODO: Implement a function that takes a two-dimensional list and returns the number of rows and the number of columns separately
def get_row_count(two_d_list):
    num_rows = len(two_d_list)
    return num_rows

def get_column_count(two_d_list):
    num_columns = len(two_d_list[0]) if two_d_list and two_d_list[0] else 0
    return num_columns    

# TODO: Implement a function that returns the element at the specified row and column in a two-dimensional list
def get_element(two_d_list, row, col):
    # Check if the specified row and column indices are valid
    if 0 <= row < len(two_d_list) and 0 <= col < len(two_d_list[0]):
        # Return the element at the specified row and column
        return two_d_list[row][col]
    else:
        # Return None for invalid indices
        return None


# TODO: Implement a function that returns the sum of all numbers in a two-dimensional list
def sum_two_d_list(two_d_list):
    # Initialize the sum to zero
    total_sum = 0
    
    # Iterate through each row in the two-dimensional list
    for row in two_d_list:
        # Add the sum of elements in each row to the total sum
        total_sum += sum(row)
    
    return total_sum


# TODO: Implement a function that prints each row of a two-dimensional list on a new line
def print_rows(two_d_list):
    for row in two_d_list:
        print(row)

# TODO: Implement a function that checks whether a given value is present in any of the sublists within a two-dimensional list
def contains_value(two_d_list, value):
    for row in two_d_list:
        if value in row:
            return True
    return False

# TODO: Implement a function that appends a new value at the end of every sublist within a two-dimensional list
def append_to_sublists(two_d_list, value):
    for row in two_d_list:
        row.append(value)

# TODO: Implement a function that replaces all instances of old_value with new_value in a two-dimensional list
def replace_in_two_d_list(two_d_list, old_value, new_value):
    for row in two_d_list:
        for i in range(len(row)):
            if row[i] == old_value:
                row[i] = new_value

# TODO: Implement a function that returns a new list containing only the first elements of each sublist in a two-dimensional list
def first_elements(two_d_list):
    result = []
    for row in two_d_list:
        if row:  # Check if the sublist is not empty
            result.append(row[0])
    return result

# TODO: Implement a function that returns a list of lists, where each inner list contains the elements of the original sublists that are at even indices
def even_elements_sublists(two_d_list):
    result = []
    for row in two_d_list:
        even_elements = [row[i] for i in range(0, len(row), 2)]
        result.append(even_elements)
    return result

# TODO: Implement a function that concatenates all sublists in a two-dimensional list into a single list
def concatenate_sublists(two_d_list):
    result = [element for sublist in two_d_list for element in sublist]
    return result
