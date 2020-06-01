def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    map1 = {}
    map2 = {}
    map1 = { num : map1.get(num, 1)+1 for num in str(num1)}
    map2 = { num : map2.get(num, 1)+1 for num in str(num2)}
    return map1 == map2
        