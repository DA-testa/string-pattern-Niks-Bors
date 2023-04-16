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
        
   
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

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
    if A<Z: #pārbauda vai teksts ir lielāks nekā pattern, ja ir, tad return
        return [] 
    
    for i in range(Z-1):
      h = (h*d) % q

    for i in range(Z):
      p = (q* p + ord(pattern[i])) % d
      t = (q*t + ord(text[i])) % d

    res = [] 
    i = 0
    while i <= A - Z:
      if hash(pattern) == hash(text[i : i + Z]):
          res.append(i)
      i += 1


      if i<A-Z:
        t=(q*(t-ord(text[i])*h)+ord(text[i+Z]))% d

        if t<0:
           t = t+d
    return res




    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable



# this part launches the functions
if name == 'main':
    print_occurrences(get_occurrences(read_input()))
   

