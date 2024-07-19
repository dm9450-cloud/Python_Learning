# WAP to find the greatest of 3 numbers entered by the user. 


num1 = int(input("Enter first number: "));
num2 = int(input("Enter Second number : "));
num3 = int(input("Enter third number"));
 
if(num1>=num2 and num1>=num3):
    print("First number is greatest number : ",num1);
elif(num2>=num1 and num2>=num3):
    print("Second number is greatest number :", num2);
else:
    print("Third number is greatest number :", num3);
