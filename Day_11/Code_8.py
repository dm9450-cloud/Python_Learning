# WAP to print the multiplication table of a number n.

num = int(input("Enter your number: "));

i = 1;
while i <= 10:
    print(num, " * ", i , " == ", num * i );
    i += 1;
