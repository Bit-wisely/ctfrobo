-- SQLite Database Schema and Seed Data for B11

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE classified_vault (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    secret_note TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO users (id, username, role) VALUES
(1, 'alice', 'staff'),
(2, 'bob', 'operator'),
(3, 'charlie', 'administrator'),
(4, 'diana', 'auditor');

INSERT INTO classified_vault (id, user_id, secret_note) VALUES
(1, 1, 'Routine office maintenance log'),
(2, 2, 'Shift handover confirmed for sector 4'),
(3, 3, 'flag{sqlite_vault_revealed}'),
(4, 4, 'Annual system audit complete - all clear');
