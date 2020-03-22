from cs50 import get_int, get_float, get_string

cc = 0

while True:
    cc = get_int("Number: ")
    cc_str = str(cc)
    if len(cc_str) >= 1 and len(cc_str) <= 16:
        #print(len(cc_str))
        break

places = len(cc_str)

luhn = 0 # Luhn's Algo 1st sum - odd place digits

j = 1 # index through cc number

for i in range(places-1,-1,-1): # march backwards through cc number
    temp=0

    digit = int(cc_str[i])
    #print(digit)
    if j%2 == 0:
        temp = 2*digit
        if temp >= 10:
            temp = temp - 9
        luhn += temp
        #print(temp)
    else:
        luhn += digit

    j=j+1


if (luhn % 10 != 0 or places >= 17 or places <= 12):
    print("INVALID")
elif ((int(cc_str[0:2]) == 34 or int(cc_str[0:2]) == 37) and places == 15):
    print("AMEX")
elif (int(cc_str[0]) == 4 and (places == 16 or places == 13)): # VISA
    print("VISA")
elif ((int(cc_str[0:2]) == 51 or int(cc_str[0:2]) == 55) and places == 16):
    print("MASTERCARD")
else:
    print("INVALID")
