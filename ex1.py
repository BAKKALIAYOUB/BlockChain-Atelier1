import hashlib


class Node:
    """
    A class to represent a node in a Merkle Tree.

    Attributes:
    - hash (str): The hash value of the node.
    - left (Node): Left child of the node.
    - right (Node): Right child of the node.
    - parent (Node): Parent node.
    """
    def __init__(self, hash: str):
        self.hash = hash
        self.left = None
        self.right = None
        self.parent = None

    def set_parent(self, parent: 'Node') -> None:
        """
        Set the parent of the current node.
        """
        self.parent = parent

    def get_left(self) -> 'Node':
        """
        Get the left child of the current node.
        """
        return self.left

    def get_right(self) -> 'Node':
        """
        Get the right child of the current node.
        """
        return self.right

    def get_parent(self) -> 'Node':
        """
        Get the parent of the current node.
        """
        return self.parent

    def __str__(self) -> str:
        """
        Return the string representation of the node's hash.
        """
        return self.hash


class MerkleTree:
    """
    A class to represent a Merkle Tree.

    Attributes:
    - data (list[str]): List of transactions or data elements.
    - leaves (list[Node]): List of leaf nodes created from data.
    - root (Node): The root node of the tree.
    """
    def __init__(self, data: list[str], hash_function: hashlib=hashlib.sha256):
        self.data = data
        self.leaves = [Node(hash_function(el.encode('utf-8')).hexdigest()) for el in self.data]
        self.hash_function = hash_function
        self.root = None

    def get_root(self) -> Node:
        """
        Return the root of the Merkle Tree.
        """
        return self.root

    def build_tree(self) -> None:
        """
        Build the Merkle Tree by hashing pairs of nodes and setting parent-child relationships.
        """
        current_level = self.leaves

        while len(current_level) > 1:
            next_level = []

            if len(current_level) % 2 == 1:
                current_level.append(current_level[-1])

            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1]

                # Combine and hash the left and right node's hashes
                combined_hash = self.hash_function(left.hash.encode('utf-8') + right.hash.encode('utf-8')).hexdigest()
                parent = Node(combined_hash)

                # Set parent-child relationships
                left.set_parent(parent)
                right.set_parent(parent)
                parent.left = left
                parent.right = right

                next_level.append(parent)

            # Move to the next level of the tree
            current_level = next_level

        self.root = current_level[0]

    def get_proof(self, transaction: str) -> list[str]:
        """
        Get the proof (Merkle path) for a given transaction.

        Args:
        - transaction (str): The transaction string whose proof is required.

        Returns:
        - list[str]: The proof consisting of sibling hashes.
        """
        proof = []

        current_node = None
        for leaf in self.leaves:
            if leaf.hash == self.hash_function(transaction.encode('utf-8')).hexdigest():
                current_node = leaf
                break

        if current_node is None:
            return []

        while current_node != self.root:
            parent = current_node.get_parent()

            # If the current node is the left child, add the right sibling's hash to the proof
            if parent.left == current_node:
                proof.append(parent.right.hash)
            else:
                proof.append(parent.left.hash)

            current_node = parent

        return proof

    def verify_proof(self, transaction: str) -> bool:
        """
        Verify if a transaction is part of the Merkle Tree using its proof.

        Args:
        - transaction (str): The transaction to be verified.

        Returns:
        - bool: True if the transaction is part of the tree, False otherwise.
        """
        proof = self.get_proof(transaction=transaction)

        if len(proof) == 0:
            return False

        current_hash = self.hash_function(transaction.encode('utf-8')).hexdigest()

        for sibling_hash in proof:
            current_hash = self.hash_function(current_hash.encode('utf-8') + sibling_hash.encode('utf-8')).hexdigest()

        return current_hash == self.root.hash



if __name__ == "__main__":
    # Example usage:

    data = [
        "Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4",
        "Transaction 5", "Transaction 6", "Transaction 7", "Transaction 8"
    ]

    tree = MerkleTree(data, hashlib.sha384)
    tree.build_tree()

    print(tree.verify_proof("Transaction 1"))
