import os
import datetime
# os.remove(
#     'Using_Python_to_Interact_with_the_Operating_System/week_2/my_text_copy.txt')

# os.rename(
#     'Using_Python_to_Interact_with_the_Operating_System/week_2/my.txt', 'Using_Python_to_Interact_with_the_Operating_System/week_2/my_blade.txt')

# print(os.path.exists('my_blade.txt'))

# print(os.path.getsize(
#     'Using_Python_to_Interact_with_the_Operating_System/week_2/my_blade.txt'))
# print(os.path.getmtime(
#     'Using_Python_to_Interact_with_the_Operating_System/week_2/my_blade.txt'))
# time_stamp = os.path.getmtime(
#     'Using_Python_to_Interact_with_the_Operating_System/week_2/my_blade.txt')
# print(datetime.datetime.fromtimestamp(time_stamp))
# print(os.path.abspath('my_blade.txt'))


# print(os.getcwd())

# os.mkdir('my_new_dir')
# for i in range(0, 5):
#     os.mkdir(f'my_new_dir_{i}')

# os.chdir('my_new_dir')
# os.rmdir('/home/johndoe/MY_education/Coursera/my_rep/Google/Using_Python_to_Interact_with_the_Operating_System/week_2/my_new_dir')
# print(os.getcwd())

print(os.listdir("week_2"))

dir = ("week_2")
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} as directory")
    else:
        print(f"{fullname} as file")
