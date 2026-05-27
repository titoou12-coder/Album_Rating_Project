DROP DATABASE IF EXISTS album_ratings;
CREATE DATABASE album_ratings;
USE album_ratings;

CREATE TABLE artists(
artist_id INT AUTO_INCREMENT PRIMARY KEY,
artist_name VARCHAR(255) NOT NULL,
previous_names VARCHAR(255),
country VARCHAR (100) NOT NULL,
city VARCHAR (100),
active_from YEAR,
still_active VARCHAR (10)
artist_type VARCHAR(50)
);

CREATE TABLE writers(
writer_id INT AUTO_INCREMENT PRIMARY KEY,
writer_name VARCHAR(255) NOT NULL,
country VARCHAR (100) NOT NULL
);

CREATE TABLE producers(
producer_id INT AUTO_INCREMENT PRIMARY KEY,
producer_name VARCHAR(255) NOT NULL,
country VARCHAR (100) NOT NULL
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
release_date DATE,
artist_id INT NOT NULL,
album_ep VARCHAR(10) NOT NULL,
record_label INT (255),
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

CREATE TABLE song_writers(
song_id INT NOT NULL,
writer_id INT NOT NULL,
PRIMARY KEY (song_id, writer_id),
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (writer_id) REFERENCES writers(writer_id)
);

CREATE TABLE song_producers(
song_id INT NOT NULL,
producer_id INT NOT NULL,
PRIMARY KEY (song_id, producer_id),
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (producer_id) REFERENCES producers(producer_id)
);

CREATE TABLE ratings(
song_id INT,
total_score FLOAT AS (
	(lyrics + production + vocals + structure_and_length +
	concept_execution + catchiness_and_memorability + emotional_impact + replay_value) / 8
    ) STORED,
lyrics FLOAT (3,2),
production FLOAT (3,1),
vocals FLOAT (3,1),
structure_and_length FLOAT (3,1),
concept_execution FLOAT (3,1),
catchiness_and_memorability FLOAT (3,1),
emotional_impact FLOAT (3,1),
replay_value FLOAT (3,1),
CONSTRAINT fk_song_id
FOREIGN KEY (song_id) REFERENCES songs(song_id)
);