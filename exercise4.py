print("""       ______________________________________________________________________________
               <<<<   Welcome to Your Multiplication Table!!  >>>>>>>>
      *Unlock the power of multiplication effortlessly with our user-friendly software 
                    - making learning fun, one table at a time!
_________________________________________________________________________________________""")

def table_1(no_1, no_2):
    print(f"Multiplication table for {no_1} up to {no_2}:")
    for i in range(1, no_2 + 1):
        print(f"{no_1} x {i} = {no_2 * i}")


def main():
    no_1=int(input("Enter the Number which you want the multiplication table:>>>>>"))
    no_2=int(input("Enter the limit upto which you want the multiplication table generated:>>>>>"))
    table_1(no_1 , no_2)
main()
print("""______________________________________________________________________
                      THANK YOU FOR USING!!!!""")
