from algosdk.v2client import algod
from algosdk import mnemonic, account

# Leer las 25 palabras desde el archivo "mnemonic.txt"
with open("mnemonic.txt", "r") as f:
    mnemonic_phrase = f.read().strip()  # Leer las 25 palabras y quitar espacios innecesarios

# Intentar convertir las 25 palabras (mnemonic) a una clave privada
try:
    private_key = mnemonic.to_private_key(mnemonic_phrase)
except Exception as e:
    print(f"Error al convertir el mnemonic a clave privada: {e}")
    exit()

# Generar la dirección pública a partir de la clave privada
public_address = account.address_from_private_key(private_key)

# Verificar la dirección pública generada
print(f"Dirección pública generada: {public_address}")

# Configuración del cliente de Algorand para Mainnet usando Algoscan
#  https://www.comparenodes.com/library/public-endpoints/algorand/

algod_address = "https://algorand-mainnet-algod.gateway.tatum.io/"  # Nodo de Algoscan para Mainnet
algod_token = ""  # No es necesario un token para este nodo

# Crear el cliente de Algorand para Mainnet usando Algoscan
algod_client = algod.AlgodClient(algod_token, algod_address)

# Obtener la información de la cuenta usando la dirección pública
try:
    account_info = algod_client.account_info(public_address)
    # Obtener el saldo en microALGOs (1 ALGO = 1,000,000 microALGOs)
    balance = account_info.get('amount')
    print(f"El saldo de la cuenta {public_address} es: {balance / 1_000_000} ALGO")
except Exception as e:
    print(f"Error al obtener el saldo de la cuenta: {e}")
    exit()

