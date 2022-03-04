def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        binlen = len(str(bin(number)))
        octf = oct(i).split('o')
        hexf = hex(i).split('x')
        binf = bin(i).split('b')
        print(i ,"", octf[1] ,"", hexf[1].upper() ,"", binf[1] )
