# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    rinda = input()
    if "F" in rinda:
        fileName = "06"
        file = "./tests/"+fileName
        with open(file,"r") as f:
            pattern = f.readline()
            text = f.readline()
    elif "I" in rinda:
        pattern = input()
        text = input()
        
    else:
        print("kļūda")
        return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (text.rstrip(), pattern.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    q=101
    d=256
    res = []
    
    p = 0 # pattern hash
    t = 0 #txt hash value
    A = len(text)
    Z = len(pattern)
    h = 1
    if A<Z:
        return [] 
    for i in range(Z-1):
        h = (h*d) % q
    for i in range(Z):
        p = (d * p + ord(pattern[i])) % q
        t = (d*p + ord(text[i])) % q
    for i in range (A-Z+1):
        if p==t:
            for j in range(Z):
                if text[i+j] != pattern[j]:
                    break
                else:
                    res.append(i)
        if A-Z > i:
            t=(d*(t-ord(text[i])*h)+ord(text[i+Z]))% q
            if t<0:
                t=t+q
    return res




    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

