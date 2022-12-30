# Eksamen i ITF10219 1 Programmering 1, 9. desember 2022
# Karakter: A

# Oppgave 3.1
def convert_seconds_to_minutes(song_duration):
    song_duration = (song_duration // 60, song_duration % 60)
    return song_duration

# Oppgave 3.2
def print_song_description(song):
    song_duraton = convert_seconds_to_minutes(song[2])
    print(f"Title: {song[0]}")
    print(f"Artist: {song[1]}")
    print(f"Duration: {song_duration[0]} min, {song_duration[1]} seconds")

# Oppgave 3.3
def create_song(title, artist, duration, album_title):
    if duration <= 0:
        print("Duration must be at least 1 second.")
        return
    if artist.casefold() == "dingus":
        print("Dingus is banned from  making songs.")
        return     
    new_song = {
        "title": title,
        "artist": artist,
        "duration": duration,
        "album_title": album_title
    }
    return new_song

# Oppgave 3.4
def count_songs_by_artists(playlist):
    num_songs_by_artists = {}
    for song in playlist:
        num_songs_by_artists.update({song["artist"]: num_songs_by_artists.setdefault(song["artist"], 0) + 1})
    return num_songs_by-artists

# Oppgave 3.5
from random import shuffle

def create_shuffled_playlist(playlist):
    new_playlist = playlist.copy()
    shuffle(new_playlist)
    return new_playlist

# oppgave 3.6
import json

def read_album_from_json_file(album_title, filename):
    try:
        with open(filename, "rt") as file:
            data = json.loads(file.read())
    except:
        print("Error when trying to read from file.")
        return
    try:
        album = data[album_title]
        return album
    except KeyError:
        print("Album does not exist.")
        return
