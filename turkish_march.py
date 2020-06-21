#!/usr/bin/python

#--------------------------------------------------------#
# Author: William Lam                                    #
#                                                        #
# Hardcoded addNote test using Turkish March.            #
#--------------------------------------------------------#

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
duration2 = 1.2
volume = 100

time_inc = 0


#---------------------------------------------------------
# Treble
#---------------------------------------------------------

# Now add the note.
MyMIDI.addNote(track,channel,71, 0,   duration,volume)
MyMIDI.addNote(track,channel,69, 0.3, duration,volume)
MyMIDI.addNote(track,channel,68, 0.6, duration,volume)
MyMIDI.addNote(track,channel,69, 0.9, duration,volume)
MyMIDI.addNote(track,channel,72, 1.2, duration2,volume)
MyMIDI.addNote(track,channel,74, 2.4, duration, volume)
MyMIDI.addNote(track,channel,72, 2.7, duration,volume)
MyMIDI.addNote(track,channel,71, 3.0, duration,volume)
MyMIDI.addNote(track,channel,72, 3.3, duration,volume)
MyMIDI.addNote(track,channel,76, 3.6, duration2,volume)
MyMIDI.addNote(track,channel,77, 4.8, duration,volume)
MyMIDI.addNote(track,channel,76, 5.1, duration, volume)
MyMIDI.addNote(track,channel,75, 5.4, duration, volume)
MyMIDI.addNote(track,channel,76, 5.7, duration, volume)
MyMIDI.addNote(track,channel,83, 6.0, duration, volume)
MyMIDI.addNote(track,channel,81, 6.3, duration, volume)
MyMIDI.addNote(track,channel,80, 6.6, duration, volume)
MyMIDI.addNote(track,channel,81, 6.9, duration, volume)
MyMIDI.addNote(track,channel,83, 7.2, duration, volume)
MyMIDI.addNote(track,channel,81, 7.5, duration, volume)
MyMIDI.addNote(track,channel,80, 7.8, duration, volume)
MyMIDI.addNote(track,channel,81, 8.1, duration, volume)
MyMIDI.addNote(track,channel,84, 8.4, duration2, volume)
MyMIDI.addNote(track,channel,81, 9.6, 0.6, volume)
MyMIDI.addNote(track,channel,84, 10.2, 0.6, volume)

MyMIDI.addNote(track,channel,79, 10.8, 0.05, volume)
MyMIDI.addNote(track,channel,81, 10.85, 0.05, volume)
MyMIDI.addNote(track,channel,83, 10.90, 0.5, volume)
MyMIDI.addNote(track,channel,81, 11.4, 0.6, volume)
MyMIDI.addNote(track,channel,78, 11.4, 0.6, volume)
MyMIDI.addNote(track,channel,79, 12.0, 0.6, volume)
MyMIDI.addNote(track,channel,76, 12.0, 0.6, volume)
MyMIDI.addNote(track,channel,81, 12.6, 0.6, volume)
MyMIDI.addNote(track,channel,78, 12.6, 0.6,  volume)

MyMIDI.addNote(track,channel,79, 13.2, 0.05, volume)
MyMIDI.addNote(track,channel,81, 13.25, 0.05, volume)
MyMIDI.addNote(track,channel,83, 13.3, 0.5, volume)
MyMIDI.addNote(track,channel,81, 13.8, 0.6, volume)
MyMIDI.addNote(track,channel,78, 13.8, 0.6, volume)
MyMIDI.addNote(track,channel,79, 14.4, 0.6, volume)
MyMIDI.addNote(track,channel,76, 14.4, 0.6, volume)
MyMIDI.addNote(track,channel,81, 15.0, 0.6, volume)
MyMIDI.addNote(track,channel,78, 15.0, 0.6,  volume)

MyMIDI.addNote(track,channel,79, 15.6, 0.05, volume)
MyMIDI.addNote(track,channel,81, 15.65, 0.05, volume)
MyMIDI.addNote(track,channel,83, 15.7, 0.5, volume)
MyMIDI.addNote(track,channel,81, 16.2, 0.6, volume)
MyMIDI.addNote(track,channel,78, 16.2, 0.6, volume)
MyMIDI.addNote(track,channel,79, 16.8, 0.6, volume)
MyMIDI.addNote(track,channel,76, 16.8, 0.6, volume)
MyMIDI.addNote(track,channel,75, 17.4, 0.6, volume)
MyMIDI.addNote(track,channel,78, 17.4, 0.6,  volume)
MyMIDI.addNote(track,channel,76, 18.0, duration2, volume)

