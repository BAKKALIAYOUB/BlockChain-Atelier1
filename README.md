# Blockchain Atelier 1

This repository contains two Python scripts, `EX1.PY` and `EX2.PY`, which demonstrate fundamental concepts of blockchain technology, specifically Merkle Trees and Block Mining.

## EX1.PY

### Concept
A Merkle Tree is a data structure used in blockchain technology to efficiently and securely verify the integrity of large amounts of data. It ensures that data is valid without storing all of it, using hashes instead.

In this script, a Merkle Tree is built from a list of transactions. Each transaction is hashed, forming the leaves of the tree. Pairs of nodes are combined to generate new hashes until a single root is obtained, known as the root hash. This root allows the verification of all transactions without requiring access to each one individually.

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

##############
# Result
##############

# Root Hash: 773bc304a3b0a626a520a8d6eacc36809ac18c0b174f3ff3cdaf0a4e9c64433d
# Proof for tx1: ['27ca64c092a959c7edc525ed45e845b1de6a7590d173fd2fad9133c8a779a1e3', '850cf301915d09ebcfa84e2ee4087025e17a6fca7e4149ce02cff94cd3db55de']
# Is the proof valid? True
```

## EX2.PY

### Concept
Block mining is a fundamental process in decentralized blockchains like Bitcoin. It involves finding a nonce (an arbitrary number) which, when combined with the block data and hashed, produces a hash starting with a certain number of zeros, representing the difficulty level.

In this script, a block is created with transaction data and a previous hash (the hash of the previous block). Mining the block involves trying different nonces until a valid hash is found that meets the difficulty level.

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
from ex2 import Block
import time

previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"

print("=====================================================================================================")
# Test different difficulty levels
for difficulty in range(1, 5):  # Change this range to test more difficulties
    new_block = Block(data="Transaction data", previous_hash=previous_hash)
    
    print(f"\nMining block with difficulty {difficulty}...")
    start_time = time.time()  # Start timing
    
    new_block.mine_block(difficulty)
    
    end_time = time.time()  # End timing
    execution_time = end_time - start_time
    
    print(f"Final block hash: {new_block.hash}")
    print(f"Nonce: {new_block.nonce}")
    print(f"Time taken to mine block at difficulty {difficulty}: {execution_time:.2f} seconds")
    print("=====================================================================================================")
    
##############
# Output
##############

# =====================================================================================================

# Mining block with difficulty 1...
# Block mined: 03ba4af7c4f5389de5f9598ab501435d38c8af0e5d0da00700c2dd8ac5763694
# Final block hash: 03ba4af7c4f5389de5f9598ab501435d38c8af0e5d0da00700c2dd8ac5763694
# Nonce: 15
# Time taken to mine block at difficulty 1: 0.00 seconds
# =====================================================================================================

# Mining block with difficulty 2...
# Block mined: 001338469f2754031a695023e22080a950a11fd83a4c3f1e0f63762533173b55
# Final block hash: 001338469f2754031a695023e22080a950a11fd83a4c3f1e0f63762533173b55
# Nonce: 213
# Time taken to mine block at difficulty 2: 0.00 seconds
# =====================================================================================================

# Mining block with difficulty 3...
# Block mined: 000655836611b2b3dd279469f5fa0dc4e8253af13ef69d38cbd9af609e15990c
# Final block hash: 000655836611b2b3dd279469f5fa0dc4e8253af13ef69d38cbd9af609e15990c
# Nonce: 12504
# Time taken to mine block at difficulty 3: 0.08 seconds
# =====================================================================================================

# Mining block with difficulty 4...
# Block mined: 00006d821813131dec823960c81060ea79566e38a507dc4b4a4c52e12ad620a7
# Final block hash: 00006d821813131dec823960c81060ea79566e38a507dc4b4a4c52e12ad620a7
# Nonce: 35014
# Time taken to mine block at difficulty 4: 0.22 seconds
# =====================================================================================================
```


