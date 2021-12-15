
def superDigits(n,k):
    s = digsum(n)
    return sup_digit(str(int(s)*k))

def sup_digit(n):
    if len(n) <= 1:
        return n
    else:
        return sup_digit( digsum(n) )

def digsum(n):
    return str(sum((int(i) for i in list(n))))

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
