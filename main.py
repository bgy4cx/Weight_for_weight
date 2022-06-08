def order_weight(input_list):
    arr = input_list.split()
    # The below sort is needed because we have to order the numbers with alphabetical ordering as well. It is easier in the begining. 
    arr.sort()
    # The ording with the requested conditions
    arr.sort(key=order_logic)
    # In the return statement the code converts the list variable to string. 
    return ''.join(str(e)+' ' for e in arr).rstrip()

def order_logic(num_str):
    z=0
    for y in num_str:
        z += int(y)
    return z