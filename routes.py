


from flask import Blueprint, render_template, request, redirect, url_for, session, flash

# Create a blueprint for the main routes
main = Blueprint('main', __name__)

@main.before_request
def setup_cart():
    if 'cart' not in session:
        session['cart'] = []

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/category/<string:category_name>')
def category_products(category_name):
    from models import Product
    products = Product.query.filter_by(category=category_name).all()

    if not products:
        flash(f"No products available in the {category_name} category.")
        return redirect(url_for('main.product_list'))

    return render_template('category_products.html', products=products, category_name=category_name)

@main.route('/products')
def product_list():
    from models import Product
    products = Product.query.all()
    product_categories = {}

    for product in products:
        category = product.category
        if category not in product_categories:
            product_categories[category] = []
        product_categories[category].append(product)

    return render_template('products.html', product_categories=product_categories)

# New route: Product details page
@main.route('/product/<int:product_id>')
def product_details(product_id):
    from models import Product
    product = Product.query.get_or_404(product_id)

    return render_template('product_details.html', product=product)

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    from models import Product
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form['quantity'])

    if quantity > product.stock_quantity:
        flash(f"Only {product.stock_quantity} items available.")
        return redirect(url_for('main.product_details', product_id=product_id))

    for item in session['cart']:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            flash(f"Updated quantity for {product.product_name}.")
            break
    else:
        session['cart'].append({'product_id': product_id, 'quantity': quantity})
        flash(f"Added {quantity} of {product.product_name} to cart.")

    return redirect(url_for('main.product_details', product_id=product_id))


@main.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    cart_items = []
    total_price = 0
    from models import Product

    # Fetch products in one query for efficiency
    product_ids = [item['product_id'] for item in cart]
    products = Product.query.filter(Product.product_id.in_(product_ids)).all()
    product_dict = {product.product_id: product for product in products}

    for item in cart:
        product = product_dict.get(item['product_id'])
        if product:
            item_total = product.price * item['quantity']
            cart_items.append({'product': product, 'quantity': item['quantity'], 'total': item_total , 'image': product.product_image })
            total_price += item_total

    tax = round(total_price * 0.1, 2)  # Example 10% tax
    return render_template('cart.html', cart_items=cart_items, total_price=total_price, tax=tax)



@main.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['product_id'] != product_id]
    session['cart'] = cart
    flash("Item removed from cart." , "red")
    return redirect(url_for('main.view_cart'))


# @main.route('/update_cart', methods=['POST'])
# def update_cart():
#     cart = session.get('cart', [])
#     for item in cart:
#         product_id = item['product_id']
#         new_quantity = int(request.form.get(f'quantity_{product_id}', item['quantity']))
#         item['quantity'] = new_quantity
#     session['cart'] = cart  # Save updated cart in session
#     flash("Cart updated successfully.")
#     return redirect(url_for('main.view_cart'))



@main.route('/update_cart', methods=['POST'])
def update_cart():
    cart = session.get('cart', [])
    for item in cart:
        product_id = item['product_id']
        new_quantity = request.form.get(f'quantity_{product_id}', type=int, default=item['quantity'])
        if new_quantity > 0:
            item['quantity'] = new_quantity
        else:
            cart = [i for i in cart if i['product_id'] != product_id]
    session['cart'] = cart
    session.modified = True
    flash("Cart updated successfully." , "blue")
    return redirect(url_for('main.view_cart'))



# @main.route('/checkout', methods=['POST'])
# def checkout():
#     from models import Product
#     from __init__ import db
#     cart = session.get('cart', [])




#         # Clear the cart and ensure session is saved
#     session['cart'] = []
#     session.modified = True  # Ensure session is updated
#     flash("Order placed successfully!")

    
#     # Redirect to the home page
#     return redirect(url_for('main.home'))





@main.route('/checkout', methods=['POST'])
def checkout():
    from models import Product  # Adjust import if necessary
    from __init__ import db

    cart = session.get('cart', [])
    print(f"Cart: {cart}")  # Debugging statement

    if not cart:
        flash("Your cart is empty. Add products before checking out.")
        return redirect(url_for('main.view_cart'))

    for item in cart:
        product = Product.query.get(item['product_id'])
        if not product or product.stock_quantity < item['quantity']:
            flash(f"Insufficient stock for {product.product_name}.","red")
            return redirect(url_for('main.view_cart'))

        product.stock_quantity -= item['quantity']

    db.session.commit()

    session['cart'] = []
    session.modified = True

    flash("Order placed successfully!" , "green")
    return redirect(url_for('main.view_cart'))


##############################3
# ML


from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from request
    data = request.get_json(force=True)
    # Send request to the model server
    response = requests.post("http://127.0.0.1:5001/invocations", 
                              headers={"Content-Type": "application/json"},
                              data=json.dumps(data))
    # Get prediction from response
    prediction = response.json()
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(port=5000)



import requests
from flask import request, render_template
from datetime import datetime

@main.route('/forecast_sales/<int:product_id>', methods=['GET'])
def forecast_sales(product_id):
    # Prepare input data for API call (forecasting 30 days ahead)
    input_data = {"periods": 30}

    # Call the MLflow model API to get forecast
    response = requests.post("http://127.0.0.1:5003/invocations", json=input_data)
    forecast = response.json()

    # Extract predictions from forecast
    predictions = forecast['yhat']
    dates = [datetime.strptime(d, '%Y-%m-%d').strftime('%d %b %Y') for d in forecast['ds']]

    return render_template('forecast.html', product_id=product_id, predictions=predictions, dates=dates)