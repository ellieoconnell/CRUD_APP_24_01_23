-- creating a database table 
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(10) NO NULL,
    drink_type VARCHAR(15) NO NULL,
    drink_size VARCHAR(10) NO NULL,
    cream BOOLEAN NOT NULL,
    drink_amount INT NOT NULL
);

-- inserting test entiries into the table 
INSERT INTO orders (first_name, drink_type, drink_size, cream, drink_amount) VALUES ("Jeff", "Latte", "Large", False, 1);
INSERT INTO orders (first_name, drink_type, drink_size, cream, drink_amount) VALUES ("Samantha", "Mocha", "Large", True, 1);
INSERT INTO orders (first_name, drink_type, drink_size, cream, drink_amount) VALUES ("Sarah", "Latte", "Small", False, 2);
INSERT INTO orders (first_name, drink_type, drink_size, cream, drink_amount) VALUES ("Tina", "Cappuccino", "Medium", False, 1);