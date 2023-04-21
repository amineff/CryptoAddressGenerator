from bitcoin_wallet import BitcoinWallet
from crypto_type import CryptoType
from ethereum_wallet import EthereumWallet

class WalletFactory:
    @staticmethod
    def get_wallet(wallet_name ,coin):
        if coin == CryptoType.BITCOIN:
            return BitcoinWallet(wallet_name)
        elif coin == CryptoType.ETHEREUM:
            return EthereumWallet(wallet_name)

