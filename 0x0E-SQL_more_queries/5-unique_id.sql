-- script that creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    UNIQUE (id),
    name VARCHAR(256) NOT NULL
);