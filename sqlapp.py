from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), unique=True)
  brand_name = db.Column(db.String(200))
  regular_price_value = db.Column(db.Float)
  offer_price_value = db.Column(db.Integer)
  currency = db.Column(db.String(200))
  classification_l1 = db.Column(db.String(200))
  classification_l2 = db.Column(db.String(200))
  classification_l3 = db.Column(db.String(200))
  classification_l4 = db.Column(db.String(200))
  image_url = db.Column(db.String(200))

  def __init__(self, name, brand_name, regular_price_value, offer_price_value,currency,classification_l1,classification_l2,classification_l3,classification_l4,image_url):
    self.name = name
    self.brand_name = brand_name
    self.regular_price_value = regular_price_value
    self.offer_price_value = offer_price_value
    self.currency=currency
    self.classification_l1=classification_l1
    self.classification_l2=classification_l2
    self.classification_l3=classification_l3
    self.classification_l4=classification_l4
    self.image_url=image_url

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'brand_name', 'regular_price_value', 'offer_price_value','currency','classification_l1','classification_l2','classification_l3','classification_l4','image_url')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  brand_name = request.json['brand_name']
  regular_price_value = request.json['regular_price_value']
  offer_price_value = request.json['offer_price_value']
  currency = request.json['currency']
  classification_l1 = request.json['classification_l1']
  classification_l2 = request.json['classification_l2']
  classification_l3 = request.json['classification_l3']
  classification_l4 = request.json['classification_l4']
  image_url=request.json['image_url']

  new_product = Product(name, brand_name, regular_price_value, offer_price_value,currency,classification_l1,classification_l2,classification_l3,classification_l4,image_url)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  brand_name = request.json['brand_name']
  regular_price_value = request.json['regular_price_value']
  offer_price_value = request.json['offer_price_value']
  currency = request.json['currency']
  classification_l1 = request.json['classification_l1']
  classification_l2 = request.json['classification_l2']
  classification_l3 = request.json['classification_l3']
  classification_l4 = request.json['classification_l4']
  image_url=request.json['image_url']

  product.name = name
  product.brand_name = brand_name
  product.regular_price_value = regular_price_value
  product.offer_price_value = offer_price_value
  product.currency = currency
  product.classification_l1 = classification_l1
  product.classification_l2 = classification_l2
  product.classification_l3 = classification_l3
  product.classification_l4 = classification_l4
  product.image_url = image_url
  
  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run(debug=False)