'''
Project 6: Hashing and Caching
Author: Christian Alexander
Created: 11/22/21
Course: CS2420
Purpose: hashmap adt
'''

class HashMap:
    '''hashmap class'''
    def __init__(self):
        self.buckets = 7
        self.map = [None] * self.buckets
        self.load = 0
        self.keyslist = []

    def get_hash(self, key):
        '''hashing function'''
        total = 0
        for i in key:
            total += i
            return total % self.buckets

    def get(self, key):
        '''Return the value for key if key is in the dictionary.
        If key is not in the dictionary, raise a KeyError.'''
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError

    def set(self, key, value):
        '''add the (key,value) pair to the hashMap.
        since test_hashmap.py loops through hm.set(k,v),
        i handled rehashing in the capacity(self) function'''
        key_value = [key, value]
        self.keyslist.append(key)
        key_hash = self.get_hash(key)
        key_value = [key, value]
        self.map[key_hash] = list([key_value])
        self.load += 1

    def remove(self, key):
        '''Remove the key and its associated value from the map.
        If the key does not exist, nothing happens.
        Do not rehash the table after deleting keys.'''
        key_hash = self.get_hash(key)
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)

    def clear(self):
        '''empty the HashMap'''
        self.load = 0
        return self.load

    def capacity(self):
        '''Return the current capacity--number of buckets--in the map.
        if the loadfactor >= 80%,
        rehash the map into a map double its current capacity.. ( - 1, right??)'''
        if self.load > .8 * self.buckets:
            self.buckets = self.buckets * 2 - 1
        return self.buckets

    def size(self):
        '''Return the number of key-value pairs in the map.'''
        return self.load

    def keys(self):
        '''Return a list of keys.'''
        return self.keyslist
