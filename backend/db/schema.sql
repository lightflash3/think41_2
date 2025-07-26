CREATE TABLE distribution_centers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    age INTEGER,
    gender VARCHAR(10),
    state VARCHAR(50),
    street_address VARCHAR(255),
    postal_code VARCHAR(20),
    city VARCHAR(50),
    country VARCHAR(50),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    traffic_source VARCHAR(50),
    created_at TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    cost NUMERIC,
    category VARCHAR(50),
    name VARCHAR(100),
    brand VARCHAR(50),
    retail_price NUMERIC,
    department VARCHAR(50),
    sku VARCHAR(50),
    distribution_center_id INTEGER REFERENCES distribution_centers(id)
);

CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    created_at TIMESTAMP,
    sold_at TIMESTAMP,
    cost NUMERIC,
    product_category VARCHAR(50),
    product_name VARCHAR(100),
    product_brand VARCHAR(50),
    product_retail_price NUMERIC,
    product_department VARCHAR(50),
    product_sku VARCHAR(50),
    product_distribution_center_id INTEGER
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(50),
    gender VARCHAR(10),
    created_at TIMESTAMP,
    returned_at TIMESTAMP,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    num_of_item INTEGER
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    inventory_item_id INTEGER REFERENCES inventory_items(id),
    status VARCHAR(50),
    created_at TIMESTAMP,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    returned_at TIMESTAMP
);
