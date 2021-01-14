import re
print("LOCAL HACK DAY - 04\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
output = ""
shift = int(input("Enter the shift you wish to encode or decode : "))
shift = shift%26
empty=[]
flag = 1
while(flag):
    print("1.Encode")
    print("2.Decode")
    print("3.Exit")
    choice = int(input("Enter your Option : "))
    if(choice == 1):    
        encode = input("Enter the password to encrypt : ")
        for i in encode:
            number=alphabet.find(i)
            number_shift=number+shift
            if number_shift>=25 :
                number_shift=number_shift-26
            outchar=alphabet[number_shift]
            empty.append(outchar)
            output="".join([str(j) for j in empty])
        print(output)
        output.replace(output,'')
    if(choice == 2):
        decode = input("Enter the encrypted code to decrypt : ")
        for i in decode:
            number=alphabet.find(i)
            number_shift=number-shift
            if number_shift>=25 :
                number_shift=number_shift-26
            outchar=alphabet[number_shift]
            empty.append(outchar)
            output="".join([str(j) for j in empty])
        print(output)
        output.replace(output,'')
    if(choice == 3):
        print("EXIT")
        flag = 0

