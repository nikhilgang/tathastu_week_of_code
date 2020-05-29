#program 2 of DAY 3

def permutation(List, String = ""):
    Set = set(List)
    stringList = []
    if len(Set) == 1:
        String += "".join(List)
        return list([String])
    for x in Set:
        List1 = list(List)
        S = String + x
        List1.remove(x)
        stringList.extend(permutation(List1, S))
    return stringList

string = list(input("Enter a string: \n"))
List = permutation(string)
print("\nAll the permutation of given string is: \n\n" + ", ".join(List))
