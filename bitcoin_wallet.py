import bitcoin
from bitcoinlib.wallets import Wallet, wallet_exists, wallet_delete

from wallet_service import WalletService

class BitcoinWallet(WalletService):
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
        address = bitcoin.pubkey_to_address(key.key_public)
        bitcoin.add_privkeys(key.key_private, 1)
        return address

    def delete(self):
            wallet_delete(self.wallet_name)