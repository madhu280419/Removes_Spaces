a = input("  python  is  cool  ")
def remove_spaces(a):
    res = ""
    char = 0
    while char < len(a):
      if ord(a(char)) == 32:
         if char+1 != 32:
              res = ord(char - 32)
              char += 1
      continue
      res += char
    return res
print(remove_spaces(a))