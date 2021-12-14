
def superDigits(x,k):
    s = digsum(x)
    return sup_digit(str(int(s)*k))

def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit( digsum(x) )

def digsum(x):
    return str(sum((int(i) for i in list(x))))

#here are the different test cases
n = '9875'
k = 4
print("n = "+ str(n) +', k = '+ str(k) + ', concatenated value = ' + str(n*k) + " superdigit is  " + str(superDigits(n,k)))

n = '148'
k = 3
print("n = "+ str(n) +', k = '+ str(k) + ', concatenated value = ' + str(n*k) + "superdigit is   " + str(superDigits(n,k)))

n = '56345'
k = 6
print("n = "+ str(n) +', k = '+ str(k) + ', concatenated value = ' + str(n*k) + " superdigit is " + str(superDigits(n,k)))
