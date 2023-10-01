#pip install pyscreenshot
#pip install win10toast
import time
import pyscreenshot

# Take a screenshot
image = pyscreenshot.grab()

# Get the current time in seconds since the epoch
ctime = int(time.time())

# Create a filename with the current time
fname = f"{ctime}_screenshot.png"

image.show()

# Save the screenshot with the current time as the filename
image.save(fname)
