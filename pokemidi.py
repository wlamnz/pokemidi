#!/usr/bin/python

#--------------------------------------------------------#
# Author: William Lam                                    #
#--------------------------------------------------------#

#Import the library
from midiutil.MidiFile import MIDIFile

# TODO make script take in a filename
filePath = "music/trainerbattle.asm" 

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0   
time = 0

# Add track name and tempo.
MyMIDI.addTrackName(track, time, "Sample Track")
 
# Add a note. addNote expects the following information:
#track, channel, pitch, time, duration, volume

channel = 2
dur_unit = 0.16
volume = 100 

# Keep track of all the music branches (and their content)
branches_dict = {}

class ChannelDetail:
    def __init__(self, channel):
        self.channel = channel
        self.time = 0
        self.note_tuples = []
        self.branches = []

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
    "B3" : 59,

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
    "F#6" : 90,
    "G6" : 91,
    "G#6" : 92,
    "A6" : 93,
    "A#6" : 94,
    "B6" : 95,

    "C7" : 96,
    "C#7" : 97,
    "D7" : 98,
    "D#7" : 99,
    "E7" : 100,
    "F7" : 101,
    "F#7" : 102,
    "G7" : 103,
    "G#7" : 104,
    "A7" : 105,
    "A#7" : 106,
    "B7" : 107,

    "C8" : 108,
}

def add_to_note_tuples(branch_name, cd):
    sound_call_branches = []
    for v in branches_dict[branch_name]:
        # If the value is a string. It must be a sound_call instruction 
        if isinstance(v, basestring):
            sound_call_branches.extend(add_to_note_tuples(v, cd))
            sound_call_branches.append(v)
        else:
            # The value is already a note tuple, add it to the list.
            cd.note_tuples.append(v)
    return sound_call_branches

octave = 4 # Middle C is the default octave if not defined
channel_details = []
current_channel = None 

# Assumption: sound call is only made on music branch
current_branch = None

tempo = 120

with open(filePath, "r") as file:
    for line in file:
        stripped_line = line.strip()

        # Either a new channel or new branch 
        if stripped_line.startswith("Music"):
            octave = 4 # Always reset the octave when we start a new music branch or channel
            parts = stripped_line.split("_");

            if parts[-1].startswith("Ch"):
                # This is a new channel. Create a new channel detail.
                channel = len(channel_details) + 1
                print("Created new channel " + str(channel))
                current_channel = ChannelDetail(channel)
                channel_details.append(current_channel)
                current_branch = None
            
            if parts[-2].startswith("branch") and current_channel != None:
                current_branch = stripped_line[0:len(stripped_line) - 2]
                # Keep track of the branch order and initialise their list
                current_channel.branches.append(current_branch)
                branches_dict[current_branch] = []

            continue

        if stripped_line == "sound_ret":
            continue

        if current_channel == None:
            continue

        parts = stripped_line.split()
        if len(parts) == 0:
            continue

        if parts[0] == "octave":
            octave = int(parts[1])
        elif parts[0] == "note":
            note = parts[1].replace(",", "").replace("_","")
            dur_length = int(parts[2])
            tup = (note, octave, dur_length)
            if current_branch != None:
                branches_dict[current_branch].append(tup)
            else:
                current_channel.note_tuples.append(tup)
        elif parts[0] == "rest":
            dur_length = int(parts[1])
            tup = (0, -1, dur_length)
            if current_branch != None:
                branches_dict[current_branch].append(tup)
            else:
                current_channel.note_tuples.append(tup)
        elif parts[0] == "sound_call":
            if current_branch != None:
                # Add the call branch 
                branches_dict[current_branch].append(parts[1])
        elif parts[0] == "tempo":
            tempo = int(parts[1])

print 'Tempo used ' + str(tempo)
MyMIDI.addTempo(track, time, tempo) 

# Add the notes to the midi file
for cd in channel_details:
    sound_call_branches = []

    for branch in cd.branches:
        if branch in sound_call_branches:
            # Assumption: sound call branches are never main music branches
            continue
            
        # Add all note tuples into the cd.note_tuples list
        sound_call_branches.extend(add_to_note_tuples(branch, cd))

    for tup in cd.note_tuples:
        note = tup[0]
        octave = tup[1]
        dur_length = tup[2];
        pitch = 255 
        duration = dur_unit * dur_length # duration is calculated by unit * length

        # Octave is -1 when a rest opcode is found
        if octave != -1:
            key = note + str(octave)
            pitch = note_dict[key] 
            #print(key, pitch)
            MyMIDI.addNote(track, cd.channel, pitch, cd.time, duration, volume)

        cd.time = cd.time + duration

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
