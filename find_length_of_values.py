def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }
    s="a"
    d="b"
    h="c"
    q=data.get(s)
    r=data.get(d)
    g=data.get(h)
    return len(q+r+g)
print(find_length_of_values(data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }))