def replace_repeated_value(lst):
    count_dict = {}
    repeated_value_found = False
    
    for value in lst:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    
    for key, count in count_dict.items():
        if count > 1:
            repeated_value_found = True
            lst = [value if value != key else -1 for value in lst]
    
    return lst, repeated_value_found

# Example usage
original_list = [1, 2, 3, 2, 4, 5, 2, 6]
modified_list, repeated_value = replace_repeated_value(original_list)
print("Modified list:", modified_list)
print("Repeated value found:", repeated_value)
