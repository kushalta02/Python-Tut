def conform(user_id,password):

    pass_store =[]
    val=list(dict1.values())

    for i in range(0,len(val)):
        pass_store.append(val[i][0])
    if user_id in dict1.keys() and password in pass_store:
        
        confirmation=input("  ")
        if confirmation == "YES" or  confirmation==" yes":