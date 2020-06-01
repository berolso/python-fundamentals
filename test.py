x = 'awesome'
y = 4
print('this is .', x )

print(x) if y > 5 else print('not',x)

while y < 10:
  print(y)
  y += 1

guess = None
target = 40
while guess is not target:
  guess = input('guess a number..')
  if guess == 'q':
    print('quitter')
    break
  guess = int(guess)
  if guess == target:
    print('you got it')
    break
  print('nope, try again')

anything = '123'
for num in anything:
  print(num)

def say_name(name):
  print(f'hi my name is {name}')
