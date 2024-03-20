def int_to_roman(num):
    romans={
  1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'

    }

    roman_num=""

    for value in sorted(romans.keys(),reverse=True):
        while num>=value:
            roman_num+=romans[value]
            num-=value

    return roman_num


number=154
print(int_to_roman(number))
