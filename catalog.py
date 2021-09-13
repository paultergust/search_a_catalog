import json

class Catalog:
    
    def __init__(self, filename):
        self._products = self.load_and_index(filename)


    def load_and_index(self, filename:str):
        products = {}
        catalog_file = open(filename, 'r')
        for line in catalog_file.readlines():
            obj = json.loads(line)
            obj['price'] = float(obj['price'])
            products[obj['id']] = obj

        return products


    def get_products(self, wishlist:list):
        selected = []
        for item in wishlist:
            try:
                selected.append(self._products[item])
            except KeyError:
                continue

        return selected

