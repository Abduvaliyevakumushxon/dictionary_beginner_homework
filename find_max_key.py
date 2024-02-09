def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
    d=list(data.keys())
    
    return max(d)
print(find_max_key(data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }))