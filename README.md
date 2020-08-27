# abba-saul
A mishnah bot for Discord

_Made by Saul Cooperman. Age 17_

### History
I have been doing the Time4Mishnah program with 2 friends for a couple of years now. We have been using Discord has our
means of communication of the COVID-19 quarantine period. The easy-to-use UI allows us to easily call and learn with good quality
audio and video.

Although it was annoying to have a Discord window open on my computer as well as a Sefaria tab for the Mishnah. So to, I
programmed a Discord bot in Python 3.8 using the discord library and the Sefaria API.

### Functionality
The main function we wanted was to be able to print a chosen Mishnah into the chat with the Book, Perek and Mishnah number. It
also has a translation functionality which allows us to translate a single word if we are struggling with the Hebrew.

##### Modes
 * Fetch: this will fetch the Mishnah from the API (-b: which book, -p: which perek, -m: which mishnah, -o: Only Hebrew[1] or English[2] (Default: Both))
 * Translate: this will translate a specific word (-w: word to translate from Hebrew to English)
##### Examples
Command: `abba saul fetch -b berakhot -p 5 -m 5`
Output: 

### Looking forward
I plan to add much more in future such as the ability to ask for commentaries and more easy Mishnah navigation. This will be
Incredibly useful as reading differenct commentaries on the Sefaria on my phone is difficult. Having it on the Discord chat means
you can navigate between different texts with ease.

Additionally, I would like to further expand it beyond just Mishnah. Although this may be difficult as I am entering my last year
of high school so it will be tough to find time.
