SELECT 
    users.username,
    users.email,
    posts.content,
    posts.created_at
FROM posts
JOIN users ON posts.user_id = users.user_id
WHERE posts.post_id <= 5;
