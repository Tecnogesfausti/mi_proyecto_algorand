from algosdk import account
from algosdk import mnemonic

# Generar una nueva cuenta
private_key, public_address = account.generate_account()

# Convertir la clave privada a una frase de recuperación (mnemonic) de 25 palabras
mnemonic_phrase = mnemonic.from_private_key(private_key)

# Mostrar la dirección pública y la frase de recuperación
print("Dirección pública de la cuenta:", public_address)
print("Frase de recuperación (mnemonic) de 25 palabras:", mnemonic_phrase)

