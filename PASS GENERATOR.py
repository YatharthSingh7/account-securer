import random
lower= 'abcdefghijklmnopqrstuvwxyz'
Upper= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol= '!@#$%^&*()?><:"}{/'
number= '1234567889'
use= lower + Upper + symbol + number
length= int(input("enter length for pass"))
password= "".join(random.sample(use,length))
print(password)
