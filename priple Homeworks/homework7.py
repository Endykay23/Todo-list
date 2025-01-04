
# Song Details

# The artist who performed the song
Artist = "Queen"

# The title of the song
Title = "Bohemian Rhapsody"

# The year the song was released
YearReleased = 1975

# The genre of the song
Genre = "Rock"

# The duration of the song in seconds
DurationInSeconds = 354

# The album in which the song was released
Album = "A Night at the Opera"

# The writer of the song
Writer = "Freddie Mercury"

# The producer of the song
Producer = "Roy Thomas Baker"

# The recording studio where the song was produced
Studio = "Rockfield Studio, Monmouthshire"

# The label that released the song
Label = "EMI"

# The tempo of the song in beats per minute
Tempo = 144

# The time signature of the song
TimeSignature = "4/4"

# The lead vocals in the song
LeadVocals = "Freddie Mercury"

# The date the song was first recorded
DateRecorded = "August 1975"

# The song's chart performance in the UK
UKChartPosition = 1

# The song's chart performance in the US
USChartPosition = 9

# Number of Grammy awards won by the song
GrammyAwardsWon = 2

# Number of MTV awards won by the song
MTVAwardsWon = 1

# The length of the song in minutes
LengthInMinutes = 5.89

# The song's key
Key = "B-flat major"

# Whether the song has an official music video
HasMusicVideo = True

# The director of the music video
MusicVideoDirector = "Bruce Gowers"

# The main theme of the song
MainTheme = "A young man’s despair after committing a crime"

# Song Details Dictionary
song_details = {
    "Artist": "Queen",
    "Title": "Bohemian Rhapsody",
    "YearReleased": 1975,
    "Genre": "Rock",
    "DurationInSeconds": 354,
    "Album": "A Night at the Opera",
    "Writer": "Freddie Mercury",
    "Producer": "Roy Thomas Baker",
    "Studio": "Rockfield Studio, Monmouthshire",
    "Label": "EMI",
    "Tempo": 144,
    "TimeSignature": "4/4",
    "LeadVocals": "Freddie Mercury",
    "DateRecorded": "August 1975",
    "UKChartPosition": 1,
    "USChartPosition": 9,
    "GrammyAwardsWon": 2,
    "MTVAwardsWon": 1,
    "LengthInMinutes": 5.89,
    "Key": "B-flat major",
    "HasMusicVideo": True,
    "MusicVideoDirector": "Bruce Gowers",
    "MainTheme": "A young man’s despair after committing a crime"
}

# Print each key and value in the dictionary
for key, value in song_details.items():
    print(f"{key}: {value}")


def guess_value(key, value):
    if key in song_details and song_details[key] == value:
        return True
    return False

# Example of using the function
key_to_guess = "Artist"
value_to_guess = "Queen"
print(guess_value(key_to_guess, value_to_guess))  # Should return True

key_to_guess = "YearReleased"
value_to_guess = 1980
print(guess_value(key_to_guess, value_to_guess))  # Should return False


"""
This file contains the details of my favorite song.
"""

# Song Details Dictionary
song_details = {
    "Artist": "Queen",
    "Title": "Bohemian Rhapsody",
    "YearReleased": 1975,
    "Genre": "Rock",
    "DurationInSeconds": 354,
    "Album": "A Night at the Opera",
    "Writer": "Freddie Mercury",
    "Producer": "Roy Thomas Baker",
    "Studio": "Rockfield Studio, Monmouthshire",
    "Label": "EMI",
    "Tempo": 144,
    "TimeSignature": "4/4",
    "LeadVocals": "Freddie Mercury",
    "DateRecorded": "August 1975",
    "UKChartPosition": 1,
    "USChartPosition": 9,
    "GrammyAwardsWon": 2,
    "MTVAwardsWon": 1,
    "LengthInMinutes": 5.89,
    "Key": "B-flat major",
    "HasMusicVideo": True,
    "MusicVideoDirector": "Bruce Gowers",
    "MainTheme": "A young man’s despair after committing a crime"
}

# Print each key and value in the dictionary
for key, value in song_details.items():
    print(f"{key}: {value}")

# Function to guess the value of any key
def guess_value(key, value):
    if key in song_details and song_details[key] == value:
        return True
    return False

# Example of using the function
key_to_guess = "Artist"
value_to_guess = "Queen"
print(guess_value(key_to_guess, value_to_guess))  # Should return True

key_to_guess = "YearReleased"
value_to_guess = 1980
print(guess_value(key_to_guess, value_to_guess))  # Should return False
