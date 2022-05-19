# import required module
import os
import time

# I use the beep here: https://freesound.org/people/Pablobd/sounds/492481/
file = 'PASTE AUDIO FILE PATH HERE'
while True:  # Infinite loop
    print('Beep beep!')
    os.system("afplay " + file)

    time.sleep(600)  # Wait 600s (10 min) before re-entering the cycle
