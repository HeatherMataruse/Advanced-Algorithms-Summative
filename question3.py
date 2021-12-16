#by Heather Mataruse

my_key =3
plain_text = 'Plain text'

def encrypted_text(plain_text,my_key):
    encryptedtext = ""
    counter = 0
    while start < my_key:
        for i in range(counter,len(plain_text),my_key):
            encryptedtext += plain_text[i]
        counter += 1

    return encryptedtext

encrypted = encrypted_text(plain_text,my_key)


# this if the functin that will handle the decryption
def decrypted_text(encrypted,my_key):
    counter= 0
    decryptedtext = ""
    #here is where i checked for the modulus 
    if len(encrypted) % 2 == 0 and my_key % 2 == 0: 
        # here i did floor division 
        x = len(encrypted)//my_key
        
        while counter < x:
            
            #here I looped to check the length of the text 
            for i in range(counter,len(encrypted),x):
                 decryptedtext += encrypted[i]
            counter+=1 
    if len(encrypted) % 2 == 0 and my_key % 2 != 0:
        # here i did floor division 
        x = len(encrypted)//my_key 
        
        while counter < x:
            x += 1
             decryptedtext += encrypted[counter] 

            for i in range(counter,len(encrypted)):
                t = i + x 
                 decryptedtext += encrypted[t]
                 decryptedtext += encrypted[t+my_key
                break
            # here i did floor division     
            x = len(encrypted)//my_key
            counter+=1 
         decryptedtext+= encrypted[x]

    return  decryptedtext
decrypted = decrypted_text(encrypted,my_key)

print("Plain text : " + plain_text)
print("Encrypted text: "+ encrypted)
print("Decryption text: "+ decrypted)
