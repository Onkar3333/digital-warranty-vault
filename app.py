from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warranties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model for Warranties
class Warranty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    warranty_period_months = db.Column(db.Integer, nullable=False)
    receipt_path = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        expiry_date = self.purchase_date + timedelta(days=(self.warranty_period_months * 30))
        return {
            'id': self.id,
            'product_name': self.product_name,
            'purchase_date': self.purchase_date.strftime('%Y-%m-%d'),
            'warranty_period_months': self.warranty_period_months,
            'expiry_date': expiry_date.strftime('%Y-%m-%d'),
            'receipt_path': self.receipt_path
        }

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/warranties', methods=['GET'])
def get_warranties():
    warranties = Warranty.query.all()
    return jsonify([w.to_dict() for w in warranties])

@app.route('/api/warranties', methods=['POST'])
def add_warranty():
    data = request.json
    try:
        warranty = Warranty(
            product_name=data['product_name'],
            purchase_date=datetime.strptime(data['purchase_date'], '%Y-%m-%d'),
            warranty_period_months=data['warranty_period_months'],
            receipt_path=data.get('receipt_path', '')
        )
        db.session.add(warranty)
        db.session.commit()
        return jsonify({'message': 'Warranty added successfully!', 'warranty': warranty.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/warranties/<int:id>', methods=['DELETE'])
def delete_warranty(id):
    warranty = Warranty.query.get_or_404(id)
    db.session.delete(warranty)
    db.session.commit()
    return jsonify({'message': 'Warranty deleted successfully!'})

# Initialize the database if not exists
@app.before_first_request
def create_tables():
    if not os.path.exists('warranties.db'):
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
