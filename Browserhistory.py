#importing queue
from queue import LifoQueue
Backward_History = LifoQueue()
forward_History = LifoQueue()
current_page = None

#Visit function
NoOfvisit=int(input("PLease Enter the Number of URL History"))

print("Enter the URLs to visit:")
for i in range(NoOfvisit):
    Url = input("Url:")
    print(f"Visiting your site{Url}")
    Backward_History.put (current_page)
    current_page= Url
    print(f"current_page:{current_page}")
#go back
while input("Do you want to return(Yes/No):").lower() =="Yes" :
    if not Backward_History.empty():
        forward_History.put(current_page)
        current_page=Backward_History.get()
        print(f"going back to {current_page}")
    else:
        print("No previous page found!!")
#go forward
while input("Do you want to go forward(Yes/No):").lower() =="Yes" :
    if not forward_History.empty():
        Backward_History.put(current_page)
        current_page=forward_History.get()
        print(f"going back to {current_page}")
    else:
        print("No previous page found!!")
        