def order_weight(input_list):
    arr = input_list.split()
    arr.sort()
    arr.sort(key=order_logic)
    return ''.join(str(e)+' ' for e in arr).rstrip()

def order_logic(num_str):
    z=0
    for y in num_str:
        z += int(y)
    return z