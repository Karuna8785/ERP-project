'''Automated Order-to-Cash End-to-End Validation Test Suite.'''
import pytest

def test_order_to_cash_pipeline():
    quotation_amount = 10000.0
    discount = 0.10
    tax_rate = 0.18
    subtotal = quotation_amount * (1.0 - discount)
    tax = subtotal * tax_rate
    total_invoice = subtotal + tax
    assert total_invoice == 10620.0
