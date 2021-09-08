***READ ME***
Quore Builder installation guide -

The first thing you'll need to have is atleast Python 3.6.8 which you can retrieve from their official website
(https://www.python.org/downloads/)

After this you will need to install the IDE Pycharm to be able to properly examine the code for Quore builder and download the reqiured dependencies
(https://www.jetbrains.com/pycharm/download/#section=windows)

Once Pycharm is opened and you can import the Quore builder python code onto your machine you must download the dependenceies required to run KivyMD

To do this once you have a project open in pycharm go to the top left toolbar and click on File, then Settings (or you can use the hotkey Ctrl+Alt+S)
From the settings menu on the left side there should be a drop down list of the project you have open. Click on it then select Python Interpreter from the options.
After selecting the interpreter be sure the correct interpreter is selected at the top of the window. This window will show you the currently install dependencies.
On the right side of the window there should be a + sign.
After clicking on the + it will direct you to another window titled Available Packages where you are able to download the required dependencies. 


The dependencies that you will need are as follows
Kivy
Kivy-Garden
Pillow
Pygments
certifi
chardet
docutils
idna
kivy-deps.angle
kivy-deps.glew
kivy-deps.gstreamer
kivy-deps.sdl2
kivymd
pip
psycopg2
pypiwin32
pywin32
requests
setuptools
urllib3

After having these installed you're ready to getting the required software for the database.

*we plan on eventually hosting the database so users can access it from their phones and do not need to download post gres in the future.
Lasty you will need to download postgres SQL from there offical website (https://www.postgresql.org/).
First make sure that you are running postgres 13. Right click on post-gres 13 and push create server name the server gym app.
Use the drop down menu on the database right click on gym app click on restore under file name put in the file in the folder called gym app.

Now run ScreenManager.py and a good test login crediantal is username Matty_J password 123456 but feel free to create your own account and as you create workouts 
they will be updated on the next time you run the program.

If you run into any issues please feel free to conact me at ztm008@shsu.edu hope you enjoy our app!