MyMIDI.addNote(track,channel,71, 19.2, duration,volume)
MyMIDI.addNote(track,channel,69, 19.5, duration,volume)
MyMIDI.addNote(track,channel,68, 19.8, duration,volume)
MyMIDI.addNote(track,channel,69, 20.1, duration,volume)
MyMIDI.addNote(track,channel,72, 20.4, duration2,volume)
MyMIDI.addNote(track,channel,74, 21.6, duration, volume)
MyMIDI.addNote(track,channel,72, 21.9, duration,volume)
MyMIDI.addNote(track,channel,71, 22.2, duration,volume)
MyMIDI.addNote(track,channel,72, 22.5, duration,volume)
MyMIDI.addNote(track,channel,76, 22.8, duration2,volume)
MyMIDI.addNote(track,channel,77, 24.0, duration,volume)
MyMIDI.addNote(track,channel,76, 24.3, duration, volume)
MyMIDI.addNote(track,channel,75, 24.6, duration, volume)
MyMIDI.addNote(track,channel,76, 24.9, duration, volume)
MyMIDI.addNote(track,channel,83, 25.2, duration, volume)
MyMIDI.addNote(track,channel,81, 25.5, duration, volume)
MyMIDI.addNote(track,channel,80, 25.8, duration, volume)
MyMIDI.addNote(track,channel,81, 26.1, duration, volume)
MyMIDI.addNote(track,channel,83, 26.4, duration, volume)
MyMIDI.addNote(track,channel,81, 26.7, duration, volume)
MyMIDI.addNote(track,channel,80, 27.0, duration, volume)
MyMIDI.addNote(track,channel,81, 27.3, duration, volume)
MyMIDI.addNote(track,channel,84, 27.6, duration2, volume)
MyMIDI.addNote(track,channel,81, 28.8, 0.6, volume)
MyMIDI.addNote(track,channel,84, 29.4, 0.6, volume)

MyMIDI.addNote(track,channel,79, 30.0, 0.05, volume)
MyMIDI.addNote(track,channel,81, 30.05, 0.05, volume)
MyMIDI.addNote(track,channel,83, 30.1, 0.5, volume)
MyMIDI.addNote(track,channel,81, 30.6, 0.6, volume)
MyMIDI.addNote(track,channel,78, 30.6, 0.6, volume)
MyMIDI.addNote(track,channel,79, 31.2, 0.6, volume)
MyMIDI.addNote(track,channel,76, 31.2, 0.6, volume)
MyMIDI.addNote(track,channel,81, 31.8, 0.6, volume)
MyMIDI.addNote(track,channel,78, 31.8, 0.6,  volume)

MyMIDI.addNote(track,channel,79, 32.4, 0.05, volume)
MyMIDI.addNote(track,channel,81, 32.45, 0.05, volume)
MyMIDI.addNote(track,channel,83, 32.5, 0.5, volume)
MyMIDI.addNote(track,channel,81, 33.0, 0.6, volume)
MyMIDI.addNote(track,channel,78, 33.0, 0.6, volume)
MyMIDI.addNote(track,channel,79, 33.6, 0.6, volume)
MyMIDI.addNote(track,channel,76, 33.6, 0.6, volume)
MyMIDI.addNote(track,channel,81, 34.2, 0.6, volume)
MyMIDI.addNote(track,channel,78, 34.2, 0.6,  volume)

MyMIDI.addNote(track,channel,79, 34.8, 0.05, volume)
MyMIDI.addNote(track,channel,81, 34.85, 0.05, volume)
MyMIDI.addNote(track,channel,83, 34.9, 0.5, volume)
MyMIDI.addNote(track,channel,81, 35.4, 0.6, volume)
MyMIDI.addNote(track,channel,78, 35.4, 0.6, volume)
MyMIDI.addNote(track,channel,79, 36.0, 0.6, volume)
MyMIDI.addNote(track,channel,76, 36.0, 0.6, volume)
MyMIDI.addNote(track,channel,75, 36.6, 0.6, volume)
MyMIDI.addNote(track,channel,78, 36.6, 0.6,  volume)
MyMIDI.addNote(track,channel,76, 37.2, duration2, volume)


