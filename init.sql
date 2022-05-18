CREATE TABLE public.database_olx
(
    id    VARCHAR(255) PRIMARY KEY,
    name  VARCHAR(200),
    price REAL,
    state VARCHAR(5),
    search VARCHAR(100),
    ddd   INTEGER,
    cep   VARCHAR(100),
    image VARCHAR(255)
)
