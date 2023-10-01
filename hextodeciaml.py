# we use ord() functiion to get teh assci value of a charcter

def hextodecimal(hexadeciaml):
    deciaml = 0
    for i in hexadeciaml:
        if '0'<=i<='9':
            deciaml = deciaml * 16 + (ord(i) - ord('0'))
        elif 'A'<=i<='F':
            deciaml = deciaml * 16 + (ord(i) - ord('A') + 10)
        else:
            return None
    return deciaml



def hextobinary(hexadeciaml):
    deciaml = hextodecimal(hexadeciaml)
    if deciaml is not None:
        list = []
        while deciaml >= 1:
            x = int (deciaml) % 2
            deciaml = deciaml / 2
            list.append(x)
        list.reverse()
        binary = "".join(map(str,list))
        return binary
    else:
        return None



def hextooctal(hexadecimal):
    decimal = hextodecimal(hexadecimal)
    if decimal is not None:
        list = []
        while decimal >= 1:
            x = int(decimal) % 8
            decimal = decimal / 8
            list.append(x)
        list.reverse()
        octal = "".join(map(str,list))
        return octal
    else:
        return None
hexadeciaml = input("Enter the Hexadecimal : ")
print('''In what do you want ot change : 
      1 = In Decimal
      2 = In binary
      3 = In Octal
      Choose one : ''')
userinput = int(input())
match userinput:
    case 1:
        result = hextodecimal(hexadeciaml)
        if result is not None:
            print(f"The decimal value : {result}")
        else:
            print("Invalid input")
    case 2:
        result2 = hextobinary(hexadeciaml)
        if result2 is not None:
            print(f"The octal value : {result2}")
        else:
            print("Invalid input")
    case 3:
        result3 = hextooctal(hexadeciaml)
        if result3 is not None:
            print(f"The octal value :")
        else:
            print("Invalid input")
