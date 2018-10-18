'''
Youtube Mass Video Audio Downloader by: Lucas Zanchetta
HOW TO USE:
1. Create a text file in the same directory of the script that has the search query for each video on a separate line
of the text file
2. Run the script and when prompted, enter the name of the text file containing the list of videos that contain the audio you wish to extract
'''

from __future__ import unicode_literals
import youtube_dl
import re
import urllib.parse
import os
import time

# The main function that is run if the user accepts the piracy notice
def main():
    print('Great! Thanks for understanding, here are the files located in the directory of this script.')
    print('If you followed the instructions, your video list text file will be located in here.')
    print('')

# When called upon, the script runs the dir command on the os to show the contents of the script's directory
    dir = lambda: os.system('dir')

    dir()  # Prints the contents of the script's directory
    print('')

    print('Enter the name of the test file with or without the extention: ')

    fileName = input()  # Specifies video Name
    fileNameSize = len(fileName)  # Gets the sie of the fileName to see the last character location
    fileExtentionIndex = fileNameSize - 4  # Subtracts 4  from the fileName to know where the beginning of the .txt
    extention = '.txt'                     # extension is if the user entered the fileName with the exntention

    if fileName[fileExtentionIndex:fileNameSize] == ".txt":  # If the last for characters of fileName are equal to .txt,
        filePath = fileName                                 # then there is no need to add the extension
# if the last four characters aren't .txt, it means the user has not included the it in their input and it must be added
    else:
        filePath = fileName + extention

    with open(filePath) as fp:
        '''
        This sets the checknum to 1 by default, checknum is used for flow control so that the code does not start 
        downloading random videos and crash
        '''
        checknum = 1
        '''
        #This runs so long as the checknum's value is equal to one, if the line the script is currently on is blank, 
        signifying the last line, the checknum gets set to 2 and this code isn't run
        '''
        while checknum == 1:

            def download(): # Downloads the video audio based on the search query text provides by the if statement
                queryString = urllib.parse.urlencode({"search_query": vidName})
                htmlContent = urllib.request.urlopen("http://www.youtube.com/results?" + queryString)
                searchResults = re.findall(r'href=\"\/watch\?v=(.{11})', htmlContent.read().decode())
                url = "http://www.youtube.com/watch?v=" + searchResults[0]
                print(url)

                # This code configures youtube_dl to download in the best quality and to use the video name as the
                # filename and make the file MP3 using FFMPEG
                ydl_opts = {
                    'format': 'bestaudio/best', # Sets audio quality to the best possible
                    'outtmpl': '%(title)s.%(ext)s', # Defines the file naming for the outputted file
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',

                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            vidName = fp.readline()
            # Checks to see if there if the current line is the last line, if it is, it sets the checknum to 2,
            if vidName != '': # stopping the code
                print(vidName) # Prints the name of the video about the be downloaded
                download() # Calls the download function to actually download the video audio
            else:
                checknum = 2 # Sets the checknum to 2 which stops the loop, and in turn, stopping the script
                print('') # Skips a line
                print('List Finished')

def disclaimer():
    clear = lambda: os.system('cls')
    clear()
    print('DISCLAIMER: DO NOT USE THIS PROGRAM TO DOWNLOAD AUDIO YOU HAVE NOT BEEN GIVEN PERMISSION TO DOWNLOAD')
    print('')
    print('We strongly discourage piracy and do not accept responsability for what you do with this script')
    print('')
    print('Do you understand this and agree not to use this script to download audio you do not own or do not have permission to download? (enter Y or N)')
    agreement = input()
    def restart():
        print('Restarting in')
        print('3')
        time.sleep(.75)
        print('2')
        time.sleep(.75)
        print('1')
        time.sleep(.75)
        clear()
        disclaimer()

    if agreement.upper() == 'Y':
        clear()
        main()
    elif agreement.upper() == 'N':
        print('Sorry, you must agree to these terms to use this program')
        restart()
    else:
        restart()

disclaimer()