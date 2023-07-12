def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    s=0
    for i in range(len(data)):
        last=data.popitem()
        s+=last[1]
    return s
data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }
a=sum_dict_values(data)
print(a)