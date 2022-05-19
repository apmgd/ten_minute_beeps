import os
import time as t

# I use the beep here: https://freesound.org/people/Pablobd/sounds/492481/
file = 'PASTE AUDIO FILE PATH HERE'
while True:  # Infinite loop
    print('Beep beep! ' + t.strftime("%H:%M", t.localtime()))
    os.system("afplay " + file)

    t.sleep(600)  # Wait 600s (10 min) before re-entering the cycle
