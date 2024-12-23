# Frequently Asked Questions (FAQ)
### this is where you'll find most of the questions that you might have


1. Questions regarding Python
   - Do i Need python installed to run this app?
     - YES, you'll need to have python installed for it to work
   - How do i Install Python?
     - 1= go to [python website](https://www.python.org/downloads/) and download the latest version of python for windows
     - 2= open the downloaded installer, tick the boxes for installing for all users and for adding python to PATH
     - 3= click in install now and do the installing as normal 
   - do i need any python library as requirement?
     - NO, all the 3 libraries used by this app (time, os, ctypes), come pre-installed with python
     
2. Questions regarding the app
   - is this a mod menu?
     - NO!, This is not a mod menu for gta online, it is an automation script that allows you to block the game's cloud saving by using windows firewall rules, and it does not interfere with any of the game's files or tasks, neither does it automates user inputs like a macro
   - Can i get banned from GTA Online for using this?
     - at the time i'm posting this (12/23/2024), NO, you won't get banned for using this app, mainly because as said before, it does not alter any of the game code os tasks, and it also doesn't automate user inputs such as a macro, so it won't trigger any of battleye cheat detections, and it probably never will, considering all the stuff that this app does can be done by command lines in windows CMD...
> [!WARNING]
> even though the chances of getting banned by using this app are extremely slim and nearly non-existent, it may happen if you use it unproperly or if it becomes detected in a far future, knowing that, be advised that i (the owner of this app) do not and will not take responsability for any bans caused by the use of this app, **SO USE IT AT YOUR OWN RISK**.
  - what is the purpose of this app?
     - the main purpose of this app is auxiliating in glitches and in the gameplay in general
   - what are the options of this app?
     - this app has 3 main options and 3 additional options, which are:
     - number 1 = block cloud saving
       - this will create a firewall rule that will block the connection leaving your pc to the rockstar cloud saving servers IP
     - number 2 = unblock cloud saving
       - deletes the firewall rule previously created, this way allowing connections with the cloud saving servers IP
     - number 7 = kill gta 5 process
       - this will kill gta 5 task and instantly close the game, useful in cases where the game froze or in certain glitches
     - number 8 = will close the app and finish it's execution
     - number 9 = will open this FAQ file that you're reading
     - number 0 = will open this app GitHUB repo
   - what are some examples of use of this app?
     - this app has a lot of uses, but the main ones are:
       - doing replay glitches for heists like cayo perico and the diamond casino heist, this way, after finishing the heist you'll will have the money but the heist will still be ready and fully preped
       - bypassing daily sell limits
       - using snacks, ammo, and armor without it subtracting from you inventory
       - replaying time trials
       - ETC
   - How do i use this app?
     - you can use it by the .py file and the executable file
        - using by the .py file:
          - 1= open cmd using administrator previleges in the same path as you placed the script
          - 2= run the following command:
            `python gta-script.py`
        - using the executable file:
          - 1= download the .exe file and the '_internal' folder, note that the .exe file must be at the same directory as the '_internal' folder and if you don't have the '_internal' folder alongside with the .exe file, the app will not run
          - 2= double click the executable and give it admin permission
   - what does UNKNOWN OPTION means?
     - UNKNOWN OPTION means that the option you inserted in the app is not recognized as any of the 6 options mentioned, this may happen if:
       - you entered a text or any other thing that isn't recognized as an option
       - you accidentally added a space before or after you enter your choosen option
       - you accidentally added more than a single digit in your option
       > remember that to choose an option in the app, you only need to type one of the 6 numbers binded to an option, you don't need to add parenthesis or brackets to the input
   - Is it better to run this app through the .py file or the executable file?
     - i would say it is better to run it through the executable, this way you don't need to worry about any misconfiguration in your python files
   - which OS and Platforms does this app works on?
     - this currently only works in windows, i'm sure that it works on windows 10 and 11, not sure about windows 7, 8 and 8.1
     - it does not work in linux and MacOS
     - it also obviously does not work in consoles

3. Question regarding alternative apps
   - Is it better than AHK no save scripts?
     - i would say so, because my python script is more stable and safer than AHK, because while python is a coding language with multiple uses, AHK, while also having multiple uses it is often related to the use of macro cheats in games, makin it less safe and more likely to cause a ban
     - but in other hand, while my script uses text inputs to trigger it's options, AHK often uses keyboard shortcuts for it, which may be quicker
   - Is it better than Powershell no save scripts?
     - Yes, it works pretty much the same as powershell scripts, however it is safer, more stable and quicker than powershell scripts
   - ins't it better just to disconnect my internet?
     - NO, because it does not work for all of the same glitches as my script, since differently from blocking cloud saving, disconnecting your internet will make you fall from the session, not only that but the heists that you can use the replay glitches, will have a pretty narrow timing that you'll be able to trigger the glitch by disconnecting your internet, and if you miss the small timing window the glitch won't work properly, while by using my script you'll have a much bigger timing window to do the glitch

4. question regarding the code and license
   - Why you don't convert the user input to a Integer value in the opt_menu function in the code?
     - the main reason i did this is because if i converted the string values of the inpu to integer, but the user accidentaly added a character value to the input, it would cause the app to crash instead of saying that the option is unknown, so instead of it i just used string vlaues in the if statements
   - can i post this app on other platforms?
     - It depends, you'll can share my github repo, but you can't upload my raw repo files to another platform without modifying them into an original file and get the credit for it, if i know of a case like this i will file a DMCA strike in whichever platform it happens

5. misc questions
   - What do i do if my question is not in the list?
     -
   - How can i support you?
     -
