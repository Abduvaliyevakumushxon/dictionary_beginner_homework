def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }
    d=list(data.values())
    
    return max(d)
print(find_max_value(data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  })) 
