# Caesar Cipher 

this is a typical substitution cipher and the rule is replace each of the alphabet with the latter standing k places further down the alphaber. 
the range of K is: 0 <= K <= 25
this repository holds:
* a enryption and decrytion implementation of this cipher 
* a ciphertext only attack
* a known plaintext attack

in the ciphertext only attack I used the `textblob` library to see if the language can be detected as English because if it can it probably means that we found the correct key. 