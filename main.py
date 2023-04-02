
import first_blockchain as fb

def adding_file_to_blockchain(file_path):

    bc = fb.Blockchain()
    bc.add_block(file_path)

    for block in bc.chain:
        print(block.__dict__)




def getting_file_from_blockchain(hash_value):

    bc = fb.Blockchain.load_from_file('blockchain.pkl')     # load the instance file of the previous data 
    for block in bc.chain:
        if(block.hash == hash_value):
            # print(block.__dict__)
            with open('output.sql' , 'w') as f:
                f.write(block.data)
            break
    else:
        print("File Not Found")   

getting_file_from_blockchain('c5ba0a4bb11abd5c8418f5d5c692b9c6c9b29e4b98efadaaf1916f225e4e44f0')     



