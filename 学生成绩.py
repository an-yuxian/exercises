
zero_to_twelve = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
 
prefixes= ['','','twen', 'thir', 'for','fif','six','seven','eigh','nine']


# 

k = int(0)
userinput = input()
def single_digit(english, wordlist):    # a function to extract the single digits. like 9 in 19, 4 in 40 etc. 
    c = ''
    for i in range(len(wordlist)):
        if wordlist[i]==english:
            c =i 
    return c

def english2num(english):
   
    if english in zero_to_twelve:
        return single_digit(english, zero_to_twelve) #check if the word in 0-12. If so, return the number directly.
   

    elif english[-4:]=='teen':
        number='1'+str(single_digit(english[0:-4], prefixes)) #19, 14, etc.
        return number

    elif 'ty' in english and 'teen' not in english: 
        k =0
        k =int(k)
        for i in range(len(english)):
            if english[i-1]+english[i]=="ty":
                k = i-1
                break
        if k ==0:
            return "Please enter a cardinal word."
            break

        print(english[k], english[k+1]) #find consecutive "t" and "y". 
        number= str(single_digit(english[0:k], prefixes))+str(single_digit(english[k+3:], zero_to_twelve))
        return number
    
    elif english=='hundred':
        return '100'
    
    else:
        return 'Please enter a cardinal word.'

print(english2num(userinput))














