# Nested Dictionaries. 


# student = {
#     "name" : "Dipanshu",
#     "score" : {
#         "chem" : 98,
#         "phy" : 97,
#         "math" : 95
#     }
# }

# student["score"]["math"]

student = {
    "name" : "Dipanshu",
    "subjects " : {
        "phy" : 95,
        "chem" :85,
        "math" : 98
    }
}
print(student["subjects "]);
print(student["subjects "]["chem"]);
print(student);