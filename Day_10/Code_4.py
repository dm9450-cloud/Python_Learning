collection = set();
collection.add(1);
collection.add(2);
collection.add("Dipanshu Maddheshiya");
collection.add((1, 2, 3));

# hashable--- immutable
# unhashable-- dict,list,set
collection.add[(1, 2, 3)];


print(collection);