str="P@#yn26at^&i5ve"
char=digit=symbol=0
character=['P','y','n','a','t','i','v','e']
digits=['2','6','5']
symbols=['@','#','^','&']
for i in str:


    if i in character:
     char=char+1
    elif i in digits:
     digit=digit+1
    else:
     symbol=symbol+1
print("char =",char)
print("digit =",digit)
print("symbol =",symbol)

    