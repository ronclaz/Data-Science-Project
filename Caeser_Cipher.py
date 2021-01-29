def cCipher(stringText, shift):
    cCipherString = ''
    if type(stringText) is str:
        for i in stringText:
            cipher1 = ord(i) + shift
            #if cipher1 > ord('z'):
                #cipher1 = ord('z') - 24
            textConvert = chr(cipher1)
            cCipherString += textConvert
        #print("Your ciphertext is: ", cCipherString)
        return cCipherString
    else:
      return 'The input is not a string'
print(cCipher('abc', 1))
print(cCipher('123', 3))
print(cCipher(44, 3))
print(cCipher('143Hg!)>#', 2))
print(cCipher("Here's 2 U MRS Robinson", 1))
dir(str)
