# Blockchain Atelier 1

This repository contains two Python scripts, `EX1.PY` and `EX2.PY`, which demonstrate fundamental concepts of blockchain technology, specifically Merkle Trees and Block Mining.

## EX1.PY

### Overview

`EX1.PY` implements a Merkle Tree, a data structure used in blockchain technology to efficiently and securely verify the integrity of data. The script includes the following classes:

- **Node**: Represents a node in the Merkle Tree.
- **MerkleTree**: Represents the Merkle Tree itself.

### Key Features

- **Node Class**:
    - Attributes: `hash`, `left`, `right`, `parent`.
    - Methods: `set_parent`, `get_left`, `get_right`, `get_parent`, `__str__`.

- **MerkleTree Class**:
    - Attributes: `data`, `leaves`, `root`.
    - Methods: `get_root`, `build_tree`, `get_proof`, `verify_proof`.

### Usage

The script demonstrates how to create a Merkle Tree from a list of transactions, build the tree, and verify the inclusion of a transaction using a Merkle proof.

### Example
```python
# Example usage of EX1.PY

from ex1 import MerkleTree

# Sample transactions
transactions = ['tx1', 'tx2', 'tx3', 'tx4']

# Create a Merkle Tree
merkle_tree = MerkleTree(transactions)

# Build the tree
merkle_tree.build_tree()

# Get the root of the tree
root = merkle_tree.get_root()
print(f"Root Hash: {root}")

# Get proof for a transaction
proof = merkle_tree.get_proof('tx1')
print(f"Proof for tx1: {proof}")

# Verify the proof
is_valid = merkle_tree.verify_proof('tx1')
print(f"Is the proof valid? {is_valid}")
```

## EX2.PY

### Overview

`EX2.PY` focuses on the concept of block mining in a blockchain. It simulates the process of mining a block by finding a nonce that satisfies a given difficulty level. The script includes the following classes:

- **Block**: Represents a block in the blockchain.
- **Blockchain**: Represents the blockchain itself.

### Key Features

- **Block Class**:
    - Attributes: `timestamp`, `data`, `previous_hash`, `nonce`, `hash`.
    - Methods: `calcul_hash`, `mine_block`.

### Usage

The script demonstrates how to create a blockchain, add blocks to it, and validate the integrity of the blockchain.

### Example
```python
# Example usage of EX2.PY
previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"

difficulty = 5
new_block = Block(data="Transaction data", previous_hash=previous_hash)
        
print(f"\nMining block with difficulty {difficulty}...")
start_time = time.time()  # Start timing

new_block.mine_block(difficulty)

end_time = time.time()  # End timing
execution_time = end_time - start_time

print(f"Final block hash: {new_block.hash}")
print(f"Nonce: {new_block.nonce}")
print(f"Time taken to mine block at difficulty {difficulty}: {execution_time:.2f} seconds")
```
