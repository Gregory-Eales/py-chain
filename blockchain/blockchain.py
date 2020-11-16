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

	def new_block(self):
		pass

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
		pass

	@property
	def last_block(self):
		return 0



def main():
	
	GregCoin = Blockchain()
	print(GregCoin.last_block)

if __name__ == '__main__':
	main()