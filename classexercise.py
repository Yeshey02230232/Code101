def revo_name(s):
    if len(s) <= 1:
        return s
    else:
        return revo_name(s[1:])+ s[0]    
s=input("Enter a word---->>>")
print("orginal name",s )
print(revo_name(s))