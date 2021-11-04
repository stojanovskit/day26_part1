# list1 = []
# list2 = []
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()
# with open("file2.txt") as file2:
#     for num in file2:
#         list2.append(num.rstrip("\n"))
result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆


print(result)






