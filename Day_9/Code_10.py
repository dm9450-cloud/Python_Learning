student = {
    "name" : "Dipanshu",
    "subjects " : {
        "phy" : 95,
        "chem" :85,
        "math" : 98
    }
}

# student.update({"City" : "Delhi"});
# print(student);

new_dict = {
    "name" : "Neha",
    "City" : "Delhi",
    "age" : 24
}

student.update(new_dict)

print(student);