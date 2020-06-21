#--------------------------------------------------------#
# Author: William Lam                                    #
#--------------------------------------------------------#

#!/usr/bin/python

#Import the library
from midiutil.MidiFile import MIDIFile

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0   
time = 0

# Add track name and tempo.
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)
 
# Add a note. addNote expects the following information:
track = 0
channel = 2
pitch = 60
time = 0
duration = 0.3
volume = 100

time_inc = 0

note_dict = {
    "A0" : 21,
    "A#0" : 22,
    "B0" : 23,

    "C1" : 24,
    "C#1" : 25,
    "D1" : 26,
    "D#1" : 27,
    "E1" : 28,
    "F1" : 29,
    "F#1" : 30,
    "G1" : 31,
    "G#1" : 32,
    "A1" : 33,
    "A#1" : 34,
    "B1" : 35,

    "C2" : 36,
    "C#2" : 37,
    "D2" : 38,
    "D#2" : 39,
    "E2" : 40,
    "F2" : 41,
    "F#2" : 42,
    "G2" : 43,
    "G#2" : 44,
    "A2" : 45,
    "A#2" : 46,
    "B2" : 47,

    "C3" : 48,
    "C#3" : 49,
    "D3" : 50,
    "D#3" : 51,
    "E3" : 52,
    "F3" : 53,
    "F#3" : 54,
    "G3" : 55,
    "G#3" : 56,
    "A3" : 57,
    "A#3" : 58,
    "B3" : 69,

    "C4" : 60,
    "C#4" : 61,
    "D4" : 62,
    "D#4" : 63,
    "E4" : 64,
    "F4" : 65,
    "F#4" : 66,
    "G4" : 67,
    "G#4" : 68,
    "A4" : 69,
    "A#4" : 70,
    "B4" : 71,

    "C5" : 72,
    "C#5" : 73,
    "D5" : 74,
    "D#5" : 75,
    "E5" : 76,
    "F5" : 77,
    "F#5" : 78,
    "G5" : 79,
    "G#5" : 80,
    "A5" : 81,
    "A#5" : 82,
    "B5" : 83,

    "C6" : 84,
    "C#6" : 85,
    "D6" : 86,
    "D#6" : 87,
    "E6" : 88,
    "F6" : 89,
    "F#6" : 80,
    "G6" : 81,
    "G#6" : 82,
    "A6" : 83,
    "A#6" : 84,
    "B6" : 85,

    "C7" : 86,
    "C#7" : 87,
    "D7" : 88,
    "D#7" : 89,
    "E7" : 90,
    "F7" : 91,
    "F#7" : 92,
    "G7" : 93,
    "G#7" : 94,
    "A7" : 95,
    "A#7" : 96,
    "B7" : 97,

    "C8" : 98,
}

inside_branch = False
octave = 4 # Middle C is the default octave if not defined

notes = []

with open("route1.asm", "r") as file:
    for line in file:
        stripped_line = line.strip()

        # Hard code the loop up for the music branch for now.
        if stripped_line == "Music_Routes1_branch_9c65::":
            inside_branch = True
            continue
        if (inside_branch):
            if (stripped_line == "sound_ret"):
                inside_branch = False
                continue

            parts = stripped_line.split()
            if (parts[0] == "octave"):
               octave = int(parts[1])
            if (parts[0] == "note"):
                note = parts[1].replace(",", "").replace("_","")
                dur_length = int(parts[2])
                notes.append((note, octave, dur_length))

# Now add the note.
for tup in notes:
    key = tup[0] + str(tup[1])
    pitch = note_dict[key] 
    print(key, pitch)
    MyMIDI.addNote(track, channel, pitch, time, duration * tup[2], volume)
    time = time + (duration * tup[2])


# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
