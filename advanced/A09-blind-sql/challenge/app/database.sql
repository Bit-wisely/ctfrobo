-- Blind SQL Schema
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT
);

CREATE TABLE secrets (
    id INTEGER PRIMARY KEY,
    secret_val TEXT
);

INSERT INTO users (id, username) VALUES (1, 'admin'), (2, 'alice');
INSERT INTO secrets (id, secret_val) VALUES (1, 'blind sql inference');
