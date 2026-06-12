import csv
import pandas as pd
import math


def get_album_name():
    album_name = input("\nWhat is the name of the album you are rating?: ")
    return album_name


def get_csv_title(album_name):
    if " " in album_name:
        csv_title = album_name.replace(" ", "")
    else:
        csv_title = album_name
    return csv_title


def get_artist(album_name):
    album_artist = input(f"Who is {album_name} by?: ")
    country = input(f"What country is {album_artist} from? ").title
    city = input(f"What city is {album_artist} from? ").title
    active_from = int(
        input(f"What year did {album_artist} become active from? "))
    still_active = bool(input(f"Is {album_artist} still active? "))
    return album_artist, country, city, active_from, still_active


def prev_names(artist):
    question = input(f"Has {artist} released music under any other name? ")
    if question.lower() == "no":
        return False
    else:
        prev_names = []
        while True:
            prev_name_q = input("What is a previous name of this artist? ")
            prev_names.append(prev_name_q)
            question2 = input(
                f"Are there any other names {artist} has released music under? ")
            if question2.lower() == "no":
                return prev_names


def get_csv_artist(album_artist):
    if " " in album_artist:
        csv_artist = album_artist.replace(" ", "")
    else:
        csv_artist = album_artist
    return csv_artist


def release_year(album_name):
    release_year = int(input(f"What year was {album_name} released in? "))
    return release_year


def get_tracklist():
    number_of_tracks = int(input("How many tracks are in this album? "))
    print("\n")
    tracklist = []
    for song in range(number_of_tracks):
        song_name = input("What is the name of song " +
                          str(song + 1) + "? ")
        tracklist.append(song_name)
    return tracklist


album_name = get_album_name()
artist_name = get_artist(album_name)
print(prev_names(artist_name))
album_year = release_year(album_name)
tracklist = get_tracklist()


header = ["Song Name", "Total Score", "Lyrics", "Production", "Vocals", "Song Structure and Length",
          "Concept Execution", "Catchiness/Memorability", "Emotional Impact", "Replay Value"]

"""
with open(f"/Users/titooukah/Documents/PythonProjects/AlbumProject/albums/{get_csv_title(album_name)}_{get_csv_artist(artist_name)}.csv", mode="a+", newline="") as album_file:
    album_writer = csv.DictWriter(
        album_file, fieldnames=header)
    album_writer.writeheader()  # add header data (columns)

    data = []

    for song_name in tracklist:
        print(f"\nRating of {song_name}: \n")
        dictionary = {"Song Name": f"{song_name}", "Total Score": 0}

        total_score = 0

        for category in header:
            if category == "Song Name":
                pass
            elif category == "Total Score":
                pass
            else:
                score = float(input(f"{category}: "))
                dictionary.update({f"{category}": score})
                total_score += score

        total_score = round(total_score/8, 2)
        dictionary.update({"Total Score": total_score})
        data.append(dictionary)

    album_writer.writerows(data)
"""

# Open and read the file OR Create File
# try:
artist_tracks = []
for dictionary in data:
    artist_tracks.append(dictionary.values())
with open(f"/Users/titooukah/Documents/PythonProjects/AlbumProject/artists/{get_csv_artist(artist_name)}_full.csv", "a+") as song_discography:
    song_discography.seek(0)
    first_char = song_discography.read(1)
    if not first_char:
        artist_writer = csv.DictWriter(
            song_discography, fieldnames=header)
        artist_writer.writeheader()
        artist_writer.writerows(data)
    else:
        artist_writer = csv.writer(song_discography)
        for track in artist_tracks:
            artist_writer.writerow(track)


# except FileNotFoundError:
#  with open(f"/Users/titooukah/Documents/PythonProjects/Album\
# Project/artists/{csv_artist}_full.csv", mode='w', newline="") as song_discography:
#       pass

# with open(f"/Users/titooukah/Documents/PythonProjects/Album\
# Project/artists/{csv_artist}_full.csv", newline="") as song_discography:

# Create an empty list
# artist_tracks = []

# Read the file and add existing rows to list
# artist_reader = csv.DictReader(song_discography)
# for row in artist_reader:
#    artist_tracks.append(row)
# print("Existing tracks are", artist_tracks)
#
# Else create a new file

#    with open(f"/Users/titooukah/Documents/PythonProjects/Album\
# Project/artists/{csv_artist}_full.csv", mode="w", newline="") as full_artist_file:

# Create and write header
#       artist_writer = csv.DictWriter(
#          full_artist_file, fieldnames=header)
#     artist_writer.writeheader()
# Write in rows of album just rated
#    artist_writer.writerows(data)


# with open(f"/Users/titooukah/Documents/PythonProjects/Album\
# Project/artists/{csv_artist}_summary.csv", mode="w", newline="") as summary_artist_file:
#    header = ["Album Name", "Release Year", "Score"]
#    csv.DictWriter(summary_artist_file, fieldnames=header)
#   dictionary = {}
