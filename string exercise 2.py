#Playing with string

#1.

my_string = 'anomalocaris'
result = my_string.index('o')
print(result)

#2
my_string = 'anomalocaris'
result_r =my_string.index('r')
print(result_r)

#3
my_string= 'waging on the purple drone'
#result_p = my_string_p.index('on')
print (my_string.rfind('on'))

#4
my_string = 'Superficial'
result_r =my_string.rfind('z')
print(result_r)


#5. find first a in last half
my_long_string = "There truly is a dazzling bright world out there, waiting for us to a explore."
#find second half of the string
second_half= my_long_string[(len(my_long_string))//2:]
#print (second_half)
index_a_2nd_half = second_half.index('a')
print(index_a_2nd_half)
result = len(second_half)+index_a_2nd_half
print(result)
#OR
second_half = (my_long_string[len(my_long_string)//2:]).rfind('a')
print((second_half)+index_a_2nd_half)

#6 find last a in first half
first_half = (my_long_string[:len(my_long_string)//2]).rfind('a')
print(first_half)

#find first a in first half
find_first_a = (my_long_string[:len(my_long_string)//2]).find('a')
print(find_first_a)

#7 print 42
my_number = '91342391'
print(((my_number).lstrip('913')).rstrip('391'))

#
#8
temp_str = '–== Warning! ==–'
print((temp_str.lstrip('–== ')).rstrip(' ==–'))

#9
my_string= '–== Error! ==–'
print(my_string.rstrip('! ==–'))

#10
my_string = '–== Success! ==–'
print(my_string.lstrip('–== '))

#11
my_string = 'Changing your dog for a bird? Some dog-lover you are.'
print(my_string.replace('dog','cat'))

#12
my_string = 'Being bold has some uses.'
print(my_string.replace('o','a'))

#13
my_string ='–== Error! ==–'
print(my_string.upper())

#14
my_string = 'abraham lincoln'
print(my_string.title())

#15. Create ’readable’ from ’rEaDaBlE’
my_string = 'rEaDaBlE'
print(my_string.lower())

#16
my_string = 'first word is capitalized'
print(my_string.capitalize())

#17.
my_string= 'a loooooooooooooooooooong word?'
print(my_string.count('o'))

#18.
godzillion = 100000000000000000000000000000000000000000
#print(my_number.count(0))

#19
my_string = 'Something out of nothing? I really doubt we can do it anytime soon..'
print((my_string[:(len(my_string))//2]).count('n'))

#20. Replace all ’0’ except the ﬁrst with ’9’in godzillion(see deﬁnition above).



#21. From ’what,if,we,have,no,choice?....’ create ’What if we have no choice?’
