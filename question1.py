# By Heather Mataruse
#This is a simaple algorithm that takes n number of elements 
#and returns the sum of them 
#This program also calculates that time taken to execute a certain number of elements 
#to calculate their sume using the time function



# here is my function for calculating the sum_of_numbers
def sum_of_n_numbers(n):

#here is our variable sum of numbers set to zero since we do not have any numbers yet
    sum_of_numbers = 0
    
#here we start by counting from first number 
    for numbers in range(1,n+1):
        sum_of_numbers += numbers
        
    # here we return the sum of the n numbers
    return sum_of_numbers
    
#this is the function that is already in python that I am calling 
#to calculate the running time
import time
start = time.process_time()

#here is where i show the output for putting the different input values
print("when input  is 10. The output is "+ str(sum_of_n_numbers(10)) + ' || Execution time: ' + str(time.process_time() - start)+"seconds")
print("when input  is 1000. The output is "+ str(sum_of_n_numbers(10000)) + ' || Execution time: ' + str(time.process_time() - start)+"seconds")
print("when input  is 1000000. The output is "+ str(sum_of_n_numbers(1000000)) + ' || Execution time: ' + str(time.process_time() - start)+"seconds")
print("when input  is 1000000000. The output is: "+ str(sum_of_n_numbers(1000000000)) + ' || Execution time: ' + str(time.process_time() - start)+"seconds")
