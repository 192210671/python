n=input("Enter the Binary Number=")
bin_num="01"
for i in range(len(n)):
  binary=True
  if n[i] not in bin_num:
    print("Invalide input")
    binary=False
    break
if binary:
  dec_num=int(n,2)
  oct_num=oct(dec_num)
  hex_num=hex(dec_num)
  print("DECIMAL=",dec_num)
  print("OCTAL=",oct_num)
  print("HEXADECIMAL=",hex_num)    
