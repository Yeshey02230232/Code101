print("Exercise>>3")
for num_ in range(1, 9):
    if num_==3:
        print(f"skipping{num_} in the inner loop")
        continue
    if num_==7:
        print(f"Reached {num_}, breaking outer loop")
        break
    else:
        print(num_)