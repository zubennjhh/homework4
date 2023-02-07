PRIMARY KEY


   CREATE TABLE products (
       product_id INTEGER PRIMARY KEY,
       name TEXT,
       descr TEXT,
       prise INTEGER,
       photo TEXT
  )

   CREATE TABLE order (
       order_id INTEGER PRIMARY KEY,
       name TEXT,
       userid INTEGER,
       address TEXT,
       product_id INTEGER,
       FOREIGN KEY (product_id)
          REFERENCES products(product_id)
   )



   INSERT INTO products (
        name,
        descr,
        price,
        photo
   ) VALUES
   ('кроссовки', 'li-ning', 200, '/images/gg.jpg'),
   ('ботинки', 'зимние', 199, '/images/gg.jpg'),


   SELECT * FROM name FROM products
