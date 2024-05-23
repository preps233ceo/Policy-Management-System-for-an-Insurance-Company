#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Product:
    def __init__(self, product_id, name, description):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.is_active = True

    def update_product(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description

    def suspend_product(self):
        self.is_active = False

    def reactivate_product(self):
        self.is_active = True

    def get_details(self):
        return f'Product[ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Active: {self.is_active}]'

