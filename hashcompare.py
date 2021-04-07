import hashlib

file1 = 'file1.txt'
file2 = 'file2.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'Arquivo {file1} é diferente do {file2}')
    print(f'O hash do {file1} é: ', hash1.hexdigest())
    print(f'O hash do {file2} é: ', hash2.hexdigest())
else:
    print(f'Arquivo {file1} é igual ao {file2}')
    print(f'O hash do {file1} é: ', hash1.hexdigest())
    print(f'O hash do {file2} é: ', hash2.hexdigest())
