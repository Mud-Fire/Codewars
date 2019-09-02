def create_phone_number(n):
    # your code here
    phone_str = '('
    for i in range(3):
        phone_str += str(n[i])
    phone_str += ') '
    for i in range(3, 6):
        phone_str += str(n[i])
    phone_str += '-'
    for i in range(6, 10):
        phone_str += str(n[i])
    return phone_str
