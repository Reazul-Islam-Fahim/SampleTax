import crud, schemas
from sqlalchemy.orm import Session 


def _calculate_tax_liability(db : Session, etin: str, taxable_income: float):
    if not isinstance(taxable_income, (int, float)):
        raise TypeError(f"Expected taxable_income to be int or float, got {type(taxable_income)}")
    
    tax_liability = 0
    slabs = [
        (100000, 0.05),
        (400000, 0.10),
        (500000, 0.15),
        (500000, 0.20),
        (2000000, 0.25),
        (float('inf'), 0.30)
    ]

    slab_values = []  # Store taxable amounts per slab
    for limit, rate in slabs:
        if taxable_income <= 0:
            break
        taxable_amount = min(taxable_income, limit)
        if not isinstance(taxable_amount, (int, float)):
            raise TypeError(f"Unexpected taxable_amount type: {type(taxable_amount)}")
        tax_liability += taxable_amount * rate
        slab_values.append(int(taxable_amount * rate))  # Ensure taxable_amount is numeric
        taxable_income -= taxable_amount

    # Pad slab_values to match the number of slab columns
    while len(slab_values) < 6:
        slab_values.append(0)

    # Create a Tax_Slab schema
    tax_slab_data = schemas.Tax_Slab(
        etin=etin,  # Include the ETIN field
        first=0,
        second=slab_values[0],
        third=slab_values[1],
        fourth=slab_values[2],
        fifth=slab_values[3],
        sixth=slab_values[4],
        seventh=slab_values[5]
    )

    # Save the tax slab data to the database
    created_slab = crud.create_tax_slab(db, etin, tax_slab_data)

    return tax_liability


