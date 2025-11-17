CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);

INSERT INTO usuarios (nome) VALUES 
    ('Lucas Sukar'),
    ('Caio Lima'),
    ('Rodrigo');
