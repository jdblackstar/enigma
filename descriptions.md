# Ciphers

## ADFGVX Cipher

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

 2. Arrange keyword alphabetically by column index, with all letters below reamining attached

    A E G M N R
    X G D G G X
    G G D V D G

 3. Read off enciphered pairs, left to right, top to bottom (reading)

    XG DG GX GG DV DG -> a  t  t  a  c  k

## ADFGX Cipher

The key for an ADFGX cipher is a 'key square' and a keyword. Similar to ADFGVX, but 5x5 square instead of 6x6.

     A D F G X

 A   p h q g m
 D   e a y n o
 F   f d x k r
 G   c v s z w
 X   b u t i l
    

 Key word: GERMAN
 Word to encipher: attack

 1. Row index of letter, Column index of letter, written under key word left to right, top to bottom (reading)

    G E R M A N
    D D X F X F
    D D G A F G

 2. Arrange keyword alphabetically by column index, with all letters below reamining attached

    A E G M N R
    X D D F F X
    F D D A G G

 3. Read off enciphered pairs, left to right, top to bottom (reading)

    XD DF FX FD DA GG -> a  t  t  a  c  k

## Affine Cipher

The key for an Affine cipher consists of 2 numbers (a and b), and assumes a 26 letter alphabet (m = 26). a should be relatively prime to m i.e. a = 15, m = 26. 

1. Convert all the letters to numbers (a=0, b=1, ..., z=25)

2. Let c be the ciphertext letter (output letter) and let p be the number representing a letter

   encrypt:
   c = ap + b (mod m), 1<=a<=m, 1<=b<=m

   decrypt:
   p = a^-1(c - b) (mod m)

   find a^-1 by:
   ax = 1 (mod m)  \  I think this can also be done by m - a

3. encrypt: 'defend', key: a = 5, b = 7, m = 26 (Roman alphabet)
   
   - d -> 3
   - c = (5 * p + 7) (mod 26)
   - c = (5 * 3 + 7) (mod 26)
   - c = 22 (mod 26)
   - c = 22
   - d(3) becomes w(22)

4. decrypt: 'wbgbuwy', inverse of a: m - a (mod 26), 26 - 5 (mod 26), 21

   - p = 21 (c - 7) (mod 26)  \  remember that b is still 7
   - p - 21 (22 - 7) (mod 26)  \  plug in numberic value for w(22)
   - p = 315 (mod 26)
   - p = 3
   - w(22) becomes d(3)

## Atbash Cipher

The key for atbash is essentially to swap a letter with it's inverse i.e. A becomes Z, B becomes X, etc.

1. ABCDEFGHIJKLMNOPQRSTUVWXYZ
   ZYXWVUTSRQPONMLKJIHGFEDCBA

2. Encrypt: y = 27 - x, where x is a letter of the message to encrypt and y is a letter of the encrypted message.

3. Decrypt: x = 27 - y, where x is a letter of the message to encrypt and y is a letter of the encrypted message.

## Autokey Cipher

The key is a keyword. e.g. 'FORTIFICATION'

1. Uses tabula recta, below:
   

       A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
       ---------------------------------------------------
   A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
   B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
   C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
   D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
   E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
   F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
   G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
   H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
   I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
   J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
   K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
   L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
   M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
   N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
   O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
   P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
   Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
   R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
   S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
   T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
   U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
   V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
   W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
   X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
   Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
   Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

   2. To encipher a message, place the keyword above the plaintext. Once all of the key character have been written, start writing the plaintext as the ley:

   FORTIFICATIONDEFENDTHEEASTWA   <- Keyword, then phrase to encrypt
   DEFENDTHEEASTWALLOFTHECASTLE   <- Phrase to encrypt

   - Find the first letter to encrypt (D, bottom row)
   - Fine the first letter in keyphrase (F, top row)
   - with D as the row, and F as the column, find the intersection (I)
   - D becomes I

## Baconian Cipher

There is no key for this cipher. Instead, each letter is assigned a sequence of 5 characters. A binary system.

1. Encoding table:

   A = aaaaa  I/J = abaaa    R = baaaa
   B = aaaab    K = abaab    S = baaab
   C = aaaba    L = ababa    T = baaba
   D = aaabb    M = ababb  U/V = baabb
   E = aabaa    N = abbaa    W = babaa
   F = aabab    O = abbab    X = babab
   G = aabba    P = abbba    Y = babba
   H = aabbb    Q = abbbb    Z = babbb

2. Encode: "STRIKE NOW"

   S     T     R     I     K     E     N     O     W 
   baaab baaba baaaa abaaa abaab aabaa abbaa abbab babaa

   Hold OFf uNtIl you hEar frOm mE agAin. wE May cOMpROmIse.

   Capital letter in encoding message indicates a 'b' in the decoded message

## Base64 Cipher
## Beaufort Cipher
## Bifid Cipher
## Caesar Cipher
## Codes and Nomenclators Cipher
## Columnar Transposition Cipher
## Enigma Cipher
## Four-Square Cipher
## Fractionated Morse Cipher
## Hill Cipher
## Homophonic Substitution Cipher
## Lorenz Cipher
## Playfair Cipher
## Polybius Square Cipher
## Porta Cipher
## ROT13 Cipher
## Rail-fence Cipher
## Running Key Cipher
## Simple Substitution Cipher
## Straddle Checkerboard Cipher
## Trifid Cipher
## Vigenere and Gronsfeld Cipher
