"""2**15 = 32768 and the sum of the digits is 3 + 2 + 7 + 6 + * = 26.

What is the sum of the digits of the number 2**1000?"""

power = list(str(2**1000))

print(power)
print("Number of digits: " + str(len(power)))

sum = 0

for digit in power:
    sum += int(digit)

print("the sum of the digits is: {0}".format(sum))
