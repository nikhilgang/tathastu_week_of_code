#program 4 of DAY 6

def next_greater(s):
    if s==sorted(s,reverse=True):
        return 'Already Largest'

    if s==sorted(s):
        s[len(s)-2],s[len(s)-1] =s[len(s)-1],s[len(s)-2]
        str_num = [str(i) for i in s]
        return int("".join(str_num))

        
    for i in range(len(s)-1,0,-1):
        if s[i]>s[i-1]:
            index=i-1
            break
    
    smallest_index = s.index(min(filter(lambda i: i> s[index],s[index+1:])))
    x=s.pop(smallest_index)

    s.insert(index,x)
    s[index+1:] =sorted(s[index+1:]) 
    str_num = [str(i) for i in s]
    return int("".join(str_num))



num = list(input('enter the number   :  '))
print("\nThe next possible greatest number is:",next_greater(num))
