def my_range (start,end):
    cat=[]
    while start < end:   
        cat.append (start)
        start = start+1
    return cat 
print (my_range (1,8))