-- create database
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- switch to db

USE tyrell_corp;

-- create table
CREATE TABLE IF NOT EXISTS nexus6 (
    id      INT             NOT NULL        AUTO_INCREMENT      PRIMARY KEY,
    name    VARCHAR(256)
);

-- insert data
INSERT INTO nexus6 (name)
VALUES ("name");
