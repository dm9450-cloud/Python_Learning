# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (you can take help of built-in data type)


values = {9, 9.0, 8, 8.0}
print(values);     #{9, 8}

values2 = {9, "9.0"};
print(values2);

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values);