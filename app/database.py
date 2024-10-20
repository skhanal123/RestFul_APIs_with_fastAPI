from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Skhanal%40123@localhost:5433/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             port="5433",
#             user="postgres",
#             password="Skhanal@123",
#             cursor_factory=RealDictCursor,
#         )

#         cursor = conn.cursor()
#         print("Database connection was successfull")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

# my_posts = [
#     {"id": 1, "title": "api", "post": "content_post api"},
#     {"id": 2, "title": "api2", "post": "content_post_api2"},
# ]


# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post


# def find_index(id):
#     for index, post in enumerate(my_posts):
#         if post["id"] == id:
#             return index


# @app.get("/test")
# async def test_get(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts)
#     return {"data": posts}
