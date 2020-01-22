numbers = ["null","üks","kaks","kolm","neli","viis","kuus","seitse","kaheksa","üheksa","kümme"]
nr = 110
k = (nr % 100)
n = ((nr - k) / 100)
p = nr - (n * 100)
#viimane nr
m = (p % 10)
#teine nr
l = ((p - m) / 10)

if nr >= 100:
    if p > 19 and l != 0 and m != 0:
        print (numbers[int(n)] + "sada " + (numbers[int(l)]) + "kümmend " + numbers[int(m)])
    elif l != 0 and p < 20:
        print (numbers[int(n)] + "sada " + numbers[int(m)] + "teist")
    elif l == 0 and m != 0:
        print (numbers[int(n)] + "sada " + numbers[int(m)])
    elif m == 0 and l != 0:
        print (numbers[int(n)] + "sada " + numbers[int(l)] + "kümmend")
    else:
        print (numbers[int(n)] + "sada")
        
elif nr <= 99 and nr > 10:
    if nr > 19 and m != 0:
        print (numbers[int(l)] + "kümmend " + numbers[int(m)])
    elif m == 0:
        print (numbers[int(l)] + "kümmend ")
    else:
        print (numbers[int(m)] + "teist")
elif nr >= 10:
    print (numbers[nr])
    
    
