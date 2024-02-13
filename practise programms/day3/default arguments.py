#default arguments
def ask
_ok(prompt,retries=4,remainder='Please try Again!'):
  while True:
    ok=input(prompt)
    if ok in ('y','ye','yes'):
      return True
    if ok in ('n','no','nop','nope'):
      return False
    retries=retries-1
    if retries <0:
      raise ValueError("Invalid user response")
      print(remainder)
ask_ok('Do you really want to quit?')

