s = input("Enter A String To Be Reversed : ")
reversed_str = ''
for i in range(len(s) - 1, -1, -1):
    reversed_str += s[i]    
print("String reversed using Iterative Method : ", reversed_str)


# Recursive Method
if s == "":
    reversed_str =""
else:
    reverse_str = (s[1:]) + s[0]
print("String reversed using Recursive Method : ",reversed_str)