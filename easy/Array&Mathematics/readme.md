[Solve Yourself Here](https://www.hackerrank.com/challenges/np-array-mathematics/problem)
Task
You are given two integer arrays,  and  of dimensions X. Your task is to perform the following operations:
Add (A+B)
Subtract (A-B)
Multiply (A*B)
Integer Division (A//B)
Mod (A%B)
Power (A**B)
Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
Input Format
The first line contains two space separated integers,  and .
The next  lines contain  space separated integers of array .
After that, the next  lines contain  space separated integers of array .
Output Format
Print the result of each operation in the given order under Task.
Sample Input
1 4
1 2 3 4
5 6 7 8
Sample Output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]