def print_upper_words(words, check):
  '''take a list as an input and return each list item capitalized on its own line'''
  for word in words:
    if word.startswith((check)):
      print(word.upper())

print_upper_words(["hello", "Hey", "goodbye", "yo", "yes"], ('h','H'))

numbers = list(range(0,11))

def times_two(n):
  return[num * 2 for num in n]

def squared(n):
  return [num ** 2 for num in n]

def generate_grid(size):
 return  [[x for x in range(size)] for x in range(size)]

days = {x : 0 for x in 'mtwtfss'}

def square_dic():
  return {num : num * num for num in range(5)}

def square_dic_evens():
  return{num : num * num if num * num % 2 == 0 else 'odd' for num in range(10)}