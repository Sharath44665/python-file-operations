# my_file =open("my_file.txt")
# content=my_file.read()
# print(content)
# my_file.close()
#       OR we can do the following

# reading the file
# with open("my_file.txt") as my_file:
#     content=my_file.read()
#     print(content)

# writing to the file
# with open("my_file.txt", mode="w") as my_file: # this will overwrite the existing texts
#     my_file.write("I like Coffee")

# with open("my_file.txt", mode="a") as my_file: # mode a for append
#     my_file.write("I like Arch linux")

# create new file and write something into file
with open("new_text.txt", mode="w") as my_file:
    my_file.write("Hi, I am sharathchandra")
    