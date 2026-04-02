def IsPalindrome(string):
    
    string = string.lower()

    punctuation = '''`~!@#$%^&*()-_=+[{]}\|:;"'<>,./? '''
     
    for x in string:
        if x in punctuation:
            string = string.replace(x, "")

    beg = 0
    end = len(string) - 1
    while(string[beg] == string[end] and beg < end): 
        beg+=1
        end-=1
    if beg == end or beg > end:
        return True
    else:
        return False

def main():
    cnt_palindrome = 0
    cnt_total = 0
    string = input('Enter a string to test, or "stop" to terminate\n')
    while string != 'stop':
        if IsPalindrome(string):
            print(string, 'is a palindrome')
            cnt_palindrome += 1
        else:
            print(string, 'is not a palindrome')
        cnt_total += 1
        string = input('Enter a string to test, or "stop" to terminate\n')
    print('Number of input strings:', cnt_total)
    print('Number of strings that are palindromes:', cnt_palindrome)
    print('Thank you for using this program')
        
main()
    
