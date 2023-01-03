print('------------------------------')
print('|    My calculator           |')
print('------------------------------')
print('')
print('Calculate sum of two values, X + Y')
continueCalculation = 'Y'
while continueCalculation == 'Y':
  print('')
  x = input('Value of X: ')
  y = input('Value of Y: ')
  result = int(x)+int(y)
  print('')
  print(f'The result of {x} and {y} is {result}')
  print('')
  continueCalculation = input('Continue Y/n: ')
  if continueCalculation != 'n':
     continueCalculation = 'Y'
print('')
print('Thanks for using myCalculator')