import hashlib
import pickle

def hashGenerator(data):
    result = hashlib.sha256(data.encode())   # sha256 is used to encode the data
    return result.hexdigest()   # to get the data in hexadecimal


class Block:
    
    def __init__(self,data,hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev = prev_hash

class Blockchain:
    chain = []
    def __init__(self):
        hashLast = hashGenerator('gen_last')   # previous block hash value
        hashStart = hashGenerator('gen_hash')   # current block hash value 

        genesis = Block('gen_data', hashStart, hashLast)
        self.chain = [genesis]
    
    def add_block(self, file_path):
        with open(file_path, 'r') as f:
            data = f.read()
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)
    
    def save_to_file(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self,f)    # it is used to save a python object to the file not string
    
    @classmethod           # it defines it as a class method and not as a instance method
    def load_from_file(cls, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)


bc = Blockchain()
bc.add_block('series.sql')
bc.save_to_file('blockchain.pkl')


# for block in bc.chain:
#     print(block.__dict__)




