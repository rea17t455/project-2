x = input('input float number: ')
 # print(type(float_num))
sum = 0
for i in x:
 if i != '.':
  sum += int(i)
print(sum)