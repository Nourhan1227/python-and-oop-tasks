# # Write a Python script to read the contents of a text file and print them to the console.
# with open('myfile.txt', 'r') as file:
#     print(file.read())


# # Write a Python script to write a string to a text file. If the file doesn't exist, create it.
# file = open('/home/nour/mypy/myfile2.txt', 'w')
# file.write("hello to myfile2\n")
# file.close()
# print("Text written to myfile2.txt")


# # # Write a Python script to append text to an existing file without overwriting its contents.
# file = open('/home/nour/mypy/myfile2.txt', 'a')
# file.write("Appending new text.\n")
# file.close()
# print("Text appended to myfile2.txt.")



# # # Write a Python script to read a file line by line and print each line with a line number.
# file = open('/home/nour/mypy/myfile2.txt', 'r')
# line_num=0
# for line in file:
#     print(f"Line {line_num}: {line.strip()}")
#     line_num+= 1

# file.close()
# print(line_num)



# # Write a Python script to copy the contents of one file to another.

# s_file = open('/home/nour/mypy/s.txt', 'r')
# dest_file = open('/home/nour/mypy/dest.txt', 'w')
# dest_file.write(s_file.read())

# s_file.close()
# dest_file.close()

# print("Contents copied from source.txt to destination.txt.")



# # Write a Python script to count the number of words in a text file.
# file = open('/home/nour/mypy/s.txt', 'r')
# word_count = 0

# for line in file:
#     word_count += len(line.split())
# file.close()

# print(f"The file contains {word_count} words.")



# # Write a Python script to merge the contents of two text files into a third file.

# file1=open('/home/nour/mypy/s.txt', 'r')
# file2=open('/home/nour/mypy/d.txt', 'r')
# file3=open('/home/nour/mypy/third.txt', 'w')
# file3.write(file1.read())
# file3.write(file2.read())

# file1.close()
# file2.close()
# file3.close()
# print("file1 and file2 is merged into third.txt")




# # Write a Python script to search for a specific word in a file and replace it with another word.
file1=open('/home/nour/mypy/s.txt', 'r')
replace_word=file1.read().replace("hello","hello50000")
file1.close()

file1 = open('/home/nour/mypy/s.txt', 'w')
file1.write(replace_word)
file1.close()

print("hello is replace to hello5000")
