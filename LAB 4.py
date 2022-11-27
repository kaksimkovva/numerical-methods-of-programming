import numpy as np
# 1
a = np.matrix('1 2; 4 -1')
b = np.matrix('2 -3; 4 1')
c = a.dot(b)
d = b.dot(a)
print(c-d)

# 2
a = np.matrix('-1 2; 0 1')
print(a**2)

# 3
a = np.matrix('3 5; 6 -1')
b = np.matrix('2 1; -3 2')
c = a.dot(b)
print(c)

# 4
a = np.matrix('2 3 4; 1 0 6; 7 8 9')
a_det = np.linalg.det(a)
print(format(a_det, '.9g))

# 5
a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2; 4 3 -2 -1')
a_det = np.lialg.det(a)
print(format(a_det, '.9g'))

# 6
A = np.matrix('1 2 -3; 0 1 2; 0 0 1')
A_inv = np.linalg.inv(A)
print(A_inv)

# 7
A = np.matrix('1 2 3 4; 3 -1 2 5; 1 2 3 4; 1 3 4 5')
rank = np.linalg.matrix_rank(A)
print(rank)

# 8 Kramer
a = np.matrix('3 -1 2; 1 4 -1; 2 3 1')
print('A=',a)

b = np.matrix('-4; 10; 8')
print('B=',b)

def kramer (a, b):
  a_det = np.linalg.det(A)
  print('Детермінант матриці = ', a_det)

  if (a_det != 0):
    print ('Розв*язуємо систему')

    x_m = np.matrix(a)
    x_m[:, 0] = b # формування допоміжної матриці (1 ст. замінюємо на ст. b)
    print('x_m=', x_m)

    y_m = np.matrix(a) #2 ст. замінюємо на ст. b
    y_m[:, 1] = b #2 c
    print('y_m=',y_m)

    z_m = np.matrix(a) #3 ст. замінюємо на ст. b
    z_m[:, 2] = b
    print('z_m=',z_m)

    x = np.linalg.det(x_m) / a_det
    y = np.linalg.det(y_m) / a_det
    z = np.linalg.det(z_m) / a_det

    print('X = ', round(x,5))
    print('Y=', round(y,5))
    print('Z=', round(z,5))

  else:
    print('Розв*язків немає')

kramer(a,b)

# 8 Matrix

A = np.matrix('2 -1 1 ; 3 4 -2; 1 -3 1')
B = np.matrix('5 ; -3 ; 4')

print('A=', A)
print('B=', B)
A_inv = np.linalg.inv(A)
print(A_inv)
X = A_inv.dot(B)
print('X=', X)

# 9

def generateArray():
  print('Input first index matrix: ')
  f_index = int(input())

  print('Input second index matrix: ')
  s_index = int(input())
  array = []
  for i in range(s_index):
    array.append([])
    for j in range(s_index):
        array[i].append(reandom.randint(0, 100))
  return array

array = generateArray()
mean_columns = np.mean(array, axios=0)
mean_rows = np.mean(array, axios=1)

print('Matrix', array)
print('Columns avg: ', mean_columns)
print('Rows avg: ', mean_rows)
