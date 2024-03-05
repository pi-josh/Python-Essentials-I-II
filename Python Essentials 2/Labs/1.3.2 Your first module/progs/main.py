from sys import path

path.insert(0, 'C:\\Users\\joshu\\Desktop\\Joshua Files\\Tech Journey\\Free Courses\\Cisco\\Python Essentials 2\\Labs\\1.3.2 Your first module\\modules')

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))