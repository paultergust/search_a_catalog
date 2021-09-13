from operator import itemgetter
from catalog import Catalog

def fit_in_budget(wishlist, budget):
    wishlist = sorted(wishlist, key=itemgetter('price'))
    filtered = []
    for item in wishlist:
        if item['price'] > budget:
            return filtered

        filtered.append(item)
        budget = budget - item['price']

    return filtered

def process_input(ids, budget):
    budget = float(budget)
    ids = ids.split(' ')
    prods = catalog.get_products(ids)
    filtered_items = fit_in_budget(prods, budget)
    count = 0
    for item in filtered_items:
        count += 1
        txt = '#{count} - "{item_id}" - {price:.2f}'
        print(txt.format(count=count, item_id=item['id'], price=item['price']))

        

ids = ''
budget = ''
catalog = Catalog('catalogo_produtos_preco.json')
print('Digite "sair" a qualquer momento para encerrar o programa.')
while True:
    ids = input('insira ids: ')
    if 'sair' in ids:
        break
    budget = input('Insira o orçamento: ')
    if 'sair' in budget:
        break
    process_input(ids, budget)

