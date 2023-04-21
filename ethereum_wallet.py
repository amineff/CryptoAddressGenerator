from bitcoinlib.wallets import Wallet, wallet_exists, wallet_delete
from eth_account import Account
from wallet_service import WalletService


class EthereumWallet(WalletService):
    def __init__(self, wallet_name):
        self.wallet_name = wallet_name
        if not wallet_exists(wallet_name):
            self.wallet = Wallet.create(wallet_name)
        else:
            self.wallet = Wallet(wallet_name)

    def get_public_key(self):
            return self.wallet.get_key().key_public

    def generate_address(self):
        key = self.wallet.get_key()
        acct = Account.from_key(key.key_private)
        print("Address:", acct)
        print("Address:", acct.address)
        return acct.address

    def delete(self):
            wallet_delete(self.wallet_name)