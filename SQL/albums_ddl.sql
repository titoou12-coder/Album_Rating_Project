DROP DATABASE IF EXISTS album_ratings;
CREATE DATABASE album_ratings;
USE album_ratings;

CREATE TABLE artists(
artist_id INT AUTO_INCREMENT PRIMARY KEY,
artist_name VARCHAR(255) NOT NULL,
country VARCHAR (100) NOT NULL,
city VARCHAR (100),
active_from YEAR,
still_active BOOLEAN
);

CREATE TABLE artist_aliases (
alias_artist_id INT NOT NULL,
primary_artist_id INT NOT NULL,
PRIMARY KEY (alias_artist_id),
FOREIGN KEY (alias_artist_id) REFERENCES artists(artist_id),
FOREIGN KEY (primary_artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE artist_previous_names (
name_id INT AUTO_INCREMENT NOT NULL,
previous_name VARCHAR (255) NOT NULL,
artist_id INT NOT NULL,
PRIMARY KEY (name_id, artist_id),
FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE band_members(
member_id INT AUTO_INCREMENT,
band_id INT NOT NULL,
role VARCHAR(50),
active_from YEAR,
departure YEAR,
PRIMARY KEY (member_id, band_id),
FOREIGN KEY (member_id) REFERENCES artists(artist_id),
FOREIGN KEY (band_id) REFERENCES artists(artist_id)
);

CREATE TABLE record_labels(
label_id INT AUTO_INCREMENT PRIMARY KEY,
label_name VARCHAR (100) NOT NULL,
parent_label_id INT,
FOREIGN KEY (parent_label_id) REFERENCES record_labels(label_id)
);

CREATE TABLE albums(
album_id INT AUTO_INCREMENT PRIMARY KEY,
album_name VARCHAR(255) NOT NULL,
artist_id INT NOT NULL,
release_date DATE,
album_ep VARCHAR(10) NOT NULL,
record_label INT,
CONSTRAINT fk_artist_id
FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
FOREIGN KEY (record_label) REFERENCES record_labels(label_id)
);

CREATE TABLE songs(
song_id INT AUTO_INCREMENT PRIMARY KEY,
song_name VARCHAR (255) NOT NULL,
album_id INT NOT NULL,
track_number INT NOT NULL,
single VARCHAR(3),
genre VARCHAR(255),
CONSTRAINT fk_album_id
FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

CREATE TABLE song_artists(
song_id INT NOT NULL,
artist_id INT NOT NULL,
role VARCHAR(50),
PRIMARY KEY (song_id, artist_id),
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE ratings(
song_id INT PRIMARY KEY,
total_score DECIMAL AS (
	(lyrics + production + vocals + structure_and_length +
	concept_execution + catchiness_and_memorability + emotional_impact + replay_value) / 8
    ) STORED,
lyrics DECIMAL (3,2),
production DECIMAL (3,1),
vocals DECIMAL (3,1),
structure_and_length DECIMAL (3,1),
concept_execution DECIMAL (3,1),
catchiness_and_memorability DECIMAL (3,1),
emotional_impact DECIMAL (3,1),
replay_value DECIMAL (3,1),
CONSTRAINT fk_song_id
FOREIGN KEY (song_id) REFERENCES songs(song_id)
);