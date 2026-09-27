-- Database schema for A08
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    secret_flag TEXT
);

INSERT INTO users (id, username, password, secret_flag) VALUES
(1, 'admin', 'SuperComplexHashP@ssword2026!#$%', 'flag{sql_injection_master}'),
(2, 'guest', 'guestpass', 'No flag here');
