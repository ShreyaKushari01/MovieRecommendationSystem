CREATE DATABASE movie_recommendation;

USE movie_recommendation;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    year INT
);

INSERT INTO movies (title, genre, year) VALUES
('The Dark Knight', 'Action', 2008),
('Inception', 'Sci-Fi', 2010),
('Titanic', 'Romance', 1997),
('The Godfather', 'Crime', 1972),
('The Shawshank Redemption', 'Drama', 1994);

