lwr = 100
uppr = 2000
for numb in range(lwr, uppr + 1):

   odr = len(str(numb))
   sum = 0
   tem = numb
   while tem > 0:
       digit = tem % 10
       sum += digit ** odr
       tem //= 10
   if numb == sum:
       print("The Armstrong numbers are: ",numb)
