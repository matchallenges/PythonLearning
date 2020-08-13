#f = open('text1.txt', 'r') # can only use one mode

#for line in f.readline():
    #print(line, end='')

#print(list(f.read()))

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
#f.close()

f = open('text1.txt', 'rb+') 

f.write(b'0123456789a1bcdef')
print(f.read())