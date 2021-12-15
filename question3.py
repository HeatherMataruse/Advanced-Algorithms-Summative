#by Heather Mataruse


text = 'Plain text'
key = 3
def encryption(text,key):
    encrypted_message = ""
    start = 0
    while start < key:
        for j in range(start,len(text),key):
            encrypted_message += text[j]
        start += 1

    return encrypted_message

encrypted = encryption(text,key)


# this if the functin that will handle the decryption
def decryption(encrypted,key):
    a = 0
    decrypted_message = ""
    #here is where i checked for the modulus 
    if len(encrypted) % 2 == 0 and key % 2 == 0: 
        # here i did floor division 
        b = len(encrypted)//key 
        
        while a < b:
            
            #here I looped to check the length of the text 
            for i in range(a,len(encrypted),b):
                decrypted_message += encrypted[i]
            a+=1 
    if len(encrypted) % 2 == 0 and key % 2 != 0:
        # here i did floor division 
        b = len(encrypted)//key 
        
        while a < b:
            b += 1
            decrypted_message += encrypted[a] 

            for i in range(a,len(encrypted)):
                c = i + b 
                decrypted_message += encrypted[c]
                decrypted_message += encrypted[c+key]
                break
            # here i did floor division     
            b = len(encrypted)//key 
            a+=1 
        decrypted_message+= encrypted[b]

    return decrypted_message
decrypted = decryption(encrypted,key)

print("Plain text : " + text)
print("Encrypted text: "+ encrypted)
print("Decryption text: "+ decrypted)
