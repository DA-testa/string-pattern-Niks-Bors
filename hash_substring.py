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
    return (text.rstrip(), pattern.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    
    p = 31
    m = 10**9 + 9
    
    n = len(text)
    k = len(pattern)
    
    power_of_p = [1]
    for i in range(1, k):
        power_of_p.append((power_of_p[-1] * p) % m)
        
    pattern_hash = 0
    for i in range(k):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * power_of_p[k-i-1]) % m
        
    text_hash = [0] * (n - k + 1)
    text_hash[0] = 0
    for i in range(k):
        text_hash[0] = (text_hash[0] + (ord(text[i]) - ord('a') + 1) * power_of_p[k-i-1]) % m
        
    for i in range(1, n - k + 1):
        text_hash[i] = (text_hash[i-1] - (ord(text[i-1]) - ord('a') + 1) * power_of_p[k-1] + m) % m
        text_hash[i] = (text_hash[i] * p + (ord(text[i+k-1]) - ord('a') + 1)) % m
    
    occurrences = []
    for i in range(n - k + 1):
        if pattern_hash == text_hash[i]:
            if text[i:i+k] == pattern:
                occurrences.append(i)
    
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

            
            if t<0:
                t=t+q
    return res




    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    


# this part launches the functions
if __name__ == '__main__':
    input_data=read_input()
    if input_data:
        print_occurrences(get_occurrences(*input_data))
   

