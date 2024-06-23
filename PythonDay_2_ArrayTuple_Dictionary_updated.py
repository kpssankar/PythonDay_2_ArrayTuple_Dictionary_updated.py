#Even and Odd lists
L1 = [10,501,22,37,100,999,87,351]
even_numbers=[]
odd_numbers=[]
for i in L1:
    if (i  % 2==0):
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("even L1:" ,even_numbers)
print ("odd L1:",odd_numbers)   


Output:
=========
Output:

even list: [10, 22, 100]
odd list: [501, 37, 999, 87, 351]



===================================================================================================================================================
#program to filter prem numbers from give list
def is_prime(n):
  """
  Checks if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """

  if n <= 1:
    return False
  for i in range(2, n-1):
    if n % i == 0:
      return False
  return True
L2 = [10,501,22,37,100,999,87,351,7]
num = len(L2)
prime_numbers = []
for num in L2:
  if is_prime(num):
    prime_numbers.append(num)
print(prime_numbers)

Output:

[37, 7]





===============================================================================================================================================

#Python Program to Find Sum of First and Last Digit

number = 1247
 
number = str(number)
 

first_digit = int(number[0])
last_digit = int(number[-1])
 
addition = first_digit + last_digit
 

print('Addition of first and last digit of the number is', 
      addition)

Output:

Addition of first and last digit of the number is 8

====================================================================================================================================================

#program to find duplicates between three lists
list1=[3,4,5,6,7,8,9,11,22]
list2=[9,8,7,6,5,4,3,2,1,11]
list3=[1,2,3,4,5,9,8,7,6,5,22]
duplicate_list1and2= (set(list1).intersection(list2))
duplicate_list1and3= (set(list1).intersection(list3))
duplicate_list2and3= (set(list2).intersection(list3))
print("duplicate between list1and2:" ,duplicate_list1and2)
print("duplicate between list1and3:",duplicate_list1and3)
print("duplicate between list2and3:", duplicate_list2and3)

Output:
duplicate between list1and2: {3, 4, 5, 6, 7, 8, 9, 11}
duplicate between list1and3: {3, 4, 5, 6, 7, 8, 9, 22}
duplicate between list2and3: {1, 2, 3, 4, 5, 6, 7, 8, 9}
==================================================================================================================================================

#program to find first non repeating element in given list4

def firstNonRepeating(list4, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if  element is present in list4
        while(j < n):
            if (i != j and list4[i] == list4[j]):
                break
            j += 1
        # if the element is not present in array
        # except at ith index then return element
        if (j == n):
            return list4[i]
 
    return -1
 
 
# Driver code
list4 = [9, 4, 9, 10, 7, 4]
n = len(list4)
print(firstNonRepeating(list4, n))

==================================================================================================================================================

# python program to find minimum element in sorted list5
 
def findMin(list5, N):
     
    min_ele = list5[0];
 
    # Traversing over array to
    # find minimum element
    for i in range(N) :
        if list5[i] < min_ele :
            min_ele = list5[i]
 
    return min_ele;
 
# Driver program
list5 = [5, 6, 1, -1, 2, 3, 4]
N = len(list5)
list=sorted(list5)
 
print(findMin(list5,N))
 

 Output:

-1

===========================================================================================================================================





# Python3 program to find first non-repeating element.
 
def firstNonRepeating(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1
 
 
# Driver code
arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))
===================================================================================================================================================

#python program to find minimum element in a rated and sorted list

def findMin(arr, N):
    
    min_ele = arr[0];

    # Traversing over array to
    # find minimum element
    for i in range(N) :
        if arr[i] < min_ele :
            min_ele = arr[i]

    return min_ele;

# Driver program
arr = [5, 6, 1, 2, 3, 4]
N = len(arr)

print(findMin(arr,N))

=====================================================================================================================================

#python program to find if there is a sub-list with sum equal to zero

def subArrayExists(arr, N):
    # traverse through array  and store prefix sums
    n_sum = 0
    s = set()

    for i in range(N):
        n_sum += arr[i]

        # If prefix sum is 0 or  it is already present
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)

    return False


# Driver's code
if __name__ == '__main__':
    arr = [-3, 2, 3, 1, 6]
    N = len(arr)

    # Function call
    if subArrayExists(arr, N) == True:
        print("Found a subarray with 0 sum")
    else:
        print("No Such sub array exits!")
        
================================================================================================================================================================

