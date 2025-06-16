#Program to assign   grades on  the basis of marks obtained
raw_data=int(input(" Enter the marks of the student : "))
if raw_data>90 and raw_data<=100:
    print(raw_data," Grade - A")
elif raw_data>76 and raw_data<=90:
    print(raw_data," Grade - B")
elif raw_data >61 and raw_data<=75:
    print(raw_data," Grade  -C")
elif raw_data>41 and raw_data<=60:
    print(raw_data," Grade - D")
else :
    print(raw_data," Grade  - E")
