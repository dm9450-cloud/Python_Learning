# WAP to print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
# len(nums)   --> 10, 9 


# index = 0, 1, 2, 3, 4, 5, ----------, len(list)-1;
idx = 0;
# while idx <= len(list)-1:    #while ids <len(list)

while idx < len(nums):

    # print(idx);
    print(nums[idx])    #num[0], num[1], num[2].....
    idx +=1;