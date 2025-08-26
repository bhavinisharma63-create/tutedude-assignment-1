Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>>#task 1

with open ('sample text.txt', 'r') as file:
    print('Reading file contents: ')
    text = file.readline()
    print("line 1: ",text)
    text = file.readline()
    print("line 2: ",text)

try:
    with open ('sample text.txt', 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("Error: The file 'sample text.txt' file was not found.")
finally:
    print(text)
    
... #task 2

a=input("enter text to write to the file: ")


n=open("output.txt","a")
line_1 = n.write(a)
print('data successfully written to output.txt')
b=input("enter additional text to append to the file: ")
line_2 = n.write(b)
print('data succesfully appended to output.txt')
n.close()

z=open("output.txt","r")
t=z.read()
print('Final content of output.txt are: ')
print(t)
z.close()
