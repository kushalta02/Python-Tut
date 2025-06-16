def delete_Char(raw_str,raw_char):
    raw_del = ""
    for ch in raw_str:
        if ch!=raw_char:
            raw_del+=ch
    
    return raw_del


raw_str=input("Enter a string ")
raw_char=input("Enter character you want to delete -")

dele_char = delete_Char(raw_str,raw_char)
print(dele_char)

