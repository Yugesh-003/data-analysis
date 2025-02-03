##Indentation Error
# def func():
# print("Hello")  




# #Type Error
# num = 10 
# text = "Hello"  
# print(num + text)  




# ##Index Error
# lst = [1, 2, 3]  
# print(lst[5])  # IndexError: list index out of range
# for i in range(4):
#     print(lst[i])



#Attribute Error
# num = 10 
# num.append(5)   # AttributeError: 'int' object has no attribute 'append'
# print(num)



# # #ModuleNotFound Error
# import numberpy  # ModuleNotFoundError: No module named 'non_existent_module'
# print("successfully imported")




# #Runtime Error
# def func():
#     func()  # Infinite recursion
# func()  # RuntimeError: maximum recursion depth exceeded







##FileNotFound Error

# with open("mark.txt", "r") as file:
#     content = file.read()  # FileNotFoundError: [Errno 2] No such file or directory





# #IO Error
# f = open("mark.txt","r")
# f.write("hi")   # cant write in a file that is opened for reading
