single_digits = ["Zero ", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "] 
double_digits = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
tens_multiple = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
tens_power = ["Hundred", "Thousand"]
inp=input("Enter the number:")
l=len(inp)  
s=list(inp)
n=int(inp)
for i in range(4-l):
    s.insert(i,"0")
word=''
if(n==0):
    print("Zero")
else:
    for i in range(4):
        num=int(s[i])
        if i==0 and num!=0:
            word =word+single_digits[num]+tens_power[1]+' '
        elif i==1 and num!=0:
            word =word+single_digits[num]+tens_power[0]+' And '
        elif i==2 and num==1 and num!=0:
            word=word+double_digits[int(s[i+1])]+' '
            break
        elif i==2 and num!=1 and num!=0:
            word=word+tens_multiple[num-2]+' '
        elif i==3 and num!=0:
            word=word+single_digits[num]+' '

    print(word)
