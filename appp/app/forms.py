from flask import request

class CustomerForm:
    def __init__(self):
        self.first_name = request.form.get('first_name')
        self.last_name = request.form.get('last_name')
        self.city = request.form.get('city')
        self.country = request.form.get('country')
        self.phone = request.form.get('phone')
