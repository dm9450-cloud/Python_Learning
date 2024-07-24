student = {
    "name" : "Dipanshu",
    "subjects " : {
        "phy" : 95,
        "chem" :85,
        "math" : 98
    }
}

pairs = list(student.items());
print(pairs[0]);
print(pairs[1]);


print(student["name"]);
# print(student["name2"]);     #error
print(student.get("name"));
# print(student.get("name2"));    #no error --- None


