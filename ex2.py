import hashlib
import datetime
import time

class Block():
    def __init__(self, data: str, previous_hash: str):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.hash = self.calcul_hash()
        
    def calcul_hash(self):
        hash = hashlib.sha256(
            
            str(self.data).encode("utf-8") +
            str(self.previous_hash).encode("utf-8") +
            str(self.timestamp).encode("utf-8") +
            str(self.nonce).encode("utf-8")
        ).hexdigest()
        # print("Hash", hash)
        return hash
    
    def mine_block(self, difficulty: int):
        target = '0' * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calcul_hash()
            
        print(f"Block mined: {self.hash}")
    

if __name__ == "__main__":
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
        