MyMIDI.addNote(track,channel,72, 38.4, duration, volume)
MyMIDI.addNote(track,channel,76, 38.4, duration, volume)
MyMIDI.addNote(track,channel,74, 39.0, duration, volume)
MyMIDI.addNote(track,channel,77, 39.0, duration, volume)
MyMIDI.addNote(track,channel,76, 39.6, duration, volume)
MyMIDI.addNote(track,channel,79, 39.6, duration, volume)
MyMIDI.addNote(track,channel,76, 40.2, duration, volume)
MyMIDI.addNote(track,channel,79, 40.2, duration, volume)
MyMIDI.addNote(track,channel,81, 40.8, duration, volume)
MyMIDI.addNote(track,channel,79, 41.1, duration, volume)
MyMIDI.addNote(track,channel,77, 41.4, duration, volume)
MyMIDI.addNote(track,channel,76, 41.7, duration, volume)
MyMIDI.addNote(track,channel,71, 42.0, duration, volume)
MyMIDI.addNote(track,channel,74, 42.0, duration, volume)
MyMIDI.addNote(track,channel,67, 42.6, 0.6, volume)

MyMIDI.addNote(track,channel,72, 43.2, duration, volume)
MyMIDI.addNote(track,channel,76, 43.2, duration, volume)
MyMIDI.addNote(track,channel,74, 43.8, duration, volume)
MyMIDI.addNote(track,channel,77, 43.8, duration, volume)
MyMIDI.addNote(track,channel,76, 44.4, duration, volume)
MyMIDI.addNote(track,channel,79, 44.4, duration, volume)
MyMIDI.addNote(track,channel,76, 45.0, duration, volume)
MyMIDI.addNote(track,channel,79, 45.0, duration, volume)
MyMIDI.addNote(track,channel,81, 45.6, duration, volume)
MyMIDI.addNote(track,channel,79, 45.9, duration, volume)
MyMIDI.addNote(track,channel,77, 46.2, duration, volume)
MyMIDI.addNote(track,channel,76, 46.5, duration, volume)
MyMIDI.addNote(track,channel,71, 46.8, duration2, volume)
MyMIDI.addNote(track,channel,74, 46.8, duration2, volume)

MyMIDI.addNote(track,channel,69, 48.0, duration, volume)
MyMIDI.addNote(track,channel,72, 48.0, duration, volume)
MyMIDI.addNote(track,channel,71, 48.6, duration, volume)
MyMIDI.addNote(track,channel,74, 48.6, duration, volume)
MyMIDI.addNote(track,channel,72, 49.2, duration, volume)
MyMIDI.addNote(track,channel,76, 49.2, duration, volume)
MyMIDI.addNote(track,channel,72, 49.8, duration, volume)
MyMIDI.addNote(track,channel,76, 49.8, duration, volume)
MyMIDI.addNote(track,channel,77, 50.4, duration, volume)
MyMIDI.addNote(track,channel,76, 50.7, duration, volume)
MyMIDI.addNote(track,channel,74, 51.0, duration, volume)
MyMIDI.addNote(track,channel,72, 51.3, duration, volume)
MyMIDI.addNote(track,channel,68, 51.6, duration, volume)
MyMIDI.addNote(track,channel,71, 51.6, duration, volume)
MyMIDI.addNote(track,channel,64, 52.2, 0.6, volume)

MyMIDI.addNote(track,channel,69, 52.8, duration, volume)
MyMIDI.addNote(track,channel,72, 52.8, duration, volume)
MyMIDI.addNote(track,channel,71, 53.4, duration, volume)
MyMIDI.addNote(track,channel,74, 53.4, duration, volume)
MyMIDI.addNote(track,channel,72, 54.0, duration, volume)
MyMIDI.addNote(track,channel,76, 54.0, duration, volume)
MyMIDI.addNote(track,channel,72, 54.6, duration, volume)
MyMIDI.addNote(track,channel,76, 54.6, duration, volume)
MyMIDI.addNote(track,channel,77, 55.2, duration, volume)
MyMIDI.addNote(track,channel,76, 55.5, duration, volume)
MyMIDI.addNote(track,channel,74, 55.8, duration, volume)
MyMIDI.addNote(track,channel,72, 56.1, duration, volume)
MyMIDI.addNote(track,channel,68, 56.4, duration, volume)
MyMIDI.addNote(track,channel,71, 56.4, duration2, volume)


