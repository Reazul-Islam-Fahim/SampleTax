from fastapi import FastAPI, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://192.168.2.33:5173",
    # "https://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)



@app.post("/user_auth/", response_model=schemas.User_Auth)
def create_user_auth(user_auth: schemas.User_Auth = Body(...), db: Session = Depends(get_db)): #Body(...) can be use instead of Query(...) for json format
    return crud.create_user_auth(db=db, user_auth=user_auth)


@app.put("/user_auth/{id}", response_model=schemas.User_Auth)
async def update_user_auth_endpoint(
    id: int,
    updated_user_auth: schemas.User_Auth,
    db: Session = Depends(get_db),
):

    updated_record = crud.update_tax_payer(db, id, updated_user_auth)

    if not updated_record:
        raise HTTPException(status_code=404, detail="UserAuth record not found")

    return updated_record


@app.get("/user_auth/{user_auth_id}", response_model=schemas.User_Auth)
def read_user_auth(id: int, db: Session = Depends(get_db)):
    db_item = crud.get_user_auth(db, id= id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/user_auth/", response_model=list[schemas.User_Auth])
def read_user_auths(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_user_auths(db, skip=skip, limit=limit)
    return items