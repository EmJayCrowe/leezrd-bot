# Honestly probably implemented in a neater way than the CONSOLE

ter_dirs = {
    #root directory
    "/": {"dir": ["Program Files", "Users", "USB Drive", "Secured"]},
    "/Program Files": {"dir": ["..", "Steam", "Scratch", "SURVEY_PROGRAM"]},

    #steam
    "/Program Files/Steam": {"dir": ["..", "steamapps"]},
    "/Program Files/Steam/steamapps": {"dir": ["..", "common", "workshop"]},
    "/Program Files/Steam/steamapps/common": {"dir": ["..", "The Stanley Parable Ultra Deluxe"], "txt": ["password_piece.txt"]},
    "/Program Files/Steam/steamapps/common/The Stanley Parable Ultra Deluxe": {"dir": [".."], "txt": ["transcript.txt"], "cmd": ["raphael"]},
    "/Program Files/Steam/steamapps/workshop": {"toolarge": True},

    #scratch
    "/Program Files/Scratch": {"dir": ["..", "Projects"]},
    "/Program Files/Scratch/Projects": {"dir": ["Trauma", "Derpymon GO!!", "old"]},
    "/Program Files/Scratch/Projects/Trauma": {"dir": [".."], "zip": ["Trauma v1.10.zip"], "txt": ["trauma.txt"]},
    "/Program Files/Scratch/Projects/Derpymon GO!!": {"dir": [".."], "txt": ["play.txt", "derpymon.txt"]},
    "/Program Files/Scratch/Projects/old": {"dir": [".."], "txt": ["warning.txt", "password_piece.txt"], "zip": ["Cat Clicker 2.zip", "Blomp!.zip"]},

    #deltarune
    "/Program Files/SURVEY_PROGRAM": {"toolarge": True},

    #main bit
    "/Users": {"dir": ["..", "emjay"]},
    "/Users/emjay": {"dir": ["..", "AppData", "Desktop", "Documents", "Downloads"]},

    #appdata
    "/Users/emjay/AppData": {"dir": ["..", "Local", "LocalLow", "Roaming"]},
    "/Users/emjay/AppData/Local": {"toolarge": True},
    "/Users/emjay/AppData/LocalLow": {"toolarge": True},
    "/Users/emjay/AppData/Roaming": {"dir": ["..", ".minecraft", "BetterDiscord", "tEdit"]},
    "/Users/emjay/AppData/Roaming/BetterDiscord": {"dir": [".."], "txt": ["delete.txt", "password_piece.txt"]},
    "/Users/emjay/AppData/Roaming/tEdit": {"toolarge": True},

    #minecraft
    "/Users/emjay/AppData/Roaming/.minecraft": {"dir": ["..", "mods", "saves", "resourcepacks", "screenshots"]},
    "/Users/emjay/AppData/Roaming/.minecraft/mods": {"toolarge": True},
    "/Users/emjay/AppData/Roaming/.minecraft/saves": {"toolarge": True},
    "/Users/emjay/AppData/Roaming/.minecraft/resourcepacks": {"toolarge": True},
    "/Users/emjay/AppData/Roaming/.minecraft/screenshots": {"dir": [".."], "jpeg": ["HIM.png"]},

    #desktop
    "/Users/emjay/Desktop": {"dir": ["..", "python stuff", "Secret"], "txt": ["one day.txt", "password_piece.txt"], "jpeg": ["scribblings.jpg"], "cmd": ["adminunlock"]},
    "/Users/emjay/Desktop/python stuff": {"dir": ["..", "scripts"]},
    "/Users/emjay/Desktop/python stuff/scripts": {"toolarge": True},
    "/Users/emjay/Desktop/Secret": {"dir": ["..", "web", "deltarune saves", "Discord", "Leez-rd", "MC Stuff", "Zoo"], "txt": ["trol.txt"]},

    #coinfrend
    "/Users/emjay/Desktop/Secret/web": {"dir": ["..", "CoinFrend"]},
    "/Users/emjay/Desktop/Secret/web/CoinFrend": {"dir": [".."], "txt": ["info.txt"], "jpeg": ["logo.png"]},

    #deltarune
    "/Users/emjay/Desktop/Secret/deltarune saves": {"toolarge": True},

    #bots
    "/Users/emjay/Desktop/Secret/Discord": {"dir": ["..", "Leez-rd Bot", "BudgetTop", "WanterTop"], "cmd": ["clearcol"]},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot": {"dir": ["..", "commands", "terminal"], "txt": ["todo.txt"], "jpeg": ["pfp.png"]},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/commands": {"dir": ["..", "slash", "unfinished"]},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/commands/slash": {"toolarge": True},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/commands/unfinished": {"dir": [".."], "cmd": ["adventure", "garden"]},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/terminal": {"dir": [".."], "txt": ["readme.txt"], "cmd": ["cd", "help"]},
    "/Users/emjay/Desktop/Secret/Discord/BudgetTop": {"dir": ["..", "commands"], "jpeg": ["pfp.png"]},
    "/Users/emjay/Desktop/Secret/Discord/BudgetTop/commands": {"dir": [".."], "cmd": ["uwu"]},
    "/Users/emjay/Desktop/Secret/Discord/WanterTop": {"dir": ["..", "commands"], "jpeg": ["pfp.png", "pfp2.png"]},
    "/Users/emjay/Desktop/Secret/Discord/WanterTop/commands": {"dir": [".."], "cmd": ["aqua", "altaqua", "list"]},

    "/Users/emjay/Desktop/Secret/MC Stuff": {"toolarge": True},

    #leez-rd folder
    "/Users/emjay/Desktop/Secret/Leez-rd": {"dir": ["..", "images", "lore"], "txt": ["password_piece.txt"]},
    "/Users/emjay/Desktop/Secret/Leez-rd/images": {"dir": ["..", "poopyshoes"], "jpeg": ["leez.png", "beth.png", "carcassite.png", "bryan.png", "albino.png"]},
    "/Users/emjay/Desktop/Secret/Leez-rd/images/poopyshoes": {"secured": True, "dir": [".."], "jpeg": ["no_blur.png", "takeover.png"]},
    "/Users/emjay/Desktop/Secret/Leez-rd/lore": {"secured": True, "dir": [".."], "jpeg": ["Book 1.png", "Book 2.png", "Book 3.png", "Book 4.png", "Recovered Correspondence 1.png", "Recovered Correspondence 2.png"]},

    #documents
    "/Users/emjay/Documents": {"dir": [".."], "txt": ["sequence.🗿"]},

    #downloads
    "/Users/emjay/Downloads": {"toolarge": True},

    #admin
    "/Secured": {"secured": True, "dir": ["..", "hidden folders"], "txt": ["plans.txt"]},
    "/Secured/hidden folders": {"secured": True, "dir": [".."], "txt": ["hint1.txt", "hint2.txt", "hint3.txt"]},

    #zoo
    "/Users/emjay/Desktop/Secret/Zoo": {"dir": ["..", "Animal SVGs", "Icons", "Funny", "WanterWither"]},
    "/Users/emjay/Desktop/Secret/Zoo/Animal SVGs": {"toolarge": True},
    "/Users/emjay/Desktop/Secret/Zoo/Icons": {"dir": ["..", "Common", "Rare"]},
    "/Users/emjay/Desktop/Secret/Zoo/Icons/Common": {"toolarge": True},
    "/Users/emjay/Desktop/Secret/Zoo/Icons/Rare": {"toolarge": True},
    "/Users/emjay/Desktop/Secret/Zoo/Funny": {"dir": [".."], "jpeg": ["avz.png", "breeding kit.png", "JAMES VEITCH CONFIRMED.png", "mr beast.png", "Crazoo Dave.png", "Chad Kady.png"]},
    "/Users/emjay/Desktop/Secret/Zoo/WanterWither": {"dir": [".."], "jpeg": ["sexy.png", "hmmm.jpg", "hesaidwhat.png", "WanToken.png", "WanterTop!.png"], "cmd": ["bert"]},

    #hidden
    "/Users/emjay/AppData/Roaming/.minecraft/newcmd": {"hidden": True, "dir": [".."], "cmd": ["alter"]},
    "/Users/emjay/Desktop/Secret/Zoo/Chad Kady": {"hidden": True, "dir": [".."], "cmd": ["prism", "rebuild", "remove"]},

    #usb
    "/USB Drive": {"dir": ["..", "unstoppable"], "txt": ["empty.txt"]},
    "/USB Drive/unstoppable": {"hidden": True, "dir": [".."], "txt": ["note.txt"], "cmd": ["dreams"]}
}

