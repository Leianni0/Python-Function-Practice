
# Max_Num
def max_num(a, b, c):
    return max(a, b, c)

print(max_num(3, 6, -5))

# Mult_list
def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


print(mult_list([1, 2, 3, 4]))
print(mult_list([3, 5, 7]))  

# Rev_string
def rev_string(my_str):
    return my_str[::-1]

print(rev_string("hello"))
print(rev_string("world")) 

# Num_wihin
def num_within(x, start, end):
    return start <= x <= end

print(num_within(3, 2, 4))  
print(num_within(3, 1, 3))  
print(num_within(10, 2, 5))

# Pascal
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):

        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(2)
pascal(5)


