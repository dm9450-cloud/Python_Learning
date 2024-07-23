# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method);

# A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
# [1, 2, 3, 2, 1]     [1, "abc", "abc", 1]
#        | copy
#   [1, 2, 3, 2, 1]-----reverse----[1, 2, 3, 2, 1]

# list1 = [1, 2, 1];          ["m", "a", "a", "m", "p"];
list2 = [1, 2, 3];

copy_list1 = list1.copy();
copy_list1.reverse();

if(copy_list1 == list1):
    print("Palindrome");
else:
    print("Not Palindrome");



