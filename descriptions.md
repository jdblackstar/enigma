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

The key is a word. e.g. 'FORTIFICATION'

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

2. Encipher: similar to autokey, except you keep repeating the key intead of beginning to message to be encrypted

   FORTIFICATIONFORTIFICATIONFO   <- Keyword, repeated to be as long as the phrase
   DEFENDTHEEASTWALLOFTHECASTLE   <- Phrase to encrypt

   - Start in the column of the unciphered letter (D)
   - Go down until you find the matching keyword letter (F)
   - The enciphered letter will be the row index (C)

   Deciphering can be performed using the exact opposite steps (same algorithm)
   
## Bifid Cipher

Key is a 25 letter "key square". can write key as one line, 1st row - 2nd row - 3rd row, etc.

   1 2 3 4 5
1| p h q g m
2| e a y l n
3| o f d x k
4| r c v s z
5| w b u t i

1. Encryption: 

   - each letter is translated into it's row and column value, written as row *over* column
   - each chunk is divided into a repeating number of characters (the example is 5)
   - append bottom row onto top row, keep period seperation
   - each 2 letter pair corresponds to a row/column location for a letter (3,2 in example becomes f)

   plaintext:   defend the east wall of the castle

   step 1: row  323223 512 2245 5222 33 512 424522
           col  312153 421 1244 1244 12 421 224441
        
   step 2:      32322 35122 24552 22335 12424 522 
                31215 34211 24412 44124 21224 441 
             
   step 3:      3232231215 3512234211 2455224412 2233544124 1242421224 522441

   step 4:      f f y h m  k h y c p  l i a s h  a d t r l  h c c h l  b l r


## Caesar Cipher

Very simple, key is increase or decrease to each letter of the original message

1. Assign every letter a numerical value (A=0, B=1, ..., Z=25)
2. Let x be the message ,y be the enciphered letter, and k be the key

   y = x + k (mod 26)

   decryption algorithm:
   x = y - k (mod 26)

## Codes and Nomenclators Cipher
## Columnar Transposition Cipher
## Enigma Cipher
## Four-Square Cipher

They key for a Four-Square Cipher is 4 5x5 matricies that do not contain j (merged with i). The upper-left and lower-right matricies are plain alphabet matricies. The upper-right and lower-left matricies are the cipher matricies. The key matrix can be combined into one line by 'reading it like a book'.

   a b c d e   Z G P T F
   f g h i k   O I H M U
   l m n o p   W D R C N
   q r s t u   Y K E Q A
   v w x y z   X V S B L
    
   M F N B D   a b c d e
   C R H S A   f g h i k
   X Y O G V   l m n o p
   I T U E W   q r s t u
   L Q Z K P   v w x y z

1. Break up the message into bigrams. To encode ATTACK AT DAWN --> AT TA CK AT DA WN

2. Find the first bigram in the upper-left and lower-right matricies (alternate capitalization in each matrix)

   A b c d e   Z G P T F
   f g h i k   O I H M U
   l m n o p   W D R C N
   q r s t u   Y K E Q A
   v w x y z   X V S B L
 
   M F N B D   a b c d e
   C R H S A   f g h i k
   X Y O G V   l m n o p
   I T U E W   q r s T u
   L Q Z K P   v w x y z

3. Find the letters in the cipher matricies that make a rectangle with the new existing letters.

   a b c d e   Z G P T F
   f g h i k   O I H M U
   l m n o p   W D R C N
   q r s t u   Y K E Q A
   v w x y z   X V S B L
 
   M F N B D   a b c d e
   C R H S A   f g h i k
   X Y O G V   l m n o p
   I T U E W   q r s t u
   L Q Z K P   v w x y z

4. This means that the bigram AT becomes TI (upper-left becomes upper-right, lower-right becomes lower-left)

   ATTACKATDAWN
   TIYBFHTIZBSY

## Fractionated Morse Cipher

The key for a Fractionated Morse cipher is a mixed alphabet that both parties must know. e.g. "ROUNDTABLECFGHIJKMPQSVWXYZ". 26 letters

Morse Code:
A  .-    N  -.    .  .-.-.-  1  .----
B  -...  O  ---   ,  --..--  2  ..---
C  -.-.  P  .--.  :  ---...  3  ...--
D  -..   Q  --.-  "  .-..-.  4  ....-
E  .     R  .-.   '  .----.  5  .....
F  ..-.  S  ...   !  -.-.--  6  -....
G  --.   T  -     ?  ..--..  7  --...
H  ....  U  ..-   @  .--.-.  8  ---..
I  ..    V  ...-  -  -....-  9  ----.
J  .---  W  .--   ;  -.-.-.  0  -----
K  -.-   X  -..-  (  -.--.           
L  .-..  Y  -.--  )  -.--.-  end of character: x        
M  --    Z  --..  =  -...-   end of word: xx 

1. Turn plaintext into Morse code with "x" between characters and "xx" between words

   plaintext:  defend the east
   morse: -..x.x..-.x.x-.x-..xx-x....x.xx.x.-x...x-x

2. Encipher using the keyword and the following table

   R O U N D T A B L E C F G H I J K M P Q S V W X Y Z
   . . . . . . . . . - - - - - - - - - x x x x x x x x
   . . . - - - x x x . . . - - - x x x . . . - - - x x
   . - x . - x . - x . - x . - x . - x . - x . - x . -

3. Encipher each block of 3 characters, and you get: ESOAVVLJRSSTRX

## Hill Cipher

The key is any matrix (as long as it's square) We'll use a 3x3 for the example enciphering

   2  4  5
   9  2  1
   3 17  7

1. To encipher our message (ATTACK AT DAWN), we need to break it into chunks of 3, first chunk is ATT

2. Create a vector that corresponds to the letters: [0 19 19]

3. Vector multiplication:

   |2  4  5|  | 0|     |171|              |15|
   |9  2  1|  |19|  =  | 57| (mod 26)  =  | 5|  =  'PFO'
   |3 17  7|  |19|     |456|              |14|

4. Deciphering: need to find an inverse matrix (mod 26) to use as our key (take PFO back to ATT, find inverse of k)

   |2  4  5|
   |9  2  1| = k
   |3 17  7|

   |15|                   | 0|
   | 5| (k^-1) (mod 26) = |19| = 'ATT'
   |14|                   |19|

5. More maths

        K = key matrix
        d = determinant of K
        I = identity matrix
   adj(k) = adjugate matrix of k

   K * K^-1 = I (mod 26)


         ...to be continued



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
