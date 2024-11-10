from enum import Enum
from sqlalchemy import text, Column, Integer, String, Float, Boolean, MetaData, Table
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, FastAPI
from db import get_db, engine

app = FastAPI()

# Function to dynamically delete a column from an existing table
def delete_column_from_table(db: Session, table_name: str, column_name: str):
    # Reflect the existing table from the database
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Check if the column exists in the table schema
    if column_name not in table.columns:
        raise HTTPException(status_code=404, detail=f"Column {column_name} not found in table {table_name}.")

    # Alter the table to drop the column
    try:
        db.execute(text(f'ALTER TABLE "{table_name}" DROP COLUMN "{column_name}"'))
        db.commit()
        return {"detail": f"Column {column_name} successfully deleted from {table_name}."}
    except Exception as e:
        db.rollback()  # In case of error, rollback any changes
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/delete_column/")
def delete_column(
    table_name: str, 
    column_name: str, 
    db: Session = Depends(get_db)
):
    try:
        # Call the function to delete the column dynamically
        return delete_column_from_table(db, table_name, column_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




# def delete_column_from_table(db: Session, table_name: str, column_name: str):
#     try:
#         # Perform the ALTER TABLE DROP COLUMN query
#         db.execute(text(f'ALTER TABLE "{table_name}" DROP COLUMN "{column_name}"'))
#         db.commit()  # Commit the transaction
#         return {"detail": f"Column {column_name} successfully deleted from {table_name}."}
#     except Exception as e:
#         db.rollback()  # Rollback in case of any error
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/delete_column/")
# def delete_column(
#     table_name: str, 
#     column_name: str, 
#     db: Session = Depends(get_db)
# ):
#     try:
#         return delete_column_from_table(db, table_name, column_name)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))