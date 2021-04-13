# virtualenv_pip

An example of running python in a virtual environment with packages installed
with pip from a requirements.txt file.

Dependencies: bash, python3 and pip3

First run:

    build.sh

Then run:

    run.sh

Sample output:

    >bash run.sh
    Image processing using PIL (pillow) and numpy of an image downloaded with requests
    Read image from URL: https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png
    Downsize image to width 256
    Edge detection
    Pixellating image
    Converting image to grey scale
    Stacking all images into a numpy array and saving as a PIL image
    Wrote file out.png
    
    Computing geographic distances between cities using haversine package
    Distance between Copenhagen and Rome (in a straight line) is 1531 km
    
    Computing the time of next time Mars rises in London in using ephem and pytz (for local time)
    Mars rises next time in London at 2021-04-14 07:38:15.567206+00:00 UTC
    Mars sets next time in London at 2021-04-14 00:32:29.700663+00:00 UTC
    Mars rises next time in London at 2021-04-14 08:38:15.567206+01:00 (local time)
    Mars sets next time in London at 2021-04-14 01:32:29.700663+01:00 (local time)


To re-build the virtual environment then simply delete the contents of the
virtual environment directory (here: venv).
