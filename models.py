from __init__ import db

class Branch(db.Model):
    __tablename__ = 'branches'

    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)

    def __repr__(self):
        return f'<"branchs " {self.branch_id} {self.branch_name} {self.city}>'

class Sales(db.Model):
    __tablename__ = 'sales'

    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    customer_age = db.Column(db.Integer, nullable=False)
    customer_gender = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    zone = db.Column(db.String(255), nullable=False)
    delivery_type = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    shipping_fee = db.Column(db.Integer, nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.SmallInteger, nullable=False)


    def __repr__(self):
        return f'<"sales" {self.order_id} {self.product_name} {self.order_quantity}>'
    
class Employee(db.Model):
    __tablename__ = 'employee'

    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id'), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<"employee" {self.employee_id} {self.first_name} {self.position}>'
    
class Inventory(db.Model):
    __tablename__ = 'inventory'

    inventory_id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(255), nullable=False)
    country_name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    total_items_quantity = db.Column(db.Integer, nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id'), nullable=False)


    def __repr__(self):
        return f'<"inventory " {self.inventory_id} {self.country_name} {self.region_name}>'
    

class Supplier(db.Model):
    __tablename__ = 'suppliers'

    supplier_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(255), nullable=False)
    contact_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.inventory_id'), nullable=False)


    def __repr__(self):
        return f'<"suppliers " {self.supplier_id} {self.supplier_name} {self.email}>'
    
class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id'), nullable=False)
    product_image=db.Column(db.String(255),nullable=False)


    def __repr__(self):
        return f'<"products " {self.product_id} {self.product_name} {self.category}>'
    

class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    loyalty_points = db.Column(db.SmallInteger, nullable=False)


    def __repr__(self):
        return f'<"customer " {self.customer_id} {self.first_name} {self.last_name}>'
    

class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.String(255), primary_key=True)
    order_date = db.Column(db.Date, nullable=False)
    ship_date = db.Column(db.Date, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(255), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.SmallInteger, nullable=False)


    def __repr__(self):
        return f'<"orders " {self.order_id} {self.quantity} {self.product_name}>'
    
    