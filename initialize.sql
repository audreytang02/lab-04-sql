
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at DATETIME
);


CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    content TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


INSERT INTO users VALUES (1, 'alice', 'alice@example.com', NOW());
INSERT INTO users VALUES (2, 'bob', 'bob@example.com', NOW());
INSERT INTO users VALUES (3, 'charlie', 'charlie@example.com', NOW());
INSERT INTO users VALUES (4, 'diana', 'diana@example.com', NOW());
INSERT INTO users VALUES (5, 'eric', 'eric@example.com', NOW());
INSERT INTO users VALUES (6, 'fiona', 'fiona@example.com', NOW());
INSERT INTO users VALUES (7, 'george', 'george@example.com', NOW());
INSERT INTO users VALUES (8, 'hannah', 'hannah@example.com', NOW());
INSERT INTO users VALUES (9, 'ian', 'ian@example.com', NOW());
INSERT INTO users VALUES (10, 'julia', 'julia@example.com', NOW());


INSERT INTO posts VALUES (1, 1, 'Alice first post', NOW());
INSERT INTO posts VALUES (2, 2, 'Bob says hello', NOW());
INSERT INTO posts VALUES (3, 3, 'Charlie has class', NOW());
INSERT INTO posts VALUES (4, 4, 'Diana writes a post', NOW());
INSERT INTO posts VALUES (5, 5, 'Eric is learning databases', NOW());
INSERT INTO posts VALUES (6, 6, 'Fiona shares a story', NOW());
INSERT INTO posts VALUES (7, 7, 'George posts something', NOW());
INSERT INTO posts VALUES (8, 8, 'Hannah writes a message', NOW());
INSERT INTO posts VALUES (9, 9, 'Ian posts a short note', NOW());
INSERT INTO posts VALUES (10, 10, 'Julia finishes her post', NOW());
