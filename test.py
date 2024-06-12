import bcrypt

print(bcrypt.hashpw('1'.encode(), bcrypt.gensalt()))