def cheeseshop(kind,*arguments,**keywords):

  print("------------Do you have any ",kind,'?')
  print("--------I'm sorry ,we 're all out of ",kind)
  for arg in arguments:
    print(arg)
    print("-"*40)
  for kw in keywords:
    print(kw,":",keywords[kw])  
cheeseshop("burger","It's very runny,sir","It's very runny runny sir",shopkeeper="Nithin",client="Raja",sketch="cheese shop")     
