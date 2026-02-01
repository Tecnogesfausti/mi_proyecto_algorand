from algosdk import account, mnemonic
# Leer mnemonic desde archivo local
with open("mnemonic.txt", "r") as f:
    ALGO_MNEMONIC = f.read().strip()

private_key = mnemonic.to_private_key(ALGO_MNEMONIC)
public_address = account.address_from_private_key(private_key)

print("Hola Algorand! 🎉")
print(f"Dirección de tu cuenta: {public_address}")
