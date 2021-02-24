class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def __repr__(self):
        sorted_products = sorted(self.products)
        final = str(f"Items in the {self.name} catalogue:\n")
        for product in sorted_products:
            #final += '\n'.join(sorted(self.products) - замества иф и първия ред
            if product == sorted_products[-1]:
                final += f'{product}'
            else:
                final += f'{product}\n'
        return final

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        #return [el for el in self.products if el.startswith(first_letter)]
        letter_products = []
        for item in self.products:
            if item[0] == first_letter:
                letter_products.append(item)
        return letter_products



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
print(catalogue)
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

