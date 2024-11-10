from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import Session
from db import get_db, engine  # Assuming you have a DB connection setup in 'db.py'

app = FastAPI()

# Create metadata instance
metadata = MetaData()

@app.post("/drop_table/")
def drop_table(table_name: str, db: Session = Depends(get_db)):
    try:
        # Reflect the table using SQLAlchemy's MetaData and engine
        table = Table(table_name, metadata, autoload_with=engine)
        
        # Drop the table
        table.drop(engine)

        return {"detail": f"Table '{table_name}' has been dropped successfully."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error dropping table: {str(e)}")



@app.post("/create_table/")
def create_table(table_name : str = Query(...), db: Session = Depends(get_db)):
    try:
        # Initialize metadata for new table
        metadata = MetaData()
        
        # Prepare a list to hold column definitions
        columns = []
        
        
        # Define the new table dynamically
        new_table = Table(table_name, metadata)

        # Create the table in the database (this will create an empty table)
        new_table.create(bind=engine)

        return {"detail": f"Table '{table_name}' has been created successfully with {len(columns)} columns."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating table: {str(e)}")
    
    
def get_table_structure(table_name: str, db: Session):
    try:
        # Reflect the existing table from the database
        metadata = MetaData(bind=db.bind)
        table = Table(table_name, metadata, autoload_with=db.bind)
        
        # Extract column details
        columns = []
        for column in table.columns:
            columns.append({
                "name": column.name,
                "type": str(column.type),
                "nullable": column.nullable,
                "default": column.default,
                "primary_key": column.primary_key,
            })
        
        return columns
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching table structure: {str(e)}")


@app.get("/get_table/{table_name}")
def get_table(table_name: str, db: Session = Depends(get_db)):
    """Get the structure of a table (columns, types, etc.)"""
    columns = get_table_structure(table_name, db)
    if not columns:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")
    return {"table_name": table_name, "columns": columns}
    
