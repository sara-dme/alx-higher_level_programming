#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for ls in my_list :
        if i == x:
            break
        else:
            try:
                print(f"{my_list[i]}", end="")
                i = i + 1
            except :
                break
    print()
    return(i)
