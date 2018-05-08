from Crypto.Cipher import DES3
import base64
import hashlib

def unpad(s):
   """
   Unpad the string padded by the pad function
   """
   return s[:-ord(s[len(s)-1:])]

def pad(to_encrypt,block_size=8):
	modulo = len(to_encrypt) % block_size
	return to_encrypt + (block_size - modulo) * chr(block_size - modulo)

def decrypt(key,encrypted_string_2):
	cipher = DES3.new(key, DES3.MODE_ECB)
	encrypted_string = base64.b64decode(encrypted_string_2)
	decrypted_string = cipher.decrypt(encrypted_string)
	return unpad(decrypted_string)

def encrypt(key,to_encrypt):
	to_encrypt = pad(to_encrypt)
	print("to_encrypt====",to_encrypt)
	cipher = DES3.new(key,DES3.MODE_ECB)
	to_encrypt = to_encrypt.encode()
	encrypted_string = cipher.encrypt(to_encrypt)
	return encrypted_string

to_hash = "Khalti Encryption Key for Api"
md5_hashed = hashlib.md5(to_hash.encode())
md5_hashed = md5_hashed.digest()
key = md5_hashed
encrypted_string_1 = "ngE7eyP2zKzjA81R2i/AxSDYNQUi4pFFhX0EctPBSdXvFnDEgwX9/w=="
to_encrypt = 'Basic YWJpbkBqYW5ha2l0ZWNoLmNvbTptYW5mb3JkMTIz'

val=encrypt(key,to_encrypt)
encrypted_string_2 = base64.b64encode(val)
print(encrypted_string_2)
print("-----------------")

val =decrypt(key,encrypted_string_2)
print(val)
print(len(val))

