CREATE database tweets;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON tweets.* TO 'user'@'localhost';
FLUSH privileges;
USE tweets;
CREATE TABLE people (id INT not NUll primary key auto_increment, twitternick CHAR(100), submit TIMESTAMP);
CREATE TABLE tweets (id INT not NULL primary key auto_increment, tweet_id CHAR(100),  submit TIMESTAMP, people_id INT not NULL, foreign key (people_id) references people(id));
