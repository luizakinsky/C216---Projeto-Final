DROP TABLE IF EXISTS "vendas";
DROP TABLE IF EXISTS "albuns";

CREATE TABLE "albuns" (
    "id" SERIAL PRIMARY KEY,
    "titulo" VARCHAR(255) NOT NULL,
    "cantor" VARCHAR(255) NOT NULL,
    "quantidade" INTEGER NOT NULL,
    "preco" FLOAT NOT NULL
);

CREATE TABLE "vendas" (
    "id" SERIAL PRIMARY KEY,
    "album_id" INTEGER REFERENCES albuns(id) ON DELETE CASCADE,
    "quantidade_vendida" INTEGER NOT NULL,
    "valor_venda" FLOAT NOT NULL,
    "data_venda" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "albuns" ("titulo", "cantor", "quantidade", "preco") VALUES ('Thriller', 'Michael Jackson', 15, 50.00);
INSERT INTO "albuns" ("titulo", "cantor", "quantidade", "preco") VALUES ('Back In Black', 'AC/DC', 10, 40.00);
INSERT INTO "albuns" ("titulo", "cantor", "quantidade", "preco") VALUES ('The Bodyguard', 'Whitney Houston', 20, 35.00)