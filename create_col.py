from enum import Enum
from sqlalchemy import text, Column, Integer, String, Float, Boolean, MetaData, Table, VARCHAR
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