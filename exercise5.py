print("""________________________________________________________________________________________
               <<<<<<<   Welcome to Your star custimise !!  >>>>>>>>
                *Unleash the cosmos from your command 
      – let our star generating software ignite your imagination with celestial brilliance.
_________________________________________________________________________________________""")

def star_(h_, r_):
    print(f"              Your star triangle of height:{h_} and row:{r_} :")
    for i in range(1, r_ + 1):
        print("*" * i)


def main():
    h_=int(input("            Enter the height of your star triangle :>>>>>"))
    r_=int(input("            Enter the row of your star triangle :>>>>>"))
    star_(h_ , r_)
main()
print("""______________________________________________________________________________________
                                   THANK YOU FOR USING!!!!""")
