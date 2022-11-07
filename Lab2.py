import hashlib
import random
from random import choice
from string import ascii_lowercase

# Function that handles the hashing of any input and truncates it into an int of "size" number of bits
def hasher(input, size):
    hash = hashlib.sha1(input.encode())
    my_hexdata = hash.hexdigest()
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    hashBin = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    hashBinInt = int(hashBin, 2)

    return hashBinInt >> (160 - size)

# Function that handles that Pre-image attacks
def preimage(num):
    results = []
    for i in range(50):
        word = genRandWord(random.randint(1,55))

        goal = hasher(word, num)
        counter = 1
        isTrue = True
        while isTrue:
            valWord = genRandWord(random.randint(1,55))
            if valWord == word:
                continue
            val = hasher(valWord, num)
            if val == goal:
                isTrue = False
            else:
                counter = counter + 1
        results.append(counter)
    return results

# Function that handles the collision attacks
def collision(num):
    results = []
    for i in range(50):
        dict = {}
        wordOne = genRandWord(100)
        # wordOne = genRandWord(random.randint(1,55))
        wordOneHash = hasher(wordOne, num)
        dict.update({wordOneHash : wordOne})
        isTrue = True
        counter = 1
        while isTrue:
            valWord = genRandWord(100)
            # valWord = genRandWord(random.randint(1,55))
            if valWord == wordOne:
                continue
            val = hasher(valWord, num)
            if val in dict.keys():
                isTrue = False
            else:
                dict.update({val : valWord})
                counter = counter + 1
        results.append(counter)
    return results

# Function to create random word of "length" length
def genRandWord(length):
    return "".join(choice(ascii_lowercase) for i in range(length))

# This section is for Primage Attacks

# bitSize = 18
# print(str(bitSize) + " bitSize: Preimage")
# res = preimage(bitSize)
# print(res)
# average = sum(res)/len(res)
# print("Average value of preimage = " + str(average))

# This section is for Collision Attacks

bitSize = 18
print(str(bitSize) + " bitSize: Collision")
res = collision(bitSize)
print(res)
average = sum(res)/len(res)
print("Average value of Collision = " + str(average))
