# enigma
Methods and Functions for encoding/decoding messages with a variety of ciphers.

## Ciphers

### ADFGVX Cipher

The key for an ADFGVX cipher is a 'key square' and a keyword.

     A D F G V X

 A   p h 0 q g 6
 D   4 m e a 1 y
 F   l 2 n o f d
 G   x k r 3 c v
 V   s 5 z w 7 b
 X   j 9 u t i 8

 Key word: GERMAN
 Word to encipher: attack

 1. Row index of letter, Column index of letter, written under key word left to right, top to bottom (reading)

    G E R M A N
    D G X G X G
    D G G V G D

 2. Arrange key word alphabetically by column index, with all letter below attached

    A E G M N R
    X G D G G X
    G G D V D G

 3. Read off enciphered pairs, left to right - top to bottom

    XG DG GX GG DV DG -> a  t  t  a  c  k
### ADFGX Cipher
### Affine Cipher
### Atbash Cipher
### Autokey Cipher
### Baconian Cipher
### Base64 Cipher
### Beaufort Cipher
### Bifid Cipher
### Caesar Cipher
### Codes and Nomenclators Cipher
### Columnar Transposition Cipher
### Enigma Cipher
### Four-Square Cipher
### Fractionated Morse Cipher
### Hill Cipher
### Homophonic Substitution Cipher
### Lorenz Cipher
### Playfair Cipher
### Polybius Square Cipher
### Porta Cipher
### ROT13 Cipher
### Rail-fence Cipher
### Running Key Cipher
### Simple Substitution Cipher
### Straddle Checkerboard Cipher
### Trifid Cipher
### Vigenere and Gronsfeld Cipher
