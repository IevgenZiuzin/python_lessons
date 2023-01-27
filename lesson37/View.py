def display_amount(products: list):
    print(f'Total: {len(products)}')


def display_products(products: list):
    if not products:
        print('Nothing to display')
        return
    for product in products:
        for key in product.keys():
            if product[key] is not None and product[key] != '':
                print(f'{key}: {product[key]}')
