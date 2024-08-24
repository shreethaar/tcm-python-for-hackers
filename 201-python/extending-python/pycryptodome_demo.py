from Crypto.Random import get_random_bytes
key=get_random_bytes(32)
print(key)
print(len(key))

from Crypto.Protocol.KDF import PBKDF2
salt=get_random_bytes(32)
password="hunter2"
key=PBKDF2(password,salt,dkLen=32)
print(key)
print(len(key))

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
to_encrypt=b"encrypt me!"
cipher=AES.new(key,AES.MODE_CBC)
print(cipher.iv)
ciphered_data=cipher.encrypt(pad(to_encrypt,AES.block_size))
print(ciphered_data)

cipher=AES.new(key,AES.MODE_CBC,iv=cipher.iv)
plaintext_data=unpad(cipher.decrypt(ciphered_data),AES.block_size)
print(plaintext_data)

from Crypto.Cipher import ARC4
cipher=ARC4.new(key)
encrypted=cipher.encrypt(to_encrypt)

cipher=ARC4.new(key)
plaintext=cipher.decrypt(encrypted)
print(plaintext)

from Crypto.PublicKey import RSA
key=RSA.generate(1024)
encrypted_key=key.exportKey(passphrase=password)
print(encrypted_key)
pub=key.publickey()
print(pub.exportKey())

print(key.can_encrypt())
print(key.can_sign())
print(key.has_private())
print(pub.has_private())

from Crypto.Cipher import PKCS1_OAEP
encrypted=cipher.encrypt(to_encrypt)
print(encrypted)

cipher=PKCS1_OAEP.new(key)
plaintext=cipher.decrypt(encrypted)
print(plaintext)

from Crypto.Hash import SHA512
plain_hash=SHA512.new(to_encrypt).digest()
hashed=int.from_bytes(plain_hash,byteorder='big')
print(hashed)

signature=pow(hashed,key.d,key.n)
print("signature: {}".format(signature))

signature_hash=pow(signature,key.e,key.n)
print(signature_hash)
print(hashed==signature_hash)
