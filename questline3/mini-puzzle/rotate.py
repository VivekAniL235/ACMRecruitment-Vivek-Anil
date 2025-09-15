binary_string=input('enter the binary string')
k=int(input('enter the no of times to be rotated'))

def rotate_and_convert(binary_string, k):
    n = len(binary_string)
    k2 = k % n # gives effective k value (when n>k)
    rotated_string = binary_string[k2:] + binary_string[:k2]
    decimal_value = int(rotated_string, 2) #converts binary value in str to decimal
    print(decimal_value)
rotate_and_convert(binary_string, k)    
