Sky-Time
========

Educational game for Sugar

This game is designed to teach youth the connection between clocks and time.  

We plan to have a title screen with two buttons, a 'play' button where the student can become familiar with the program, 
and a 'challenge' button that will allow the youth to test their knowledge of telling time.

To be able to run the game, you need to generate and move the .mo files into the correctdirectories.

To do this, open a terminal and go into the po/ directory and enter the following commands:

    $ python msgfmt.py SkyTimeEnglish.po
    $ sudo mv ./SkyTimeEnglish.mo /usr/share/locale/en/LC_MESSAGES/

This will generate the .mo file for the English translations and move the file to the proper directory that the game will read from.  Repeat those two steps for each language.

You will need to replace the 'en' in the second command line with the corresponding language code.

English = en
Spanish = es
French = fr
