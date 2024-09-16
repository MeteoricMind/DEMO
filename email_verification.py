email = "aritra@gmail.com"
j = 0
if len(email) >6:
    if "@" in email and email.count("@")==1 and "." in email and email.count(".")==1:
        if email[-4]==".":
            if email.isspace() == False:
                    if email.isalpha() == False:
                        for i in email:
                            if (i.isdigit() and i=="@" and i=="."):
                                j=j+1
                                continue
                            elif (i.isupper()==False):
                                j=j+1
                                continue
                            else:
                                print("not Valid")
                                break
                        if j == len(email):
                            print("Valid")
                            
                        
    else:
        print("Not valid")                      
else:
    print("Not valid") 

