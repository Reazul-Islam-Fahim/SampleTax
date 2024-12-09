def _calculate_tax_liability(taxable_income: float):
         tax_liability = 0
         slabs = [
        (350000, 0),
        (100000, 0.05),
        (400000, 0.10),
        (500000, 0.15),
        (500000, 0.20),
        (2000000, 0.25),
        (float('inf'), 0.30)
         ]

         for limit, rate in slabs:
             if taxable_income <= 0:
                 break
             taxable_amount = min(taxable_income, limit)
             tax_liability += taxable_amount * rate
             print(taxable_amount * rate)
             taxable_income -= taxable_amount

         return tax_liability