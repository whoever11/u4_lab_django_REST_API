-- settings.sql
CREATE DATABASE sports_league;
CREATE USER sports_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE sports_league TO sports_user;
