import sqlalchemy as db

engine = db.create_engine("sqlite:///product.db")

connection = engine.connect()

metadata = db.MetaData()

products = db.Table(
	'Products',
	metadata,
	db.Column('product_id', db.Integer, primary_key=True),
	db.Column('product_name', db.Text),
	db.Column('supplier_name', db.Text),
	db.Column('price', db.Integer))

metadata.create_all(engine)


insert_query = products.insert().values([
	{"product_name": "Banana", "supplier_name": "United Bananas", "price":7000},
	{"product_name": "Date", "supplier_name": "EcoSys", "price":3000},
	{"product_name": "Granet", "supplier_name": "TurkFruct", "price":8000},
])

connection.execute(insert_query)

select_all_query = db.select(products)
select_all_result = connection.execute(select_all_query)

print(select_all_result.fetchall())

select_price_query = db.select(products).where(products.columns.price==8000)
select_price_result = connection.execute(select_price_query)

print(select_price_result.fetchall())
