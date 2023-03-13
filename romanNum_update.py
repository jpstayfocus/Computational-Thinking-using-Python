# Author : Jephté Pierre
# Date : March 13, 2023

# Function roman takes in parameter an integer n (number) and makes
# the conversion of this integer into a roman numeral
# for example, assert romain(439) must return the text "CDXXXIX"


def romain(number):
    
    start = 1
    roman=""
    
    while(number>0):
        i = number%10
        if(start==1):
            lastRom = chiffreRomain (i, "I", "V", "X") # 0-9
        elif (start==10):
            lastRom = chiffreRomain (i, "X", "L", "C")  # 10-99  
        elif (start==100):
            lastRom = chiffreRomain (i, "C", "D", "M") # 100-999
    
#1000, 2000, 3000 due to the condition imposed by the assignment

        else:
            lastRom = chiffreRomain (i, "M", "M", "M") 
        
        roman  = lastRom+roman # pre addition
        number//= 10 # drop the last digit
        start *= 10 # move to next digit

    return roman
    
def repeter (number, text):
    c = "" # empty string
    
    for i in range (1, number + 1):
        c += text # append a character to the string for each loop
    return c # return the new string
    
def extraireChiffre(number, power):
    
    number = number // power    
    return number % 10 # return last digit

def chiffreRomain(number, x, y, z):
    
    num = "" # variable that will contain the roman numeral
    
    if (x=="I" and y=="V" and z=="X"):          # unit
        if (number>=0 and number<=3):
            num+= repeter(number, "I")  
        elif (number==4):
            num+="IV"
        elif (number>=5 and number<=8):
            num+="V"
            c = repeter(number - 5, "I")
            num+= c
        else:
            num+="IX"
            
    elif (x == "X" and y == "L" and z == "C"):   # tens
        if (number >= 0 and number <= 3):
            num += repeter (number, "X")  
        elif (number == 4):
            num += "XL"
        elif (number >= 5 and number <= 8):
            num += "L"
            c = repeter (number - 5, "X")
            num += c
        else:
            num +="XC"      
    
    elif (x == "C" and y == "D" and z == "M"):   # hundreds
        if (number >= 0 and number <= 3 ):
            num += repeter (number, "C")
        elif (number == 4):
            num += "CD"
        elif (number >= 5 and number <= 8):
            num += "D"
            c = repeter (number - 5, "C")
            num += c
        else:
            num += "CM"
    else: # thousands
        num += repeter (number, "M")
    return num # return roman numeral


def testRomain() : # tests unitaires
    assert repeter(3, "I") == "III"
    assert extraireChiffre (1234, 100) == 2
    assert chiffreRomain(9, "I", "V", "X") == "IX"
    assert chiffreRomain(8, "I", "V", "X") == "VIII"
    assert romain(439) == "CDXXXIX"
    assert romain(2948) == "MMCMXLVIII"

testRomain()


