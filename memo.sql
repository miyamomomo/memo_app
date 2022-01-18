CREATE TABLE posts (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    content TEXT
);

INSERT INTO posts(title,content)
    VALUES
    ("挨拶","こんにちは")