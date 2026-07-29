"""This is and demo python file for checking github action where we are using github action with ephermal runner to check python syntax ( linting )"""
def intro():
  name = "Himanshu Kumar"
  age = 22
  usecase = "Linting a pyton file using github action.IF you see this message this action is succesfull !!!"
  print(f"Hii {name} here !!!, I am {age} year old." + usecase)
  return "Execution completed !!"

def meta_data(name = "Himanshu"):
  length = len(name)
  print(f"The name has {length} letters !! ")
  return "Got Name length !!"
  
print(intro())
print(meta_data())
  
