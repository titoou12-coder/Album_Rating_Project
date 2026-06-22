import csv
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
    artist_data = {}
    artist_data["artist_name"] = input(f"Who is {album_name} by?: ")
    artist_data["country"] = input(
        f"What country is {artist_data['artist_name']} from? ").title()
    artist_data["city"] = input(
        f"Which city? ").title()
    artist_data["active_from"] = int(
        input(f"What year did {artist_data['artist_name']} become active from? "))
    artist_data["still_active"] = (
        input(
            f"Is {artist_data['artist_name']} still active? (yes/no): ").lower() == "yes"
    )
    return artist_data


def artist_other_names(artist):
    name_data = {
        "artist_name": artist,
        "rebrands": [],
        "aliases": []
    }

    # REBRANDS
    if input(f"Has {artist} changed their name over time? (yes/no): ").lower() == "yes":
        while True:
            name_data["rebrands"].append(input("Enter name used: "))
            if input("More rebrands? (yes/no): ").lower() == "no":
                break

    # ALIASES
    if input(f"Does {artist} use any aliases? (yes/no): ").lower() == "yes":
        while True:
            name_data["aliases"].append(input("Enter alias: "))
            if input("More aliases? (yes/no): ").lower() == "no":
                break

    return name_data


def band(artist):
    if input(f"Is {artist} a solo artist? (yes/no): ").lower() == "yes":
        return []
    else:
        band = []
        while True:
            member = {"band_name": artist}
            member["member_name"] = input(
                f"Name a member of {artist}: ").title()
            member["role"] = input(
                f"What is {member['member_name']}'s primary role in {artist}?: ").lower()
            member["active_from"] = int(
                input(f"What year did {member['member_name']} join {artist}?: "))
            if input(f"Is {member['member_name']} still part of {artist}? (yes/no): ").lower() == "yes":
                member["departure"] = ""
            else:
                member["departure"] = int(
                    input(f"What year did {member['member_name']} leave {artist}?: "))
            band.append(member)
            if input(f"Any more members of {artist}? (yes/no): ").lower() == "no":
                break
    return band


def get_album_info(album_name, artist_name):
    album_info = {"album_name": album_name}
    album_info["artist_name"] = artist_name
    album_info["release_date"] = input(f"When was {album_name} released in? Please give answer in the format MM-YYYY":)
    if input("is this an album or ep?: ").lower == "album":
        album_info["album_ep"] = "Album"
    else:
        album_info["album_ep"] = "EP"
    album_info["record_labels"] = input(
        f"What record label released {album_name}")


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
print(artist_name)
print(artist_other_names(artist_name["artist_name"]))
print(band(artist_name["artist_name"]))
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
