-- Schema and data for I14 SQL Question

CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept_id INTEGER,
    role TEXT NOT NULL,
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE secure_vault (
    record_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    secret_value TEXT NOT NULL,
    FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
);

INSERT INTO departments (dept_id, name) VALUES
(101, 'Human Resources'),
(102, 'Finance'),
(103, 'Cyber Security'),
(104, 'Logistics');

INSERT INTO employees (emp_id, name, dept_id, role) VALUES
(1, 'Alice Smith', 101, 'HR Manager'),
(2, 'Bob Jones', 102, 'Accountant'),
(3, 'Charlie Stone', 103, 'Department Head'),
(4, 'David Evans', 103, 'Security Analyst'),
(5, 'Eve Adams', 104, 'Supply Lead');

INSERT INTO secure_vault (record_id, emp_id, secret_value) VALUES
(1, 1, 'Standard HR insurance document'),
(2, 2, 'Fiscal quarter report Q3'),
(3, 3, 'flag{relational database joined}'),
(4, 4, 'Intrusion detection rule pack 2026'),
(5, 5, 'Warehouse delivery manifest');
