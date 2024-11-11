from enum import Enum
from sqlalchemy import text, MetaData, Table
from sqlalchemy.orm import Session
from db import Base
from fastapi import HTTPException, Depends, FastAPI
from  db import get_db, engine

app = FastAPI()

# Enum for column types
class ColumnTypeEnum(str, Enum):
    string = "string"
    integer = "integer"
    float = "float"
    boolean = "boolean"
    
    
    
def get_column_type_sql(column_type: ColumnTypeEnum):
    """Converts the enum type to SQLAlchemy column type string"""
    if column_type == ColumnTypeEnum.string:
        return "VARCHAR"
    elif column_type == ColumnTypeEnum.integer:
        return "INTEGER"
    elif column_type == ColumnTypeEnum.float:
        return "FLOAT"
    elif column_type == ColumnTypeEnum.boolean:
        return "BOOLEAN"
    else:
        raise ValueError(f"Unsupported column type: {column_type}")
    
    
    
def add_column_to_table(db: Session, table_name: str, column_name: str, column_type: ColumnTypeEnum):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Convert the column_type enum to a valid SQL type string
    column_type_sql = get_column_type_sql(column_type)

    try:
        # Perform the ALTER TABLE ADD COLUMN query using raw SQL
        db.execute(text(f'ALTER TABLE "{table_name}" ADD COLUMN "{column_name}" {column_type_sql}'))
        db.commit()  # Commit the transaction
        return {"detail": f"Column {column_name} of type {column_type_sql} added to {table_name}."}
    except Exception as e:
        db.rollback()  # Rollback in case of any error
        raise HTTPException(status_code=500, detail=str(e))
    
    
   
    
    
    
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
    
    
    
    
    
def update_column_in_table(db: Session, table_name: str, column_name: str, new_value: str, condition: str):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Construct the SQL UPDATE statement
    update_statement = text(f"""
        UPDATE "{table_name}" 
        SET "{column_name}" = :new_value
        WHERE {condition}
    """)

    try:
        # Execute the update statement
        db.execute(update_statement, {"new_value": new_value})
        db.commit()  # Commit the transaction
        return {"detail": f"Column {column_name} updated successfully in table {table_name}."}
    except Exception as e:
        db.rollback()  # Rollback in case of any error
        raise HTTPException(status_code=500, detail=str(e))


    
    
    
    
@app.post("/add_column/")
def add_column(
    table_name: str, 
    column_name: str, 
    column_type: ColumnTypeEnum, 
    db: Session = Depends(get_db)
):
    try:
        # Call the function to add the column dynamically
        add_column_to_table(db, table_name, column_name, column_type)
        return {"detail": f"Column {column_name} of type {column_type} added to {table_name}."}
    except Exception as e:
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
    
    
    
@app.post("/update_column/")
def update_column(
    table_name: str,
    column_name: str,
    new_value: str,
    condition: str,
    db: Session = Depends(get_db)
):
    try:
        # Call the function to update the column dynamically
        return update_column_in_table(db, table_name, column_name, new_value, condition)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))