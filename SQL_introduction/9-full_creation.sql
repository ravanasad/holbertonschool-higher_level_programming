-- creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
    ID INT,
    NAME VARCHAR(256),
    SCORE INT
);

INSERT INTO second_table (`ID`, `NAME`, `SCORE`) VALUES (1, 'John', 10);
INSERT INTO second_table (`ID`, `NAME`, `SCORE`) VALUES (2, 'Alex', 3);
INSERT INTO second_table (`ID`, `NAME`, `SCORE`) VALUES (3, 'Bob', 14);
INSERT INTO second_table (`ID`, `NAME`, `SCORE`) VALUES (4, 'George', 8);