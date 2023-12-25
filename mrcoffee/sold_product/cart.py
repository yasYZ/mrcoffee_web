class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, amount):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price), 'name': str(product.name), 'picture':  str(product.picture), 'sale_price': str(product.sale_price), 'category': str(product.category), 'sale': product.is_sale, 'amount': str(amount)}
        self.session.modified = True

    def delete(self, product):
            product_id_str = str(product)

            if product_id_str in self.cart:
                del self.cart[product_id_str]
                self.session.modified = True
