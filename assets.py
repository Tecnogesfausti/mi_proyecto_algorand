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
    
    # Saldo ALGO
    balance = account_info.get('amount', 0)
    print(f"Saldo: {balance / 1_000_000} ALGO")

    # Assets de la cuenta
    assets = account_info.get("assets", [])
    if assets:
        print("\nAssets de la cuenta:")
        for asset in assets:
            asset_id = asset["asset-id"]
            amount = asset["amount"]

            # Intentar obtener más info del asset
            try:
                info = algod_client.asset_info(asset_id)
                name = info.get("params", {}).get("name", "")
                decimals = info.get("params", {}).get("decimals", 0)
                real_amount = amount / (10 ** decimals)
                print(f"- {name} (ID {asset_id}): {real_amount}")
            except Exception as e:
                print(f"- Asset ID {asset_id}: {amount} (info detallada no disponible: {e})")
    else:
        print("No hay assets asociados a esta cuenta.")

except Exception as e:
    print(f"Error al obtener la información de la cuenta: {e}")

