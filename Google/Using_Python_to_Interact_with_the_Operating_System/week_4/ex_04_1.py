def for_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 600 + seconds


cont = 'y'

while(cont.lower() == 'y'):
    hours = int(input("Enter the hours - "))
    minutes = int(input("Enter the minute - "))
    seconds = int(input("Enter the seconds - "))
    print(f"That's {for_seconds(hours, minutes, seconds)} seconds ")
    print()
    cont = input('Do you want to do another conversion [y to continue] - ')

print('God Bye!!!')
