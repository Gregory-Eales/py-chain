import hashlib
import json
from time import time

"""

# Block Format

block = {
	'index': 1,
	'timestamp': 1506057125.900785,
	'transactions': [
		{
			'sender': "8527147fe1f5426f9dd545de4b27ee00",
			'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
			'amount': 5,
		}
	],
	'proof': 324984774000,
	'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
"""


class Blockchain(object):

	def __init__(self):

		self.chain = []

		self.current_transactions = []

		self.new_block(previous_hash=1, proof=100)

	def new_block(self, proof, previous_hash=None):
		
		block = {
			'index': len(self.chain)+1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1])
		}

		self.current_transactions = []
		self.chain.append(block)
		return block

	def new_transaction(self, sender, recipient, amount):

		self.current_transactions.append(
			{
				"sender":sender,
				"recipient":recipient,
				"amount":amount,
				}
			)

		return self.last_block["index"]+1

	def hash(self, block):
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		return self.chain[-1]

	def proof_of_work(self, last_proof):

		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	def valid_proof(self, last_proof, proof):

		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"


	def valid_chain(self, chain):
		
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")

            if block['previous_hash'] != self.hash(last_block):
                return False

            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):

        neighbours = self.nodes
        new_chain = None

        max_length = len(self.chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False



def main():
	GregCoin = Blockchain()
	print(GregCoin.last_block)

if __name__ == '__main__':
	main()