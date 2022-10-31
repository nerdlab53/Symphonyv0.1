# Symphony v0.01
Symphony is a computer vision based project that allows you to play music through leg gestures using ArucoMarkers.

## Overview:
* We use OpenCV and ArucoMarkers for detecting the markers that have been placed on the floor, the marker size is kept after taking in consideration the average shoe size of the partcipants so as to avoid any errors whilel detecting the markers.
* After the detection of the marker is done, the next challenge we face is how to produce the sounds used in the game. We tackle this problem by using boolean expresions in the conditional statements. When the participant puts his leg on the marker, the marker returns a boolean value:0  which plays the sound of player winning a point. When the leg is removed, the marker is detected again and hence the production of sound is stopped.
* We have used Tkinter to provide a user interface to the participant to make the game more interactive by making dynamic pop-ups for windows like "Game-Over" and "Game-Begins" and providing them options to select their preferred in-game-music.


## Language Used: Python






## Libraries Used: OpenCV Tkinter Aruko Sound
