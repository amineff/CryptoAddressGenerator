from flask_restful import Resource, reqparse
from crypto_type import COIN_TYPES
from models import Address, db
from wallet_factory import WalletFactory
import os

class AddressList(Resource):
    def post(self):
        try:
            choices = [choice for choice in COIN_TYPES]
            parser = reqparse.RequestParser()
            parser.add_argument('coin', required=True, help='Coin type is required', choices=choices,type=lambda s: s.upper().strip())
            args = parser.parse_args()
            coin = args['coin']
            print('coin to be generated:', coin)
            wallet_service = WalletFactory.get_wallet(os.getenv('WALLET_NAME'), coin)
            # generate the address for the given coin using crypto libraries
            # and store it in the database
            pub_key = wallet_service.get_public_key()
            address = wallet_service.generate_address()
            new_address = Address(coin=coin, address=address, pub_key=pub_key, wallet=os.getenv('WALLET_NAME'))
            db.session.add(new_address)
            db.session.commit()
            return {'id': new_address.id, 'address': new_address.address}
        except Exception as e:
            return {'error': str(e)}, 500

class AddressRetrieve(Resource):
    def get(self, address_id):
        address = Address.query.get(address_id)
        if not address:
            return {'error': 'Address not found'}, 404
        return {'coin': address.coin, 'address': address.address}


class AddressListAll(Resource):
    def get(self):
        addresses = Address.query.all()
        return [{'id': address.address_id, 'coin': address.coin, 'address': address.address, 'updated_at' : address.updated_at.strftime('%Y-%m-%d %H:%M'), 'created_at' : address.created_at.strftime('%Y-%m-%d %H:%M')} for address in addresses]