# Advanced-Algorithms-Summative Questions


Qn1. To solve a mathematical problem that is required to return the sum of the first n numbers is our interest. There are a number of algorithms that can be used to solve the same problem. At this point we need to use loops to add the first n numbers and return the sum.

Context

 n=8

Numbers considered are: 1,2,3,4,5,6,7,8

Sum will be 1+2+3+4+5+6+7+8

The sum will be returned.

 

Tasks to be completed

Write the pseudo code for the algorithm (sufficiently commented)
Derive the function of the running time of the algorithm and express the function in big-oh notation.
Write the program and test it on four different values: 10, 10000, 1000000, 1000000000. What were your observations on the response time on every respective input? How did the output behave and why?
 

Qn2. ALU has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
Examples

 grade = 84 round to 85 (85 - 84 is less than 3)
 grade = 29 do not round (result is less than 40)
 grade = 57 do not round (60 - 57 is 3 or higher)
Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

Function Description

Complete the function gradingStudents.

gradingStudents has the following parameter(s):

int grades[n]: the grades before rounding
Returns

int[n]: the grades after rounding as appropriate
 

Input Format

The first line contains a single integer, n, the number of students.

Each line i of the n subsequent lines contains a single integer, grades[i].

Constraints 

1 <= n <= 60
0 <= grades[i] <= 100
Explanation

Image_49.jpg

Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 75 - 73 < 3, the student's grade is rounded to 75.
Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70 - 67 = 3, the grade will not be modified and the student's final grade is 67.
Student 3 received a 38, and the next multiple of 5 from 38 is 40. Since 40 - 38 < 3, the student's grade will be rounded to 40.
Student 4 received a grade below 33, so the grade will not be modified and the student's final grade is 33.
 

Qn3.

Data communication and cloud computing largely depend on cryptography regardless of the type. Cryptography keeps senders and receivers to be assured that chances are high for non-targeted receivers in understanding the contents shared.

In this context we are required to work on an encryption algorithm that will organize that text in a matrix guided by the key value such that data can be re-written in columns to produce encrypted data.

For example,

Text: Plain text
Key: 2

Table
Image_50.jpg

The key specifies the number of rows while the text length specifies the number of columns. The encrypting function will take two values text and the key, in the end it will return encrypted text. The decryption algorithm will equally have two arguments encrypted text and the key, it will return correct text

Encrypted message: Pantxli et (write a row after a row)

Tasks to be complete

Write algorithms that will implement the encryption and decryption in this context (You may choose to use the pseudo codes or natural English statements, it is up to your choice).
Clarify the correctness of the algorithms by providing the actual implementation in a programming language (of your choice). Present the match between inputs and outputs.
Highlight factors that make the algorithm simple and clear.
What is the running time of the algorithm?
Change the key to be 3 instead of 2, which algorithms among the two (the algorithm that has the key of 2 and the algorithm that has the key of 3) will tend to run slow (and which one will tend to run fast).
 

Qn4. We define super digit of an integer x using the following rules:

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
For example, the super digit of 9875 will be calculated as:

super_digit(9875)   9+8+7+5 = 29 

super_digit(29) 2 + 9 = 11

super_digit(11) 1 + 1 = 2

super_digit(2) = 2 

 

Example

n = ‘9875’

k = 4

The number p is created by concatenating the string n k times so the initial p = 9875987598759875.

superDigit(p) = superDigit(9875987598759875)

                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116

     superDigit(p) = superDigit(116)

                   1+1+6 = 8

     superDigit(p) = superDigit(8)

 

All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it is the super digit.

Function Description

Complete the function superDigit as per the conditions given. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

string n: a string representation of an integer
int k: the times to concatenate n to make p.
Returns

int: the super digit of n repeated k times
Input Format

The first line contains two space separated integers, n and k.

Constraints

1 <= n < 10100000

1 <= k <= 105

 

Explanation

Here n = 148 and k = 3 , so p = 148148148.

super_digit(P) = super_digit(148148148) 

               = super_digit(1+4+8+1+4+8+1+4+8)

                = super_digit(39)

                = super_digit(3+9)

                = super_digit(12)

                = super_digit(1+2)

               = super_digit(3)

                = 3

 

Qn5.

Given an undirected graph and a starting node, determine the lengths of the shortest paths from the starting node to all other nodes in the graph. If a node is unreachable, its distance is -1. Nodes will be numbered consecutively from 1 to n, and edges will have varying distances or lengths.

For example, consider the following graph of 5 nodes:

Begin      End      Weight

  1             2             5

  2             3             6

  3             4             2

  1              3            15

Image_51.jpg

Starting at node 1, the shortest path to 2 is direct and distance 5. Going from 1 to 3, there are two paths: 1 -> 2 -> 3 at a distance of 5 + 6 = 11 or 1 -> 3 at a distance of 15. Choose the shortest path, 11. From 1 to 4, choose the shortest path through 3 and extend it: 1 -> 2 -> 3 -> 4 for a distance of 11 + 2 = 13 There is no route to node 5, so the distance is -1.

The distances to all nodes in increasing node order, omitting the starting node, are 5 11 13 -1.

Function Description

Write a function with the name shortestReach. It should return an array of integers that represent the shortest distance to each node from the start node in ascending order of node number.

shortestReach has the following parameter(s):

n: the number of nodes in the graph
edges: a 2D array of integers where each edges[i] consists of three integers that represent the start and end nodes of an edge, followed by its length
s: the start node number
Input Format

The first line contains t, the number of test cases.

Each test case is as follows:

- The first line contains two space-separated integers n and m, the number of nodes and edges in the graph.

- Each of the next m lines contains three space-separated integers x, y, and r, the beginning and ending nodes of an edge, and the length of the edge.

- The last line of each test case has an integer s, denoting the starting position.

 

Constraints

1 <= t <= 10 (Number of test cases should not be more than 10)

2 <= n <= 3000 (Graph can have a minimum number of 2 nodes and a max of 3000).

1 <= m <= N x (N - 1)/2 (Graph can have a min of 1 edge and a max of N x (N - 1)/2)

1 <= x, y, s <= N (Beginning and ending nodes and the starting position are Natural numbers)

1 <= r <= 105

If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

Output Format

For each of the  test cases, print a single line consisting of n - 1 space separated integers denoting the shortest distance to the n - 1 nodes from starting position s in increasing order of their labels, excluding s.

For unreachable nodes, print -1.

Explanation

The graph given in the test case is shown as :
Image_52.jpg

* The lines are weighted edges where weight denotes the length of the edge.

The shortest paths followed for the three nodes 2, 3 and 4 are as follows :

1/S->2 - Shortest Path Value : 24

1/S->3 - Shortest Path Value : 3

1/S->3->4 - Shortest Path Value : 15
