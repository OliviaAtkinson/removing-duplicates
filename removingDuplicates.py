with_duplicates = ["Olivia", "Ryan", 10 , 17, "Nathan", "Josh", "Ryan" , 10, 8,"Nathan"]

def without_duplicates(with_duplicates):
    new_array = []
    [new_array.append(word) for word in with_duplicates if word not in new_array]
    print (new_array)

without_duplicates(with_duplicates)