ter_backdirs = {
    #root directory
    "/": "/",
    "/Program Files": "/",
    "/Secured": "/",
    "/Secured/hidden folders": "/Secured",
    "/USB Drive": "/",

    #steam
    "/Program Files/Steam": "/Program Files",
    "/Program Files/Steam/steamapps": "/Program Files/Steam",
    "/Program Files/Steam/steamapps/common": "/Program Files/Steam/steamapps",
    "/Program Files/Steam/steamapps/common/The Stanley Parable Ultra Deluxe": "/Program Files/Steam/steamapps/common",

    #scratch
    "/Program Files/Scratch": "/Program Files",
    "/Program Files/Scratch/Projects": "/Program Files/Scratch",
    "/Program Files/Scratch/Projects/Trauma": "/Program Files/Scratch/Projects",
    "/Program Files/Scratch/Projects/Derpymon GO!!": "/Program Files/Scratch/Projects",
    "/Program Files/Scratch/Projects/old": "/Program Files/Scratch/Projects",

    #main bit
    "/Users": "/",
    "/Users/emjay": "/Users",

    #appdata
    "/Users/emjay/AppData": "/Users/emjay",
    "/Users/emjay/AppData/Roaming": "/Users/emjay/AppData",
    "/Users/emjay/AppData/Roaming/BetterDiscord": "/Users/emjay/AppData/Roaming",

    #minecraft
    "/Users/emjay/AppData/Roaming/.minecraft": "/Users/emjay/AppData/Roaming",
    "/Users/emjay/AppData/Roaming/.minecraft/screenshots": "/Users/emjay/AppData/Roaming/.minecraft",
    "/Users/emjay/AppData/Roaming/.minecraft/newcmd": "/Users/emjay/AppData/Roaming/.minecraft",

    #desktop
    "/Users/emjay/Desktop": "/Users/emjay",
    "/Users/emjay/Desktop/python stuff": "/Users/emjay/Desktop",
    "/Users/emjay/Desktop/Secret": "/Users/emjay/Desktop",

    #coinfrend
    "/Users/emjay/Desktop/Secret/web": "/Users/emjay/Desktop/Secret",
    "/Users/emjay/Desktop/Secret/web/CoinFrend": "/Users/emjay/Desktop/Secret/web",

    #bots
    "/Users/emjay/Desktop/Secret/Discord": "/Users/emjay/Desktop/Secret",
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot": "/Users/emjay/Desktop/Secret/Discord",
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/terminal": "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot",
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/commands": "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot",
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/commands/unfinished": "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/commands",
    "/Users/emjay/Desktop/Secret/Discord/BudgetTop": "/Users/emjay/Desktop/Secret/Discord",
    "/Users/emjay/Desktop/Secret/Discord/BudgetTop/commands": "/Users/emjay/Desktop/Secret/Discord/BudgetTop",
    "/Users/emjay/Desktop/Secret/Discord/WanterTop": "/Users/emjay/Desktop/Secret/Discord",
    "/Users/emjay/Desktop/Secret/Discord/WanterTop/commands": "/Users/emjay/Desktop/Secret/Discord/WanterTop",

    #leez-rd folder
    "/Users/emjay/Desktop/Secret/Leez-rd": "/Users/emjay/Desktop/Secret",
    "/Users/emjay/Desktop/Secret/Leez-rd/images": "/Users/emjay/Desktop/Secret/Leez-rd",
    "/Users/emjay/Desktop/Secret/Leez-rd/images/poopyshoes": "/Users/emjay/Desktop/Secret/Leez-rd/images",
    "/Users/emjay/Desktop/Secret/Leez-rd/lore": "/Users/emjay/Desktop/Secret/Leez-rd",

    #documents
    "/Users/emjay/Documents": "/Users/emjay",

    #downloads
    "/Users/emjay/Downloads": "/Users/emjay",


    "/Users/emjay/Desktop/Secret/Leez-rd": "/Users/emjay/Desktop/Secret",
    "/Users/emjay/Desktop/Secret/MC Stuff": "/Users/emjay/Desktop/Secret",
    "/Users/emjay/Desktop/Secret/Zoo": "/Users/emjay/Desktop/Secret",
    "/Users/emjay/Desktop/Secret/Zoo/Animal SVGs": "/Users/emjay/Desktop/Secret/Zoo",
    "/Users/emjay/Desktop/Secret/Zoo/Icons": "/Users/emjay/Desktop/Secret/Zoo",
    "/Users/emjay/Desktop/Secret/Zoo/Icons/Common": "/Users/emjay/Desktop/Secret/Zoo/Icons",
    "/Users/emjay/Desktop/Secret/Zoo/Icons/Rare": "/Users/emjay/Desktop/Secret/Zoo/Icons",
    "/Users/emjay/Desktop/Secret/Zoo/Funny": "/Users/emjay/Desktop/Secret/Zoo",
    "/Users/emjay/Desktop/Secret/Zoo/WanterWither": "/Users/emjay/Desktop/Secret/Zoo",
    "/Users/emjay/Desktop/Secret/Zoo/Chad Kady": "/Users/emjay/Desktop/Secret/Zoo",

    "/USB Drive/unstoppable": "/USB Drive",


}

