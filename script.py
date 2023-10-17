from CodeCipher import caesar_decode
from CodeCipher import caesar_encode

# ---- Testing Lines ----
message1 = """
xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek 
qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
"""

message2 = """
Hello again friend! I knew you would love the Caesar Cipher, it's a cool, 
simple way to encrypt messages. Did you know that back in Caesar's time, 
it was considered a very secure way of communication and it took a lot of 
effort to crack if you were unaware of the value of the shift? That's all 
changed with computers! Now we can brute force these kinds of ciphers very 
quickly, as I'm sure you can imagine.
"""

message3 = """
Hzggj vbvdi amdziy! I fizr tjp rjpgy gjqz ocz Cvznvm Cdkczm, do'n v xjjg, 
ndhkgz rvt oj zixmtko hznnvbzn. Ddy tjp fijr ocvo wvxf di Cvznvm'n odhz, 
do rvn xjindyzmzy v qzmt nzxpmz rvt ja xjhhpidxvodji viy do ojjf v gjo ja 
zaajmo oj xmvxf da tjp rzmz pivrvmz ja ocz qvgpz ja ocz ncdao? Tcvo'n vgg 
xcvibzy rdoc xjhkpozmn! Njr rz xvi wmpoz ajmxz ocznz fdiyn ja xdkczmn qzmt 
lpdxfgt, vn I'h npmz tjp xvi dhvbdiz.
"""

# ---- Testing function ----
decoded_message = caesar_decode(message1, 10)
print(f'\nDecoding Message1:\n{decoded_message}')

encoded_message = caesar_encode(message2, 5)
print(f'\nEncoding Message2:\n{encoded_message}')

decoded_message = caesar_decode(message3, 5)
print(f'\nDecoding Message3:\n{decoded_message}')

decoded_message = caesar_decode(caesar_encode(message2, 5), 5)
print(f'\nDecoding Message Encoded:\n{decoded_message}')
