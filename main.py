#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PolicyHolder import PolicyHolder
from Product import Product
from Payment import Payment

# Create products
product1 = Product(product_id=1, name="Health Insurance", description="Comprehensive health insurance")
product2 = Product(product_id=2, name="Life Insurance", description="Term life insurance")

# Create policyholders
policyholder1 = PolicyHolder(policyholder_id=1, name="John Doe")
policyholder2 = PolicyHolder(policyholder_id=2, name="Jane Smith")

# Register products to policyholders
policyholder1.register_product(product1)
policyholder2.register_product(product2)

# Create payments
payment1 = Payment(payment_id=1, policyholder_id=1, product_id=1, amount=100.0)
payment2 = Payment(payment_id=2, policyholder_id=2, product_id=2, amount=150.0)

# Process payments
payment1.process_payment()
payment2.process_payment()

# Display policyholders' details
print(policyholder1.get_details())
print(policyholder2.get_details())

# Display payments' details
print(payment1.get_details())
print(payment2.get_details())


# In[ ]:




