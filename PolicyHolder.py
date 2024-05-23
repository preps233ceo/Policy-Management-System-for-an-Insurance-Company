#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PolicyHolder:
    def __init__(self, policyholder_id, name, status='active'):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = status
        self.products = []

    def register_product(self, product):
        self.products.append(product)

    def suspend(self):
        self.status = 'suspended'

    def reactivate(self):
        self.status = 'active'

    def get_details(self):
        products_list = ', '.join([product.name for product in self.products])
        return f'PolicyHolder[ID: {self.policyholder_id}, Name: {self.name}, Status: {self.status}, Products: {products_list}]'

