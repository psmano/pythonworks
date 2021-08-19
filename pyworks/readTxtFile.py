#Reading the Text File

filename = input('Enter File Name: ')
file = open(filename,mode='r')
text = file.read()
file.close()

print(text)
