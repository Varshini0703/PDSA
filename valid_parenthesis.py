def isValid(s):
  mapping = {
      ')':'(',
      ']':'[',
      '}':'{'
  }
  stack = []
  for char in s:
    if char not in mapping:
      stack.append(char)    # appending all the open braces into the stack list
    else:
      if len(stack)==0:     # meaning no open braces
        return False 
      if mapping[char] != stack.pop():
        return False
  if len(stack)!=[]:
    return False
  return True 
