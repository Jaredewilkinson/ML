def input_output():
    """
    This function reads in text files line by line.
    
    'r' = read mode.
    'w' = open clear contents write.
    'a' = open append to existing contents.
    'rt' = open in read and text mode.
    'wt' = open in write and text mode.
    'rb' = open in read and binary.
    'wb' = open in write and binary.
    """
    x = str(input("Enter file path name."))
    y = str(input("Enter in read argument (r,w,a). "))
    f= open(x, y)
    for line in f:
        print(line.rstrip())# strips newlines from end of line.