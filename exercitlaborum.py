def update_average(current_avg, new_value, weight):
    """
    Update the current average with a new value using the given weight.
    
    Args:
    - current_avg (float): The current average value.
    - new_value (float): The new value to incorporate into the average.
    - weight (float): The weight factor determining the influence of the new value.
    
    Returns:
    - float: The updated average.
    """
    return current_avg + (new_value - current_avg) / weight

# Example usage
current_avg = 10.0
new_value = 12.0
weight = 5

updated_avg = update_average(current_avg, new_value, weight)
print(updated_avg)  # Output: 10.4
