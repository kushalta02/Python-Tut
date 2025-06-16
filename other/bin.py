"""
CREATE A BINARY FILE WITH ROLL NUMBER NAME AND MARKS
INPUT A ROLL NUMBER AND UPDATE MARKS.
"""
import pickle
#UDF FOR INSERTING DATA 
def sdata():
    f = open("student_data.dat","ab")
    r_no = int(input(" ENTER STUDENT ROLL NO-: "))
    name = input("ENTER STUDENT NAME :")
    marks = int(input("ENTER STUDENT MARKS:"))
    res={'Roll_no':r_no,'Sname':name,'Smarks':marks}
    pickle.dump(res,f)
    f.close()
#UDF FOR SEEKING ROLL NO AND UPDATING MARKS
def display():
    fn=open("student_data.dat","rb+")
    i=int(input(" ENTER ROLL NO "))
    f=0
    # USING TRY AND EXCEPT TO AVOID EOF ERROR  
    try:
        while True:
            #EXECUTE UNTILL REACH END
            te=fn.tell()
            print(" position",te)
            #TO KNOW POSITION 
            k=pickle.load(fn)

            if k["Roll_no"]==i:#CHECK ROLL NO
                n_mark=int(input(" ENTER NEW MARKS :"))
                k["Smarks"]=n_mark
                print(fn.seek(te))
                pickle.dump(k,fn)
                print(k)
                f=1
                break
                #BREAKING LOOP
    except EOFError :
        fn.close()
        if f==0:#IN CASE RECORD NOT FOUND
            print(" NO RECORD FOUND ")
#sdata()
display()