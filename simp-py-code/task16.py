# Please write a program to generate all sentences where subjects is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey", "Football"]
# Hints: Use list[index] notation to get a element from a list
subject_list = ["I", "You"]
verb_list = ["Play", "Love"]
object_list = ["Hockey", "Football"]
for subject in subject_list:
    for verb in verb_list:
        for objec in object_list:
            print(subject +" " +verb +" "+ objec)