ter_content = {
    "/Program Files/Steam/steamapps/common/The Stanley Parable Ultra Deluxe": {"transcript.txt": "This is the story of a man named Stanley.\n \nStanley worked for a company in a big building where he was Employee #427.\n \nEmployee #427's job was simple: he sat at his desk in Room 427 and he pushed buttons on a keyboard.\n \nOrders came to him through a monitor on his desk telling him what buttons to push, how long to push them, and in what order.\n \nThis is what Employee #427 did every day of every month of every year, and although others may have considered it soul rending,\n \nStanley relished every moment that the orders came in, as though he had been made exactly for this job.\n \nAnd Stanley was happy.\n \nAnd then one day, something very peculiar happened.\n \nSomething that would forever change Stanley;\n \nSomething he would never quite forget.\n \nHe had been at his desk for nearly an hour when he had realized not one single order had arrived on the monitor for him to follow.\n \nNo one had shown up to give him instructions, call a meeting, or even say 'hi'. Never in all his years at the company had this happened, this complete isolation.\n \nSomething was very clearly wrong. Shocked, frozen solid, Stanley found himself unable to move for the longest time.\n \nBut as he came to his wits and regained his senses, he got up from his desk and stepped out of his office.\n \nAll of his co-workers were gone. What could it mean? Stanley decided to go to the meeting room; perhaps he had simply missed a memo.\n \nWhen Stanley came to a set of 2 open doors, he entered the door on his left.\n \n(+46,901 lines)"},
    "/Program Files/Scratch/Projects/Trauma": {"trauma.txt": "Trauma was a game I made in Scratch back for April Fools' 2022. It's intended to be so brutally unfair that you don't want to beat it, but there'll always be those people who are determined to prevail.\n \nYou can download and play the game by opening the other file in this folder, but be warned; it's not meant to be fun.", "Trauma v1.10.zip": " ```[Download Trauma v1.10.zip](https://drive.google.com/file/d/10zA-oWzoaRHHJzncQhO_J38JOJDTveP5/)``` "},
    "/Program Files/Scratch/Projects/Derpymon GO!!": {"derpymon.txt": "Derpymon GO!! is a long story. Back in 2018 (I WAS NINE), I created Derpymon GO!!, a parody of the many crappy Pokémon GO clones available on Scratch. It was actually really fun, and concepts for Derpymon (originally DUMBYMON) date back a year or two before even then.\n \nHowever because of the awful refresh rate of the laptop I originally made it on in comparison to others, the game doesn't work properly on all devices. I had many ideas for a possible Derpymon Go 2, but considering the original game didn't even work, in April/May of 2022 I started building a re-imagining of Derpymon GO!! from the ground up. In the coming months I made multiple content updates, adding postgame content and more stuff. In mid January I released version 1.4, the final major content update for the game. It is the only Scratch game still up on my account today, as I'm very proud of it. You can find the link by opening play.txt.", "play.txt": " ```[Play Derpymon GO!! on Scratch with this link!](https://scratch.mit.edu/projects/677269153)\n[Alternatively, play it here with 60fps](https://turbowarp.org/677269153)``` "},
    "/Program Files/Scratch/Projects/old": {"password_piece.txt": "Keep the order in your head. Pokémon comes first, then the secret word, then the number, and finally the animal.", "warning.txt": "Just as an FYI, these games are... okay, but they are definitely less fleshed-out.\n \nCat Clicker 2 is quite good from what I remember, but some of the achievements expect you to play the game a lot longer than there is content for.\n \nBlomp was just a fun idea I had once. Blomp will always be where your mouse is.\n \nHere be dragons!", "Blomp!.zip": " ```[Download Blomp!](https://drive.google.com/file/d/1lyMMYwPIchrPhv3cArzkdaZFbzPyt1p3)``` ", "Cat Clicker 2.zip": " ```[Download Cat Clicker 2](https://drive.google.com/file/d/1IH-MknMuuDJUzrISONgx4uOXeCNF16FO)``` "},
    "/Users/emjay/Desktop": {"one day.txt": "38°15′00.5″N  122°24′38.9″W\n \none day", "password_piece.txt": "PW_POKEMON", "scribblings.jpg": "https://cdn.discordapp.com/attachments/1074287626623926272/1082393673028882472/scribblings.jpg"},
    "/Users/emjay/Desktop/Secret": {"trol.txt": "Ones there was a trol he was a magic trol and one trol got sik then pop poop got sik\nthe next day thewood from the house that the trols live in 99 years later trols started to die\nexept the magic trol he was good the end"},
    "/Users/emjay/Desktop/Secret/web/CoinFrend": {"info.txt": "CoinFrend! What started as a gag website has now turned into a site I actively use to upload files and hide secrets.```\n[Link](https://sites.google.com/view/coinfrend)\n \n```/supersecret/party", "logo.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1077359242341797919/cflogo.png"},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot": {"todo.txt": "Left to do before 1.0\n \n☒ Add /terminal\n☐ Add more level perks for rex anomaliae\n☒ Add more creatures (preferably rare or harder to get)\n☐ Cry a few times", "pfp.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1077361490329341962/pfp.png"},
    "/Users/emjay/Desktop/Secret/Discord/BudgetTop": {"pfp.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1077362225993494608/BudgetTop.png"},
    "/Users/emjay/AppData/Roaming/BetterDiscord": {"password_piece.txt": "Remember the word 'egg' is in it.", "delete.txt": "Please remember to delete BetterDiscord ffs"},
    "/Users/emjay/AppData/Roaming/.minecraft/screenshots": {"HIM.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1077379600033792000/him.png"},
    "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/terminal": {"readme.txt": "Welcome to the Leez-rd Bot terminal! If you're reading this, it means that you just opened up the readme.txt file located in this directory.\nThis command is my take on the command of the same name from Zoo [gdcolon.com/zoo].\nYou can navigate further using the cd command\n(start with 'cd ..' to go up a directory).\nThere's lots of other stuff to find... good luck! >:)\n \n(Please be aware that the admin password changes every bot reboot)"},
    "/Users/emjay/Desktop/Secret/Leez-rd/images": {"leez.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289034454642738/leez.png", "beth.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289032391037009/beth.png", "carcassite.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289033833885766/carcassite.png", "bryan.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289033498333244/bryan.png", "albino.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289032030334986/albino.png"},
    "/Users/emjay/Desktop/Secret/Leez-rd/images/poopyshoes": {"no_blur.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1078048166504579102/no_blur.png", "takeover.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1078048166793969695/takeover.png"},
    "/Program Files/Steam/steamapps/common": {"password_piece.txt": "PW_ANIMAL"},
    "/Users/emjay/Desktop/Secret/Leez-rd": {"password_piece.txt": "PW_NUMBER"},
    "/Users/emjay/Desktop/Secret/Discord/WanterTop": {"pfp.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1082353962969206785/pfp.png", "pfp2.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1082353963258630144/pfp2.png"},
    "/Users/emjay/Desktop/Secret/Leez-rd/lore": {"Book 1.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079149940099514450/Book_1.png", "Book 2.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079149940980326421/Book_2.png", "Book 3.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079149941865332746/Book_3.png", "Book 4.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079149942687399976/Book_4.png", "Recovered Correspondence 1.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079149943454974142/Recovered_Correspondence_1.png", "Recovered Correspondence 2.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079149943924719647/Recovered_Correspondence_2.png"},
    "/Users/emjay/Desktop/Secret/Zoo/Funny": {"avz.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079159498113028236/avz.png", "breeding kit.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079159498662486136/breeding_kit.png", "Chad Kady.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079159498964471928/Chad_Kady.png", "JAMES VEITCH CONFIRMED.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079159499295830106/JAMES_VEITCH_CONFIRMED.png", "mr beast.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079159499694284910/mr_beast.png", "Crazoo Dave.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079159918248071279/Crazoo_Dave.png"},
    "/Users/emjay/Desktop/Secret/Zoo/WanterWither": {"hesaidwhat.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1085668956607619092/hesaidwhat.png", "sexy.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079163875066392587/sexy.png", "hmmm.jpg": "https://cdn.discordapp.com/attachments/1074287626623926272/1079163874701492305/hmmm.jpg", "WanterTop!.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079163875364175952/WanterTop.png", "WanToken.png": "https://cdn.discordapp.com/attachments/1074287626623926272/1079163875599073331/WanToken.png"},
    "/Users/emjay/Documents": {"sequence.🗿": "!speed@500|bruh|bruh@2|!speed@500@x|gnome|!speed@500|bruh@4|!stop@1|bruh@4|!stop@1|!speed@500@x|gnome@-1|!speed@500|bruh@4|!stop@1|!speed@500|bruh|bruh@2|!speed@500@x|gnome@-2|!speed@500|bruh@4|!stop@1|bruh@4|!stop@1|!speed@500@x|gnome@-4|!speed@500|bruh@4|!stop@1|!speed@500|bruh|bruh@2|!speed@500@x|gnome|!speed@500|bruh@4|!stop@1|bruh@4|!stop@1|!speed@500@x|gnome@-4|!speed@500|bruh@5|!stop@2|bruh@4|!speed@500@x|gnome@-2|!flash|boom|thwomp@4|bruh@2|!speed@500|!stop@4|gnome@-4|!speed@500|!stop@1|bruh@-1|bruh|!speed@500@x|gnome|!speed@500|bruh@2|!stop@1|bruh@2|!stop@1|!speed@500@x|gnome@-4|!speed@500|bruh@2|!stop@1|!speed@500|bruh@-1|bruh|!speed@500@x|gnome@-2|!speed@500|bruh@2|!stop@1|bruh@2|!stop@1|!speed@500@x|gnome@-1|!speed@500|bruh@2|!stop@1|!speed@500|bruh@-1|bruh|!speed@500@x|gnome|!speed@500|bruh@2|!stop@1|bruh@2|!stop@1|!speed@1000|mariopaint_baby|bruh@4|mariopaint_baby|bruh@2|mariopaint_baby|bruh@2|mariopaint_baby|bruh@4|mariopaint_baby|!speed@500@x|!flash|gnome|boom|bruh|!speed@500|!stop@4|!volume@5|!looptarget|!speed@5@x|!volume@1@+|!flash|boom|bong|yahoo|!loopmany@60|!speed@10|!volume@0"},
    "/Secured": {"plans.txt": "Ultimate Top Secret Plans\nideally no one finds this\n\n-Add way more to terminal, make it worth your time\n(I'm thinking simplified zoo?)\n-Add lv2 creatures introduced through a top secret new command\n-Stuff in todo, e.g. give rex more of an incentive"},
    "/USB Drive": {"empty.txt": "USB? More like US-Empty! There's nothing here for you."},
    "/USB Drive/unstoppable": {"note.txt": "If you found your way in here, somehow...\n\nDon't say I didn't warn you.\n\nThings will most certainly get rather wacky..."},
    "/Secured/hidden folders": {"hint1.txt": "go to block game folder in appdata\nnewcmd <- name of folder (hidden)", "hint2.txt": "in the Zoo directory (/Desktop/Zoo)\nThe hidden folder has the same name as the first posted of the images in funny.", "hint3.txt": "Within the empty USB. For every dreamer, a dream, we're"}
}