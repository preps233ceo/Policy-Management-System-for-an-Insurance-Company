#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Payment:
    def __init__(self, payment_id, policyholder_id, product_id, amount, status='pending'):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.status = status

    def process_payment(self):
        self.status = 'completed'

    def set_reminder(self):
        return f'Reminder: Payment for policyholder {self.policyholder_id} is pending.'

    def apply_penalty(self):
        penalty = self.amount * 0.10
        self.amount += penalty

    def get_details(self):
        return f'Payment[ID: {self.payment_id}, PolicyHolderID: {self.policyholder_id}, ProductID: {self.product_id}, Amount: {self.amount}, Status: {self.status}]'

