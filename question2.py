#by Heather Mataruse


import math
# this list contains the grades that i will round off later in the code
original_grades = [73,38,67,33]

#here is my function that calculates the different student gradess 
def gradingStudents(grades):
    #i the created a list where the final grades will be stored
    n = []
    
    # I creates a for loop while loop to check 
    # the number the grades is so that if can round it off to give the final grades
    for grades in original_grades:
#if the grades is lower than 38 its considered as fail hence in that case round is not necessary
        if grades < 38:
            n.append(grades) 
            
        else:
            
            #then i find the nearest multiple of 5 is the grades is >= 38
            rounded_grades = math.ceil(grades/5)*5
        
            if rounded_grades-grades < 3:
                n.append(rounded_grades)
            else:
                n.append(grades)
                
    #here i returned the official grades of the student 
    return n

print("Student original grade : "+ str(original_grades))
print("Student final grade:    "+ str(gradingStudents(original_grades)))
