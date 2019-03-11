# lecture string
print('Hi', 'Hello')
print('Hi', 'Hello', end='!')

print('Hi', 'Hello', sep='!')

# 1

string_bark = 'bark'
print(string_bark[0], string_bark[1], string_bark[2], string_bark[3])

string_park = 'park'
print(string_bark[0], string_bark[1], string_bark[2], string_bark[3])

#2

my_string ='pin'
print(my_string[0:2], my_string[1:3])


#3,
my_string = 'abracadabra'
print(my_string[:my_string.find('cadabra')], my_string[my_string.find('cadabra'):])

#4
print(len('four'))

#5
print(len('viisi'))

#6
print('breathe'[:-1])

#7
print('weight'[:-1])

#8.
print('hearth'[1:])

#9.
print('weight'[1:])

#10
my_string= 'intermediate'
start = my_string.find('media')
end = start+len('media')
print(my_string[start:end])

#11
my_string = 'premediates'
start= my_string.find('media')
end = start+len('media')
print (my_string[start:end])

#12 from ’grand’ and ’ma’ create: ’grandma’
first_s= 'grand'
second = 'ma'
print(f'{first_s}{second}')
#or
print('grand'+'ma')

#13 from ’grand’ and ’dad’ create: ’grandad’

grand = 'grand'
dad = 'ad'
print(f'{grand}{dad}')


# 14. from ’grand’ and ’ma’ create: ’grandgrandgrandma’
print(f'{first_s*3}{second}')

# 15. from ’grand’ and ’dad’ create: ’grandgrandgrandgrandad’
print(f'{grand*4}{dad}')

#OR
string1='grand'
string2='dad'
total = string1*4+string2[1:]
print(total)


# 16. from 3 create: ’3’
value=3
print(str(value))


# 17. from 4 create: ’444’
value=4
print(str(value)*3)



#18
another_string= 'Another bad example, what a good day'

print(another_string.replace('good','bad').replace('bad','good',1))
