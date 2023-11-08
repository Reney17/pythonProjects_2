import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$^&*()_+{}:\"<>?[];',./\\"
all_chars = lower + upper + numbers + symbols

#set the desired length of the password
length = 16 

password = ''.join(random.sample(all_chars, length))
print("Generated password:",  password)