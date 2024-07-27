# WAP to search for a number x in this tuple using loop:
    
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x =36;
i = 0;   #intialzation
while i < len(nums):
    # print(nums[i]);   
    if(nums[i] == x):
        print("Found at idx", i);
        break;
    else:
        print("Finding..")
    i += 1;

print("End of loop");
