def print_formatted(number):
    
    for i in range(1,number+1):
        integer=i
        octal=oct(i)
        hexal=hex(i)
        binary=bin(i)
        
        print(integer,"    ",octal[2:],"    ",hexal[2:].upper(),"    ",binary[2:])
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
