
def encryption(word,shift):

    result=""
    word=str(word).lower()
    for i in word:
        if i.isalpha(): #only work on alphabet letter, else will add blank to the index
            base=ord(i)
            shifted=ord(i)+shift #shift all letter to the right by the key value
            if shifted > 122:
                shifted=shifted-26 #keeps the ASCII value within lower case range
            result+=chr(shifted)
        else:
            result+=i
    print(result)
    return result

def decryption(word,shift):

    result=""
    word=str(word).lower()
    for i in word:
        if i.isalpha(): #only work on alphabet letter, else will add blank to the index
            base=ord(i)
            shifted=base-shift #shitf all letters to the left by the key value
            if shifted < 97:
                shifted=shifted+26 #keeps the ASCII value within lower case range
            result+=chr(shifted)
        else:
            result+=i
    print(result)
    return result

temp=encryption("gfiohusdhfslduhasdfkjhsdflusdfsfdsfd",3)

decryption(temp,3)

