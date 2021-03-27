x = 4       #4  = 0000 0100
y = 11      #11 = 0000 1011

#4 | 11
z = x|y         #15 = 0000 1111
print('Value of 4|11 is',z)

#4 >> 11
z = x >> y      #0 = 0000 0000
print('Value of 4 >> 11 is', z)

#4 ^ 11
z = x^y         #15 = 0000 1111
print('Value of 4^11 is', z)

#~4
z = ~x          #-5 = 0000 0101
print('Value of ~4 is', z)

#11 & 4
z = y & x       #0 = 0000 0000
print('Value of 11&4 is', z)
