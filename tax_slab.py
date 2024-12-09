import crud, schemas
from sqlalchemy.orm import Session 

def _calculate_tax_liability(taxable_income: float):
         tax_liability = 0
         slabs = [
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
     

# print(_calculate_tax_liability(850000))



def _calculate_tax_liability_and_create_slab(db: Session, etin: str, taxable_income: float):
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
        tax_liability += taxable_amount * rate
        slab_values.append(int(taxable_amount))  # Convert to int for consistency
        taxable_income -= taxable_amount

    # Pad slab_values to match the number of slab columns
    while len(slab_values) < 6:
        slab_values.append(0)

    # Create a Tax_Slab schema
    tax_slab_data = schemas.Tax_Slab(
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

    return {
        "tax_liability": tax_liability,
        "created_slab": created_slab
    }