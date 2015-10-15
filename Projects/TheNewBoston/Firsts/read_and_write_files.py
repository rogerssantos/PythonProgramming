fw = open('sample.txt', 'w')
fw.write('My name is Roger and I like the moon\n')
fw.write('and I also like cheeseburger.')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)