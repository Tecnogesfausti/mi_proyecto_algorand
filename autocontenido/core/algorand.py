from algosdk.v2client import algod

ALGOD_URL = "https://algorand-mainnet-algod.gateway.tatum.io/"
ALGOD_TOKEN = ""

class AlgorandClient:
    def __init__(self):
        self.client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_URL)

    def get_account_info(self, address):
        return self.client.account_info(address)

    def get_balance(self, address):
        info = self.get_account_info(address)
        return info["amount"] / 1_000_000

    def get_assets(self, address):
        info = self.get_account_info(address)
        return info.get("assets", [])
