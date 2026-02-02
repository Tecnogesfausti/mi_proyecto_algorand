# mi_proyecto_algorand
# Creelo en GitHub
git remote add origin git@github.com:TecnogesFauti/Algorand-Project.git
git remote -v
git add .
etc...

#github
source venv/bin/activate
.\venv\Scripts\activate
git status
git add .
git commit -m "Descripción de los cambios realizados"
git push origin main
(con git status vas viendo lo que debes hacer...)

1.- tener una sshkey en github


# codigo pruebas
Pruebas de envio de tokens
En Algorand vamos con 25 palabras aunque Pera me  invita a usar un formato nuevo (24 palabras)
al final con el el SDK no consigo trabajar con la private_key
Solucion:

crea_cuenta.py
(mnemomic.txt guarda las 24 palabras)
(direccion.key guarda la direccion nueva)

y en Pera Wallet importo con esas 25, a continuacion verifico la dir. 34ES... 
Ejemplos:
1.'hello_algorand.py' -> confirma la dir.34xxxx

2.' 
y ya puedo pasar FaustiCoins
o lo que quiera hacer.

#autocontenido
Crear una AppImage visual con una estructura ModelView y que conecte con el SDK
LA idea es ir añadiendo funciones de assets, saldo, etc.
EL problema es que la cuenta creada en Pera Wallet debe tener el formato legacy
de 25 palabras.
La solucion. Crear una que sera la que 'hable' con otras cuentas.

