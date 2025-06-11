def remove_spaces(a):
    result = ""
    space_added = False
    for i in a:
        if ord(i) == 32:
            if not space_added:
                result += " "
                space_added = True
        else:
            result += i
            space_added = False
    return result.strip()
a = input("enter a string")
print(remove_spaces(a))