#---------------------------------------------------------
# Bass
#---------------------------------------------------------

MyMIDI.addNote(track,channel,45, 1.2, duration,volume)
MyMIDI.addNote(track,channel,48, 1.8, duration,volume)
MyMIDI.addNote(track,channel,52, 1.8, duration,volume)
MyMIDI.addNote(track,channel,48, 2.4, duration,volume)
MyMIDI.addNote(track,channel,52, 2.4, duration,volume)
MyMIDI.addNote(track,channel,48, 3.0, duration,volume)
MyMIDI.addNote(track,channel,52, 3.0, duration,volume)

MyMIDI.addNote(track,channel,45, 3.6, duration,volume)
MyMIDI.addNote(track,channel,48, 4.2, duration,volume)
MyMIDI.addNote(track,channel,52, 4.2, duration,volume)
MyMIDI.addNote(track,channel,48, 4.8, duration,volume)
MyMIDI.addNote(track,channel,52, 4.8, duration,volume)
MyMIDI.addNote(track,channel,48, 5.4, duration,volume)
MyMIDI.addNote(track,channel,52, 5.4, duration,volume)

MyMIDI.addNote(track,channel,45, 6.0, duration,volume)
MyMIDI.addNote(track,channel,48, 6.6, duration,volume)
MyMIDI.addNote(track,channel,52, 6.6, duration,volume)

MyMIDI.addNote(track,channel,45, 7.2, duration,volume)
MyMIDI.addNote(track,channel,48, 7.8, duration,volume)
MyMIDI.addNote(track,channel,52, 7.8, duration,volume)

MyMIDI.addNote(track,channel,45, 8.4, duration,volume)
MyMIDI.addNote(track,channel,48, 9.0, duration,volume)
MyMIDI.addNote(track,channel,52, 9.0, duration,volume)
MyMIDI.addNote(track,channel,48, 9.6, duration,volume)
MyMIDI.addNote(track,channel,52, 9.6, duration,volume)
MyMIDI.addNote(track,channel,48, 10.2, duration,volume)
MyMIDI.addNote(track,channel,52, 10.2, duration,volume)

MyMIDI.addNote(track,channel,40, 10.8, duration,volume)
MyMIDI.addNote(track,channel,47, 11.4, duration,volume)
MyMIDI.addNote(track,channel,52, 11.4, duration,volume)
MyMIDI.addNote(track,channel,47, 12.0, duration,volume)
MyMIDI.addNote(track,channel,52, 12.0, duration,volume)
MyMIDI.addNote(track,channel,47, 12.6, duration,volume)
MyMIDI.addNote(track,channel,52, 12.6, duration,volume)

MyMIDI.addNote(track,channel,40, 13.2, duration,volume)
MyMIDI.addNote(track,channel,47, 13.8, duration,volume)
MyMIDI.addNote(track,channel,52, 13.8, duration,volume)
MyMIDI.addNote(track,channel,47, 14.4, duration,volume)
MyMIDI.addNote(track,channel,52, 14.4, duration,volume)
MyMIDI.addNote(track,channel,47, 15.0, duration,volume)
MyMIDI.addNote(track,channel,52, 15.0, duration,volume)

MyMIDI.addNote(track,channel,40, 15.6, duration,volume)
MyMIDI.addNote(track,channel,47, 16.2, duration,volume)
MyMIDI.addNote(track,channel,52, 16.2, duration,volume)

MyMIDI.addNote(track,channel,35, 16.8, duration,volume)
MyMIDI.addNote(track,channel,47, 17.4, duration,volume)
MyMIDI.addNote(track,channel,40, 18.0, duration2,volume)

MyMIDI.addNote(track,channel,45, 20.4, duration,volume)
MyMIDI.addNote(track,channel,48, 21.0, duration,volume)
MyMIDI.addNote(track,channel,52, 21.0, duration,volume)
MyMIDI.addNote(track,channel,48, 21.6, duration,volume)
MyMIDI.addNote(track,channel,52, 21.6, duration,volume)
MyMIDI.addNote(track,channel,48, 22.2, duration,volume)
MyMIDI.addNote(track,channel,52, 22.2, duration,volume)

