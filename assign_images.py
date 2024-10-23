import random
from sqlalchemy import create_engine, MetaData, Table
import random
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session

# Database credentials
server_name = "depigroup1" 
database_name = "retail_store" 
username = "omar"  
password = "A1b2c3d4e10&" 

# Create the database engine
engine = create_engine(
    f'mssql+pyodbc://{username}:{password}@{server_name}.database.windows.net:1433/'
    f'{database_name}?driver=ODBC+Driver+18+for+SQL+Server'
)

# Reflect metadata and load products table
metadata = MetaData()
metadata.reflect(bind=engine)
products_table = Table('products', metadata, autoload=True, autoload_with=engine)

# Define images for each category
categories_images = {
    'Athletic Shoes' : [
'https://m.media-amazon.com/images/I/81SlkNo4bKL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51AQVhWkITL._AC_SX625_.jpg'
,'https://m.media-amazon.com/images/I/512pX4ykmfL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/81pl-ouoCcL._AC_UL320_.jpg'
,'https://m.media-amazon.com/images/I/618dNXC87RL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/617RiKGd34L._AC_UL320_.jpg'
    ],
    'Boots' : [
        'https://m.media-amazon.com/images/I/41YwYsX1fvL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51vSZsZ0CJL._AC_SX625_.jpg'
        ,'https://m.media-amazon.com/images/I/41nGSTERjOL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/515cSz-xUFL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/512vMowdj8L._AC_UL320_.jpg','https://m.media-amazon.com/images/I/31n+4eOisHL._AC_UL320_.jpg'
    ],

    'classic' :[
        'https://m.media-amazon.com/images/I/61Uizym5NLL.AC_SL1500.jpg' , 'https://m.media-amazon.com/images/I/71JimHwcnJL._AC_SY625_.jpg'
        ,'https://m.media-amazon.com/images/I/61A3oqUZYqL._AC_SY625_.jpg','https://m.media-amazon.com/images/I/41DivipkNuL._AC_.jpg'
        ,'https://m.media-amazon.com/images/I/61v2v5EcXiL._AC_SX679_.jpg','https://m.media-amazon.com/images/I/71EcDCpQXNL._AC_SY625_.jpg'
    ],

    'Heels' : [
        'https://m.media-amazon.com/images/I/51EPn0lE7HL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51AcAoKbtsL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/51jj2xTyBoL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/41F0QpAukYL._AC_UL320_.jpg'
        , 'https://m.media-amazon.com/images/I/61s8WMyMKfL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/714Oq5dVUuL._AC_UL320_.jpg'
                ],

    'Loafers' : [
        'https://m.media-amazon.com/images/I/61kpLRpEAwL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/41iWyEipcAL._AC_UL320_.jpg'
        , 'https://m.media-amazon.com/images/I/41gi2LWJHbL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/71o7H3XlnIL._AC_UL320_.jpg'
        , 'https://m.media-amazon.com/images/I/41utaFW9ebL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/41dmhudCSVL._AC_UL320_.jpg'
                ],



    'Sandals': [
        'https://m.media-amazon.com/images/I/51MfdSYlCXL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51QFgZ9Il1L._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/51yUI1pgzkL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/7150iyHk7XL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/51V+Psx30ZL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51p4Rt7iPXL._AC_UL320_.jpg'
     
        ],
    'Sneakers' : [
        'https://m.media-amazon.com/images/I/51y607p-h4L._AC_UL320_.jpg','https://m.media-amazon.com/images/I/81UF7LjuqxL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/61QENo259UL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51aDjqzpUpL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/51eJ9YnkuYL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/410UM8iMwNL._AC_UL320_.jpg'

    ],
    'Slippers': [
        'https://m.media-amazon.com/images/I/71BdQJi+URL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51o+hgnvydL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/41sfg3aGM-L._AC_UL320_.jpg','https://m.media-amazon.com/images/I/51xen+wiNLL._AC_UL320_.jpg'
        ,'https://m.media-amazon.com/images/I/619XlaOlKxL._AC_UL320_.jpg','https://m.media-amazon.com/images/I/41FZ4FEAKDL._AC_UL320_.jpg'

    ],
    # Add more categories as needed...
}

# Assign random images to products by category
# Assign random images to products by category
with Session(engine) as session:
    for category, images in categories_images.items():
        # Select products with the matching category
        select_query = select(products_table).where(products_table.c.category == category)
        products = session.execute(select_query).fetchall()

        for product in products:
            # Assign a random image to the product
            random_image = random.choice(images)
            update_query = (
                update(products_table)
                .where(products_table.c.product_id == product.product_id)
                .values(product_image=random_image)
            )
            session.execute(update_query)

    session.commit()

print("Product images updated successfully.")


