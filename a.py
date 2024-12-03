
a = open('a.txt', 'r')
b = a.read()
print(b)
a.close()



a= open('a.txt', 'w')
a.write('Hello, World!')
a.close()


file = open('a.txt', 'a')
file.write('Ragul.')
file.close()
