# This file is where I convert mp3 files I have downloaded into wave files
# Should make it easier for me to preprocess the music before controlling
# the relays. If all else fails, I can still play the files through
# omxplayer
#
# Author: Jason C. Nucciarone
# Drafted: 7/18/2019

from os import path
from pydub import AudioSegment

# Create a function that controls the main converting loop
def convert():
    # Ask user for filepath to mp3 files
    print("Please insert path to mp3 files as 'path/to/file/'\n")
    path_to_mp3 = input("Path to mp3 files: ")
    print("\n")

    # Ask user for file where they want to store wave files
    print("Please insert path to desired destination for wave files as 'path/to/file/'\n")
    path_to_wave = input("Destination for wave files: ")
    print("\n")

    # Ask user for .txt files with song names in them
    # Txt files will be stored in the same directory as this program
    print("Please insert txt file as 'songnames.txt'\n")
    song_names = input("Insert txt file containing song names here: ")
    print("\n")

    # Open loop that runs until all song names have been read
    with open(song_names, "r") as file:
        line_from_file = file.readline()

        # So we also get the first line of the txt file
        line_from_file = line_from_file.rstrip('\n')  # remove newline character
        # Add appropriate file name extensions
        song_mp3 = line_from_file + ".mp3"
        song_wave = line_from_file + ".wav"

        # Create path_to_song and path_to_output by
        # concatenating path and song together
        path_to_song = path_to_mp3 + song_mp3
        path_to_output = path_to_wave + song_wave

        # try and except statement to catch if something is wrong
        try:
            # Import song as mp3
            sound = AudioSegment.from_file(path_to_song, format="mp3")

            # Export song as wave
            file_handle = sound.export(path_to_output, format="wav")
        except IOError:
            print("Something went wrong!")

        for line_from_file in file:
            line_from_file = line_from_file.rstrip('\n')  # remove newline character
            # Add appropriate file name extensions
            song_mp3 = line_from_file + ".mp3"
            song_wave = line_from_file + ".wave"

            # Create path_to_song and path_to_output by
            # concatenating path and song together
            path_to_song = path_to_mp3 + song_mp3
            path_to_output = path_to_wave + song_wave

            # try and except statement to catch if something is wrong
            try:
                # Import song as mp3
                sound = AudioSegment.from_file(path_to_song, format="mp3")

                # Export song as wave
                file_handle = sound.export(path_to_output, format="wave")
            except IOError:
                print("Something went wrong!")


# Loop to call function
if __name__=="__main__":
    try:
        convert()
    except KeyboardInterrupt:
        exit()
