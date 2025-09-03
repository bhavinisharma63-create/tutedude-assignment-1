Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>>#task 1

#task 1
marks = {'arjun':'56','aparashit': '71','shruti':'97'}
name = input('Enter your student name: ')
if name in marks:
    print(f"{name} marks are:{marks[name]}")
else:
    print(f"sorry no record found of {name} ")
    
#task 2

l=[1,2,3,4,5,6,7,8,9,10]
print(f"the original list:{l} ")
first_five = l[:5]
print(f"extracted first five elements: ",first_five)
reversed_list = first_five[::-1]
print(f"Reversed extracted elements: ",reversed_list)
