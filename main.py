from flask import Flask
from flask_restful import Api
from models import db
from dotenv import load_dotenv
from resources import AddressList, AddressRetrieve, AddressListAll
import os

#load the enviroment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PGSQL_URI')
db.init_app(app)
api = Api(app)

api.add_resource(AddressList, '/address')
api.add_resource(AddressListAll, '/addresses')
api.add_resource(AddressRetrieve, '/address/<int:address_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)