MyMIDI.addNote(track,channel,45, 22.8, duration,volume)
MyMIDI.addNote(track,channel,48, 23.4, duration,volume)
MyMIDI.addNote(track,channel,52, 23.4, duration,volume)
MyMIDI.addNote(track,channel,48, 24.0, duration,volume)
MyMIDI.addNote(track,channel,52, 24.0, duration,volume)
MyMIDI.addNote(track,channel,48, 24.6, duration,volume)
MyMIDI.addNote(track,channel,52, 24.6, duration,volume)

MyMIDI.addNote(track,channel,45, 25.2, duration,volume)
MyMIDI.addNote(track,channel,48, 25.8, duration,volume)
MyMIDI.addNote(track,channel,52, 25.8, duration,volume)

MyMIDI.addNote(track,channel,45, 26.4, duration,volume)
MyMIDI.addNote(track,channel,48, 27.0, duration,volume)
MyMIDI.addNote(track,channel,52, 27.0, duration,volume)

MyMIDI.addNote(track,channel,45, 27.6, duration,volume)
MyMIDI.addNote(track,channel,48, 28.2, duration,volume)
MyMIDI.addNote(track,channel,52, 28.2, duration,volume)
MyMIDI.addNote(track,channel,48, 28.8, duration,volume)
MyMIDI.addNote(track,channel,52, 28.8, duration,volume)
MyMIDI.addNote(track,channel,48, 29.4, duration,volume)
MyMIDI.addNote(track,channel,52, 29.4, duration,volume)

MyMIDI.addNote(track,channel,40, 30.0, duration,volume)
MyMIDI.addNote(track,channel,47, 30.6, duration,volume)
MyMIDI.addNote(track,channel,52, 30.6, duration,volume)
MyMIDI.addNote(track,channel,47, 31.2, duration,volume)
MyMIDI.addNote(track,channel,52, 31.2, duration,volume)
MyMIDI.addNote(track,channel,47, 31.8, duration,volume)
MyMIDI.addNote(track,channel,52, 31.8, duration,volume)

MyMIDI.addNote(track,channel,40, 32.4, duration,volume)
MyMIDI.addNote(track,channel,47, 33.0, duration,volume)
MyMIDI.addNote(track,channel,52, 33.0, duration,volume)
MyMIDI.addNote(track,channel,47, 33.6, duration,volume)
MyMIDI.addNote(track,channel,52, 33.6, duration,volume)
MyMIDI.addNote(track,channel,47, 34.2, duration,volume)
MyMIDI.addNote(track,channel,52, 34.2, duration,volume)

MyMIDI.addNote(track,channel,40, 34.8, duration,volume)
MyMIDI.addNote(track,channel,47, 35.4, duration,volume)
MyMIDI.addNote(track,channel,52, 35.4, duration,volume)

MyMIDI.addNote(track,channel,35, 36.0, duration,volume)
MyMIDI.addNote(track,channel,47, 36.6, duration,volume)
MyMIDI.addNote(track,channel,40, 37.2, duration2,volume)

MyMIDI.addNote(track,channel,36, 39.6, 0.6,volume)
MyMIDI.addNote(track,channel,48, 40.2, 0.6,volume)

MyMIDI.addNote(track,channel,40, 40.8, 0.6,volume)
MyMIDI.addNote(track,channel,52, 41.4, 0.6,volume)

MyMIDI.addNote(track,channel,43, 42.0, duration2,volume)

MyMIDI.addNote(track,channel,36, 44.4, 0.6,volume)
MyMIDI.addNote(track,channel,48, 45.0, 0.6,volume)

MyMIDI.addNote(track,channel,40, 45.6, 0.6,volume)
MyMIDI.addNote(track,channel,52, 46.2, 0.6,volume)

MyMIDI.addNote(track,channel,43, 46.8, duration2,volume)

MyMIDI.addNote(track,channel,33, 49.2, 0.6,volume)
MyMIDI.addNote(track,channel,45, 49.8, 0.6,volume)

MyMIDI.addNote(track,channel,36, 50.4, 0.6,volume)
MyMIDI.addNote(track,channel,48, 51.0, 0.6,volume)

MyMIDI.addNote(track,channel,40, 51.6, duration2,volume)

MyMIDI.addNote(track,channel,33, 54, 0.6,volume)
MyMIDI.addNote(track,channel,45, 54.6, 0.6,volume)

MyMIDI.addNote(track,channel,36, 55.2, 0.6,volume)
MyMIDI.addNote(track,channel,48, 55.8, 0.6,volume)

MyMIDI.addNote(track,channel,40, 56.4, duration2,volume)


# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
