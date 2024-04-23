import os
import csv
from solders.keypair import Keypair

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def account_generator():
    """Return address and privateKey in base58"""
    account = Keypair()
    address = account.pubkey()
    priv_key = account.from_json(account.to_json())
    return address, priv_key

if __name__ == '__main__':
    name_file = str(input("Name Output file (without csv): "))
    amount = int(input("How many accounts to create: "))
    i = 0

    directory = "Wallet"
    create_directory_if_not_exists(directory)

    with open(file=os.path.join(directory, f"{name_file}.csv"), mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "Private Key"])  # Write header row
        while i != amount:
            address, private_key = account_generator()
            print(f"Generated wallet {i+1}/{amount}: Address: {address}")
            writer.writerow([address, private_key])
            i += 1
