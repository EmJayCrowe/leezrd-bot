# The codebase for this bot is an utter mess. It was the first larger-scale coding thing I ever did.
# Some of it is so ancient and unreadable that I struggle to understand and interpret it.
# There's no new comments on this file, because really I'm not too fussed.

# Feel free to reach out though, I'll do my best to explain anything and everything
# Discord - https://derpymon.xyz/@/discord
# Bluesky - https://derpymon.xyz/@/bsky




import discord
from discord import app_commands
from discord import user
from config import TOKEN
from discord import AppCommandOptionType
from discord.utils import get
from typing import Optional
import random
from math import trunc

import calendar
import datetime
import math

from pathlib import Path
import ast

import json

import bcbscommand
from bcbscommand import verbused_said
from bcbscommand import verbused_ate
from bcbscommand import verbused_travel
from bcbscommand import verbused_moved
from bcbscommand import verbused_listened
from bcbscommand import verbused_played
from bcbscommand import extension_said
from bcbscommand import extension_ate
from bcbscommand import extension_travel
from bcbscommand import extension_moved
from bcbscommand import extension_played
from bcbscommand import sentencestrs
from bcbscommand import nouns
from bcbscommand import verbs
from bcbscommand import music

from terminal_directories import ter_dirs
from terminal_directories import ter_backdirs
from terminal_directories import ter_content

from pingmsgs import ping_msg
from pingmsgs import high_ping_msg
from pingmsgs import zero_ping_msg
from pingmsgs import negative_ping_msg

print(len(nouns))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

terAdmin_animal = random.choice(["tapir", "DUCK", "caterpillar", "dodo", "BETH"])
terAdmin_animalhints = {
    "tapir": "your real favourite animal. Not the one you pretend is on Discord. Also it's in all lowercase.",
    "DUCK": 'your "favourite" animal. '+"Also it's in all uppercase.",
    "caterpillar": "the animal WanterWither likes. Also it's in all lowercase.",
    "dodo": "the one that's famously extinct. Also it's in all lowercase.",
    "BETH": "the one from the Leez-rd Realm. Can they count as animals? Anyway, the one that 'has lots of relatives' apparently. Also it's in all uppercase."
}
terAdmin_number = str(random.choice(range(1111, 10000)))
terAdmin_pokenumber = random.choice(["123", "234", "345", "456", "567", "678", "789", "890"])
terAdmin_pokes = {
    "123": "Scyther",
    "234": "Stantler",
    "345": "Lileep",
    "456": "Finneon",
    "567": "Archeops",
    "678": "Meowstic",
    "789": "Cosmog",
    "890": "Eternatus"
}
terAdmin_finalpoke = terAdmin_pokes[terAdmin_pokenumber]

terAdmin_password = terAdmin_finalpoke+"egg"+str(terAdmin_number)+terAdmin_animal

ter_pieceResponses = {
    "animal": "Remember the animal. It's ",
    "number": "Don't forget the number. It's ",
    "pokemon": "Don't forget the Pokémon. "
}

print("Today's password is "+terAdmin_password)
#error msgs

noitems = ["https://cdn.discordapp.com/attachments/841741493010038785/1070059897644908705/error.png", "nice lack of items you got there", "you don't have any of that!", "you do know you don't have that item, right?", "you actually have 0 of those thank you"]
nocreatures = ["https://cdn.discordapp.com/attachments/841741493010038785/1070059999319052288/error.png", "nice lack of creatures you got there", "maybe try actually catching that first"]
notdev = ["No Entry", "get your own bot to test!", "no", "nice try", "You're not jsakosasnjams enough", "do you possess The Duck? I think not.", "Excuse me"]
notrex = ["A great feat must be achieved first...", "You are not ready...", "You must first accomplish a noble task...", "Wake the sleeping giant first..."]
creaturebutitem = ["that's an item, not a creature?", "that's an item you dingbat", "https://cdn.discordapp.com/attachments/841741493010038785/1070421924997505165/error.png", "That's no creature I've seen before..."]
itembutcreature = ["that's a creature, not an item?", "that's a creature you dingbat", "https://cdn.discordapp.com/attachments/841741493010038785/1070421924997505165/error.png", "That's no item I've seen before..."]
nofile = ["That user doesn't exist!", "That's an invalid user...", "That user has no associated data, or doesn't exist."]

#catch vars

commons = ["leez", "beth", "residue"]
uncommons = ["bryan", "carcassite"]
rares = ["albino", "poopyshoes", "frorg"]
items = ["paintbrush", "stopwatch", "label", "steak", "beans", "cherry", "compass", "stopwatch", "steak", "beans", "cherry", "compass"]
trophies = ["bug", "hand", "legacy", "duck", "pillar", "first", "lucky", "luckier", "waste", "contributor", "compendium", "bertmedal", "cake", "cakiercake"]

ter_validcommands = ["cd", "help", "uwu", "adminunlock", "raphael", "clearcol", "alter", "compendium", "rebuild", "prism", "remove", "aqua", "altaqua", "list", "funky", "dreams", "bert"]


berts = {
    "wanterbert": {"name": "WanterBert", "emoji": "<:wanterbert:1153441065437765683>"},
    "diabert": {"name": "Diabert", "emoji": "<:diabert:1125505787205271633>"},
    "starbert": {"name": "Starbert", "emoji": "<:starbert:1125505793333133342>"},
    "giraffebert": {"name": "Giraffe Bert", "emoji": "<:giraffebert:1125505788497121411>"},
    "barbaribert": {"name": "Barbaribert", "emoji": "<:barbaribert:1125505784676098100>"},
    "nert": {"name": "Nert", "emoji": "<:nert:1125505791508615230>"},
    "antibert": {"name": "Anti-bert", "emoji": "<:antibert:1125505783547838575>"},
    "kingbert": {"name": "King Bert", "emoji": "<:kingbert:1125505790514561236>"},
    "mythicbert": {"name": "Mythic Bert", "emoji": "<:mythicbert:1153441042692059297>"}
}

valid_dreams = {"leez": ["82359", "14631", "72586"],
                "beth": ["51312", "68730"]
                
                }

ter_cmds = {
    "cd": {"help": "Changes the directory of the terminal. Use "+'".."'+" to go back one directory, or "+'"home"'+" to return to the start. The current folder can be viewed with `$ cd //`.", "usage": "`$ cd [path]`", "examples": "`$ cd folder`\n`$ cd ..`"},
    "help": {"help": "Lists most discovered commands, or provides info on a specific one.", "usage": "`$ help [command?]`", "examples": "`$ help help`"},
    "uwu": {"help": "uwu-ifies text.", "usage": "`$ uwu [text]`"},
    "adminunlock": {"help": "Unlocks admin privileges. Requires a password.", "usage": "`$ adminunlock [password]`"},
    "raphael": {"help": "Stanley.", "usage": "`$ raphael`"},
    "aqua": {"help": "Catch an aquatic animal every six hours!", "usage": "`$ aqua`"},
    "altaqua": {"help": "Catch an 'alt' aquatic animal once every day!", "usage": "`$ altaqua`"},
    "list": {"help": "View your (or someone else's) aqarium!", "usage": "`$ list [user id?]`"},
    "clearcol": {"help": "Removes your custom embed colour.", "usage": "`$ clearcol`"},
    "rebuild": {"help": "Rebuild a prism for special effects.", "usage": "`$ rebuild <red/green/blue/black>`"},
    "funky": {"help": "Randomises your embed colour.", "usage": "`$ funky`"},
    "alter": {"help": "Your next catch will be a 'strange' creature. Overwrites any existing guarantee.\nHas a 24-hour cooldown which can be removed with a contract (</sign:1079498426183602291> `alter`)", "usage": "`$ alter`"},
    "bert": {"help": "Encounter Berts of all different shapes and sizes.", "usage": "`$ bert [subcommand?]`", "examples": "`$ bert`\n`$ bert exchange`"},
    "dreams": {"help": "Enter the dream world!", "usage": "`$ dreams` (View current dream)\n`$ dreams in [creature]` (Enter a dream)\n`$ dreams out` (Exit the dream world)", "examples": "`$ dreams`\n`$ dreams in leez`"}
}


ter_cmdcategories = {
    "system": ["adminunlock", "cd", "help"],
    "fun": ["bert", "funky", "raphael", "uwu"],
    "aqua": ["altaqua", "aqua", "list"],
    "tool": ["alter", "clearcol"],
    "prism": ["prism", "rebuild", "remove"]
}

rexfoods = {
    "leez": 2,
    "beth": 2,
    "bryan": 4,
    "albino": 6,
    "poopyshoes": 7,
    "residue": 2,
    "carcassite": 5,
    "redprismalgam": 6,
    "greenprismalgam": 6,
    "blueprismalgam": 6,
    "blackprismalgam": 16,
    "frorg": 7,
    "bert": 12,
    "jack": 12,
    "ad": 12,
    "adamantprismalgam": 16,
    "dazzlingprismalgam": 16,
    "iridescentprismalgam": 16,
    "mythicprismalgam": 18,
    "markiplier": 14,
    "darkiplier": -1,
    "paintbrush": 4,
    "stopwatch": 4,
    "label": 4,
    "steak": 7,
    "beans": 7,
    "cherry": 7,
    "compass": 4,
    "stew": 15,
    "contract": 7
}

unusableitems = ["redshard", "greenshard", "blueshard", "blackshard", "cherry", "paintbrush", "label", "contract", "mythicenergy"]

catchmsgs = ["crossed paths with", "encountered", "rescued", "caught", "took in", "met", "ran into", "found", "made friends with", "scored"]

specialprivileges = [793441657227313174, 705750043671658537, 990710399043264524, 815350320959193128]
dev = [793441657227313174, 990710399043264524]

creaturedata = {
    "leez": {"rarity": 1, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289034454642738/leez.png", "emoji": "<:leezrd:831177020108963890>", "name": "Leez-rd", "an": "a ", "id": "leez", "colour": {"red": 40, "green": 180, "blue": 0}, "desc": "One of the most common creatures in the Leez-rd Realm, however elsewhere they are mostly unheard of. There are 6 theoretical species of Leez-rd, but only 4 have been proven to exist."},
    "beth": {"rarity": 1, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289032391037009/beth.png", "emoji": "<:beth:905871385379893289>", "name": "Beth", "an": "a ", "id": "beth", "colour": {"red": 230, "green": 230, "blue": 255}, "desc": "Beth has a caring demeanour. It, like most creatures in the Leez-rd Realm, does not sexually reproduce. Beth clones itself. Which is the real one...?"},
    "residue": {"rarity": 1, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289314344742982/residue.png", "emoji": ":grey_question:", "name": "Leez-rd Residue", "an": "some ", "id": "residue", "colour": {"red": 200, "green": 210, "blue": 220}, "desc": "Among the stranger Leez-rd types. These form when a Healy Leez-rd resurrects a dead Leez-rd. They are not recognised as living organisms."},
    "bryan": {"rarity": 2, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289033498333244/bryan.png", "emoji": "<:bryan:930494048949641227>", "name": "Bryan", "an": "​", "id": "bryan", "colour": {"red": 200, "green": 40, "blue": 40}, "desc": "A relative of Beth, he doesn't like the colour red very much, which causes some problems."},
    "carcassite": {"rarity": 2, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289033833885766/carcassite.png", "emoji": "<:carcassite:1041737974947254445>", "name": "Carcassite", "an": "a ", "id": "carcassite", "colour": {"red": 130, "green": 170, "blue": 130}, "desc": "A parasitical species held resposible for the extinction of Healy Leez-rds. It brings Leez-rds close to death before taking control of them."},
    "albino": {"rarity": 3, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289032030334986/albino.png", "emoji": "<:albinoleezrd:838122895225782322>", "name": "albino Leez-rd", "an": "an ", "id": "albino", "colour": {"red": 255, "green": 255, "blue": 225}, "desc": "Wow! Albinism also affects Leez-rds, and more commonly than you might think. The pale skin and red eyes make it look adorable. Don't you agree?"},
    "poopyshoes": {"rarity": 3, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289034827939870/poopyshoes.png", "emoji": "<:poopyshoes:963147618626723840>", "name": "Poopyshoes", "an": "​", "id": "poopyshoes", "colour": {"red": 0, "green": 106, "blue": 160}, "desc": "An interesting figure whose background and personality are very much unknown. There have been few recorded sightings of him."},
    "redprismalgam": {"rarity": 2, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289035209609227/redamalg.png", "emoji": "<:redprismalgam:1070437926971912204>", "name": "Red Prismalgam", "an": "a ", "id": "redprismalgam", "colour": {"red": 255, "green": 10, "blue": 10}, "desc": "Sometimes prismification can have some... interesting results. This creature is a manifestation of the adamant Red Prism's energy."},
    "greenprismalgam": {"rarity": 2, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289034182004776/greenalamg.png", "emoji": "<:greenprismalgam:1070433518569656451>", "name": "Green Prismalgam", "an": "a ", "id": "greenprismalgam", "colour": {"red": 10, "green": 255, "blue": 10}, "desc": "Sometimes prismification can have some... interesting results. This creature is a manifestation of the dazzling Green Prism's energy."},
    "blueprismalgam": {"rarity": 2, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289033095692318/blueamalg.png", "emoji": "<:blueprismalgam:1070437016539516959>", "name": "Blue Prismalgam", "an": "a ", "id": "blueprismalgam", "colour": {"red": 10, "green": 10, "blue": 255}, "desc": "Sometimes prismification can have some... interesting results. This creature is a manifestation of the iridescent Blue Prism's energy."},
    "blackprismalgam": {"rarity": 3, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074289032722395246/blackamalg.png", "emoji": "<:blackprismalgam:1071878412102283274>", "name": "Black Prismalgam", "an": "a ", "id": "blackprismalgam", "colour": {"red": 20, "green": 20, "blue": 20}, "desc": "The closest living representation of the Original Prism, drawing from red, green, and blue energy."},
    "adamantprismalgam": {"rarity": 4, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1080854790927568956/adamantamalg.png", "emoji": "<:adamantprismalgam:1080855118137790474>", "name": "Adamant Prismalgam", "an": "an ", "id": "adamantprismalgam", "colour": {"red": 250, "green": 165, "blue": 25}, "desc": "The truest representation of the Red Prism's light. Its appearance is eerily similar to that of a Carcassite, prompting many theories on how prismification works."},
    "dazzlingprismalgam": {"rarity": 4, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1080854791447642284/dazzlingamalg.png", "emoji": "<:dazzlingprismalgam:1080855124034977822>", "name": "Dazzling Prismalgam", "an": "a ", "id": "dazzlingprismalgam", "colour": {"red": 100, "green": 75, "blue": 95}, "desc": "The truest representation of the Green Prism's light. Its uncanny resemblance to Leez-rds could provide some insight into understanding prismification."},
    "iridescentprismalgam": {"rarity": 4, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1080854791737065532/iridescentamalg.png", "emoji": "<:iridescentprismalgam:1080855127063277638>", "name": "Iridescent Prismalgam", "an ": "an ", "id": "iridescentprismalgam", "colour": {"red": 155, "green": 20, "blue": 210}, "desc": "The truest representation of the Blue Prism's light. Its peculiar similarities to Beth could help provide explanation to how prismification works."},
    "mythicprismalgam": {"rarity": 4, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1080854791204388904/amalg.png", "emoji": "<:mythicprismalgam:1080855120746659884>", "name": "Mythic Prismalgam", "an": "a ", "id": "mythicprismalgam", "colour": {"red": 255, "green": 255, "blue": 255}, "desc": "A representation of the Original Prism's light. It bares a strong resemblance to Frorgs, a creature of black light, which has created many new theories on prismification."},
    "frorg": {"rarity": 3, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1074423527047962745/frorg.png", "emoji": "<:frorg:1074423071248764938>", "name": "Frorg", "an": "a ", "id": "frorg", "colour": {"red": 0, "green": 200, "blue": 170}, "desc": "A peculiar creature distantly related to Beth. They have become a regular nuisance, as hundreds *can* and *will* swarm areas."},
    "bert": {"rarity": -1, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1079425664643506277/Bert.png", "emoji": "<:bert:1079448808729104485>", "name": "Bert", "an": "a ", "id": "bert", "colour": {"red": 255, "green": 230, "blue": 200}, "desc": "A creature from another world. Some have noticed the uncanny resemblance to Beth and its family tree, but it is *definitely* a fungus."},
    "jack": {"rarity": -1, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1079425664916140202/Jack.png", "emoji": "<:jack:1079448810641707099>", "name": "Jack", "an": "​", "id": "jack", "colour": {"red": 210, "green": 220, "blue": 40}, "desc": "A creature brought in from another world, frequently hunted by another creature. They were born in a disturbing event."},
    "ad": {"rarity": -1, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1079425664375066824/Ad.png", "emoji": "<:ad:1079448805847597156>", "name": "Ad", "an": "​", "id": "ad", "colour": {"red": 255, "green": 240, "blue": 0}, "desc": "Ad is a very handsome fellow, however it hides a dark secret; it hunts another creature for sport. It is from another world."},
    "markiplier": {"rarity": 99, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1091487758024986736/markiplier.png", "emoji": "<:markiplier:1091487216326422528>", "name": "Markiplier", "an": "​", "id": "markiplier", "colour": {"red": 255, "green": 255, "blue": 255}, "desc": "Hello everybody my name is Markiplier."},
    "darkiplier": {"rarity": 99, "catchicon": "https://cdn.discordapp.com/attachments/1074287626623926272/1091487757781704744/darkiplier.png", "emoji": "<:darkiplier:1091487211775610961>", "name": "Darkiplier", "an": "​", "id": "darkiplier", "colour": {"red": 0, "green": 0, "blue": 0}, "desc": "Hello everybody my name is Darkiplier."},


}

itemdata = {
    "paintbrush": {"emoji": ":paintbrush:", "name": "paintbrush", "an": "a ", "consumable": 0, "id": "paintbrush", "desc": "Change the embed colour of most menus to one of your choosing."},
    "stopwatch": {"emoji": ":stopwatch:", "name": "stopwatch", "an": "a ", "consumable": 1, "id": "stopwatch", "desc": "Conveniently reduces your /catch cooldown by 30 minutes."},
    "label": {"emoji": ":label:", "name": "label", "an": "a ", "consumable": 0, "id": "label", "desc": "Lets you change the name the bot uses for you."},
    "steak": {"emoji": ":cut_of_meat:", "name": "steak", "an": "a ", "consumable": 1, "id": "steak", "desc": "A delicious steak. Guarantees a *Leez-rd type creature* on your next catch.\n\nAlternatively, feed it to Rex Anomaliae for lots of energy!"},
    "beans": {"emoji": ":beans:", "name": "beans", "an": "​", "consumable": 1, "id": "beans", "desc": "Some fancy beans. Guarantees a *Beth type creature* on your next catch.\n\nAlternatively, feed it to Rex Anomaliae for lots of energy!"},
    "redshard": {"emoji": "<:redshard:1070017410205241374>", "name": "red shard", "an": "a ", "consumable": 0, "id": "redshard", "desc": "An ancient shard that fell from the adamant Red Prism. Often used in prismification."},
    "greenshard": {"emoji": "<:greenshard:1070017427183771799>", "name": "green shard", "an": "a ", "consumable": 0, "id": "greenshard", "desc": "An ancient shard that fell from the dazzling Green Prism. Often used in prismification."},
    "blueshard": {"emoji": "<:blueshard:1070017442295840929>", "name": "blue shard", "an": "a ", "consumable": 0, "id": "blueshard", "desc": "An ancient shard that fell from the iridescent Blue Prism. Often used in prismification."},
    "cherry": {"emoji": ":cherries:", "name": "twin cherry", "an": "a ", "consumable": 0, "id": "cherry", "desc": "A juicy, sweet cherry. Doubles what you find from /catch.\n\nAlternatively, feed it to Rex Anomaliae for lots of energy!"},
    "compass": {"emoji": ":compass:", "name": "compass", "an": "a ", "consumable": 1, "id": "compass", "desc": "Rather helpfully reduces your remaining quest length by 3 hours."},
    "stew": {"emoji": ":stew:", "name": "stew", "an": "a bowl of ", "consumable": 1, "id": "stew", "desc": "A stew that tastes... interesting. Guarantees a *rare creature* on your next catch.\n\nAlternatively, feed it to Rex Anomaliae for *TONS* of energy!"},
    "contract": {"emoji": ":scroll:", "name": "contract", "an": "a ", "consumable": 1, "id": "contract", "desc": "Signing this contract allows you to completely remove one cooldown."},
    "blackshard": {"emoji": "<:blackshard:1071862902379790468>", "name": "black shard", "an": "a ", "consumable": 0, "id": "blackshard", "desc": "A deeply mysterious shard that may have fallen from the Original Prism. It is simultaneously adamant, dazzling and iridescent."},
    "mythicenergy": {"emoji": "<:mythicenergy:1080212197797539991>", "name": "mythic energy", "an": "a vessel of ", "consumable": 0, "id": "mythicenergy", "desc": "A vessel that contains the very essence of light and being. It must have some purpose."}
}

questemojis = {
    "leez": "<:leezrd:831177020108963890>",
    "beth": "<:beth:905871385379893289>",
    "bryan": "<:bryan:930494048949641227>",
    "albino": "<:albinoleezrd:838122895225782322>",
    "poopyshoes": "<:poopyshoes:963147618626723840>",
    "residue": ":grey_question:",
    "carcassite": "<:carcassite:1041737974947254445>",
    "redprismalgam": "<:redprismalgam:1070437926971912204>",
    "greenprismalgam": "<:greenprismalgam:1070433518569656451>",
    "blueprismalgam": "<:blueprismalgam:1070437016539516959>",
    "blackprismalgam": "<:blackprismalgam:1071878412102283274>",
    "frorg": "<:frorg:1074423071248764938>",
    "bert": "<:bert:1079448808729104485>",
    "jack": "<:jack:1079448810641707099>",
    "ad": "<:ad:1079448805847597156>",
    "adamantprismalgam": "<:adamantprismalgam:1080855118137790474>",
    "dazzlingprismalgam": "<:dazzlingprismalgam:1080855124034977822>",
    "iridescentprismalgam": "<:iridescentprismalgam:1080855127063277638>",
    "mythicprismalgam": "<:mythicprismalgam:1080855120746659884>",
    "markiplier": "<:markiplier:1091487216326422528>",
    "darkiplier": "<:darkiplier:1091487211775610961>",
    "paintbrush": ":paintbrush:",
    "stopwatch": ":stopwatch:",
    "label": ":label:",
    "redshard": "<:redshard:1070017410205241374>",
    "greenshard": "<:greenshard:1070017427183771799>",
    "blueshard": "<:blueshard:1070017442295840929>",
    "steak": ":cut_of_meat:",
    "beans": ":beans:",
    "cherry": ":cherries:",
    "compass": ":compass:",
    "stew": ":stew:",
    "contract": ":scroll:",
    "blackshard": "<:blackshard:1071862902379790468>"
}

catchshardamts= {
    "leez": 2,
    "beth": 2,
    "residue": 2,
    "bryan": 3,
    "carcassite": 3,
    "albino": 3,
    "poopyshoes": 4,
    "redprismalgam": 2,
    "greenprismalgam": 2,
    "blueprismalgam": 2,
    "blackprismalgam": 4,
    "frorg": 4,
    "bert": 4,
    "jack": 4,
    "ad": 4,
    "adamantprismalgam": 4,
    "dazzlingprismalgam": 4,
    "iridescentprismalgam": 4,
    "mythicprismalgam": 4,
    "markiplier": 4,
    "darkiplier": 2
}

catchguaranshards= {
    "leez": "greenshard",
    "beth": "blueshard",
    "residue": "blueshard",
    "bryan": "redshard",
    "carcassite": "redshard",
    "albino": "greenshard",
    "poopyshoes": "blueshard",
    "redprismalgam": "redshard",
    "greenprismalgam": "greenshard",
    "blueprismalgam": "blueshard",
    "blackprismalgam": "blackshard",
    "frorg": "blueshard",
    "bert": "blackshard",
    "jack": "blackshard",
    "ad": "blackshard",
    "adamantprismalgam": "redshard",
    "dazzlingprismalgam": "greenshard",
    "iridescentprismalgam": "blueshard",
    "mythicprismalgam": "blackshard",
    "markiplier": "blackshard",
    "darkiplier": "blackshard"
}

reds = ["carcassite", "bryan", "redprismalgam"]
greens = ["leez", "albino", "greenprismalgam"]
blues = ["beth", "residue", "blueprismalgam"]
blacks = ["frorg", "redprismalgam", "greenprismalgam", "blueprismalgam", "poopyshoes", "blackprismalgam"]

shards = ["redshard", "greenshard", "blueshard"]
shards_black = ["redshard", "greenshard", "blueshard", "blackshard"]

funNicks = {
    "matthew": {"allowed": True, "msg": "..."},
    "poopyshoes": {"allowed": True, "msg": "<:poopyshoes:963147618626723840>"},
    "jsakosasnjams": {"allowed": True, "msg": "Hey, how'd you know?"},
    "aaron": {"allowed": True, "msg": "Caterpillar."},
    "emjay": {"allowed": False, "msg": "I already took that one."},
    "emjaycrowe": {"allowed": False, "msg": "I already took that one."},
    "wanterwither": {"allowed": True, "msg": "Caterpillar."},
    "colon": {"allowed": True, "msg": "The best punctuation mark!"},
    "gdcolon": {"allowed": True, "msg": "The best punctuation mark!"},
    "craig": {"allowed": True, "msg": "Who names their son Craig?"},
    "leez": {"allowed": True, "msg": "The original."},
    "beth": {"allowed": True, "msg": "Is everyone in the world related to you?"},
    "leez-rd": {"allowed": True, "msg": "The original."},
    "orteil": {"allowed": True, "msg": "But that's not you, is it?"},
    "ortiel": {"allowed": True, "msg": "But that's not you, it it...?"},
    "markiplier": {"allowed": True, "msg": "Hello everybody my name is Markiplier."},
    "raphael": {"allowed": True, "msg": "Stanley."},
    "stanley": {"allowed": True, "msg": "This is the story of a man named Stanley."},
    "fuck": {"allowed": False, "msg": "Try harder than that"},
    "penis": {"allowed": False, "msg": "Invalid nickname: not long enough"},
    "niko": {"allowed": True, "msg": "They are the messiah!!!"},
    "frisk": {"allowed": True, "msg": "Imagine if there was a hard mode"},
    "chara": {"allowed": True, "msg": "The true name."},
    "duck": {"allowed": True, "msg": ":duck:"},
    "caterpillar": {"allowed": True, "msg": ":bug:"},
    "pillar": {"allowed": True, "msg": ":bug:"},
    "nick": {"allowed": True, "msg": "I mean, it IS a name..."},
    "name": {"allowed": True, "msg": "I bet you think you're so clever"},
    "abc": {"allowed": True, "msg": "That-that barely even counts as a name!"},
    "nickname": {"allowed": True, "msg": "I suppose it is a name. I'll allow it."},
    "qwerty": {"allowed": True, "msg": "I think that's a keyboard, not a name"},
    "qwertyuiop": {"allowed": True, "msg": "How many nicknames have you tried at this point?"},
    "qwertyuiopasdfghjkl": {"allowed": True, "msg": "...how do I respond to this"},
    "qwertyuiopasdfghjklzxcvbnm": {"allowed": True, "msg": "That's a name."},
    "asdfghjkl": {"allowed": False, "msg": "That's not a name."},
    "asdf": {"allowed": True, "msg": "The ska of tom!!!!"},
    "zxcvbnm": {"allowed": False, "msg": "I forbid it"},
    "plmoknijbuhvygctfxrdzeswaq": {"allowed": False, "msg": "just stop"},
    "qazwsxedcrfvtgbyhnujmikolp": {"allowed": False, "msg": "just stop"},
    "qazxswedcvfrtgbnhyujmkiolp": {"allowed": False, "msg": "please stop"},
    "plmkoijnbhuygvcftrdxzsewaq": {"allowed": False, "msg": "please stop"},
    "phishy": {"allowed": True, "msg": "yes Hello! IT iz mee CoinFrend Phishy!!"},
    "spamton": {"allowed": False, "msg": "I WILL NOT [Just Stand There & Comply With] THIS [Slanderous Misuse] OF MY [Branding]!!"},
    "legs": {"allowed": True, "msg": "Ah yes, my beautiful- huh? That't the NAME you've picked?"},
    "tom scott": {"allowed": True, "msg": "I got an email..."},
    "flipper": {"allowed": True, "msg": "More like sipper... of tropical drinks"},
    "robotop": {"allowed": False, "msg": "No... that would be disrespectful."},
    "robobor": {"allowed": False, "msg": "No... that would be disrespectful."},
    "polaris": {"allowed": False, "msg": "No... that would be disrespectful."},
    "polarstar": {"allowed": False, "msg": "No... that would be disrespectful."},
    "zoo": {"allowed": False, "msg": "No... that would be disrespectful."},
    "zoo 2": {"allowed": False, "msg": "No... that would be disrespectful."},
    "witherbot": {"allowed": False, "msg": "No... that would be disrespectful."},
    "witherstormbot": {"allowed": False, "msg": "No... that would be disrespectful."},
    "wantertop": {"allowed": False, "msg": "I PROMISE I'LL UPDATE IT SOON"},
    "witherbro": {"allowed": True, "msg": "Uh... sure. This one isn't taken, right?"},
    "robolite": {"allowed": True, "msg": "Uh... sure. This one isn't taken, right?"},
    "cookies": {"allowed": True, "msg": "So you like time travel?"},
    "bo": {"allowed": True, "msg": "Oh my god!"},
    "yellow": {"allowed": True, "msg": "Not one for talking?"},
    "dr. prof": {"allowed": True, "msg": "So you like rats"},
    "dr prof": {"allowed": True, "msg": "So you like rats"},
    "dr. professor": {"allowed": True, "msg": "So you like rats"},
    "dr professor": {"allowed": True, "msg": "So you like rats"},
}
funPasswords = {
    "emjay": "no",
    "matthew": "no",
    "poopyshoes": "no",
    "wench": "WHO TOLD YOU?!",
    "h4xx": "WHO TOLD YOU?!",
    "jsakosasnjams": "You dare try and harness the power of jsakosasnjams??",
    "emjaycrowe": "no",
    "leez": "The original.",
    "leez-rd": "The original.",
    "colon": "He's cute",
    "2845": "You couldn't possibly have known this",
    "nightshark115": ":zipper_mouth:",
    "password": "Are you serious?!",
    "duck": ":duck:",
    "passcode": "Are you serious?!",
    "hunter2": "How very secure",
    "rubrubpowah123": "This is getting stupid...",
    "adminunlock": "how meta of you",
    "ixnoah": "Password does not know how to code",
    "wanterwither": "WanterWither? I hardly know her...",
    "e": "There's always an E in "+'"nerd"',
    "e!": "There's always an E in "+'"nerd"',
    "1234": "no",
    "12345": "nope",
    "12345": "Uh uh uh!",
    "123456": "Nosiree Bob!",
    "1234567": "That's snot it!",
    "12345678": "nah",
    "123456789": "no. just no.",
    "1234567890": "That's... hmmm maybe this one will pass",
    "12345678901": "Ooh! Now we're talking",
    "qwerty": "creativity at its finest!",
    "qwertyuiop": "creativity at its finest!",
    "273": "No Stinkbug for you",
    "okay,leez-rd,don'ttellanyonebutcolonandnickeh30arereallycute": "...\n \n...yes",
    "flipper": "More like sipper... of tropical drinks",
    "zoo": "Zoo? More like... uhh... zdumb gottem",
    "robotop": "i looove gd cologne",
    "robobor": "i looove gd cologne",
    "polaris": "This bot doesn't have XP, silly",
    "polarstar": "This bot isn't testing XP, silly",
    "zoo2": "Zoo 2? More like... uhh... z2dumb gottem",
    "witherbot": "not here... somewhere... else...",
    "wantertop": "not here... somewhere... else...",
    "witherstormbot": "not here... somewhere... else...",
    "witherbro": "password has been forgotten by everyone.",
    "nowiamseriouslygettingpissedoffiwillshove50fuckingpotatoesupyourassifyoudonotgivemeaccessimmediately": "You're not supposed to be *changing* the password, you're supposed to be *guessing* it!"
}


questrewards = {
    "leez": {
    "rewards": 3,
    "time": 14400,
    "guaranteedReward": "leez",
    "reward1": ["steak", "stopwatch"],
    "reward2": ["leez", "beth", "albino"],
    "reward3": ["greenshard", "leez"]
    },
    "beth": {
    "rewards": 3,
    "time": 14400,
    "guaranteedReward": "beth",
    "reward1": ["beans", "compass"],
    "reward2": ["beth", "bryan"],
    "reward3": ["blueshard", "beth"]
    },
    "residue": {
    "rewards": 3,
    "time": 14400,
    "guaranteedReward": "residue",
    "reward1": ["leez", "beth", "residue"],
    "reward2": ["steak", "beans"],
    "reward3": ["greenshard", "blueshard"]
    },
    "bryan": {
    "rewards": 4,
    "time": 21600,
    "guaranteedReward": "beth",
    "reward1": ["beans", "beth"],
    "reward2": ["beans", "bryan"],
    "reward3": ["beth", "bryan"],
    "reward4": ["redshard", "bryan"]
    },
    "carcassite": {
    "rewards": 3,
    "time": 21600,
    "guaranteedReward": "leez",
    "reward1": ["leez", "albino"],
    "reward2": ["label", "carcassite"],
    "reward3": ["redshard", "carcassite"]
    },
    "albino": {
    "rewards": 5,
    "time": 28800,
    "guaranteedReward": "albino",
    "reward1": ["leez", "albino"],
    "reward2": ["leez", "albino"],
    "reward3": ["leez", "albino"],
    "reward4": ["leez", "albino"],
    "reward5": ["leez", "albino"]
    },
    "poopyshoes": {
    "rewards": 4,
    "time": 43200,
    "guaranteedReward": "poopyshoes",
    "reward1": ["stopwatch", "paintbrush"],
    "reward2": ["stopwatch", "label"],
    "reward3": ["redshard", "greenshard", "blueshard"],
    "reward4": ["stopwatch", "compass"]
    },
    "redprismalgam": {
    "rewards": 3,
    "time": 21600,
    "guaranteedReward": "redshard",
    "reward1": ["redshard", "greenshard"],
    "reward2": ["redshard", "blueshard"],
    "reward3": ["greenshard", "blueshard", "blackshard"]
    },
    "greenprismalgam": {
    "rewards": 3,
    "time": 21600,
    "guaranteedReward": "greenshard",
    "reward1": ["greenshard", "redshard"],
    "reward2": ["greenshard", "blueshard"],
    "reward3": ["redshard", "blueshard", "blackshard"]
    },
    "blueprismalgam": {
    "rewards": 3,
    "time": 21600,
    "guaranteedReward": "blueshard",
    "reward1": ["blueshard", "redshard"],
    "reward2": ["blueshard", "greenshard"],
    "reward3": ["redshard", "greenshard", "blackshard"]
    },
    "blackprismalgam": {
    "rewards": 3,
    "time": 21600,
    "guaranteedReward": "blackshard",
    "reward1": ["redshard", "redshard"],
    "reward2": ["greenshard", "greenshard"],
    "reward3": ["greenshard", "blueshard"]
    },
    "frorg": {
    "rewards": 2,
    "time": 14400,
    "guaranteedReward": "beth",
    "reward1": ["stew", "contract", "blackshard"],
    "reward2": ["stew", "contract", "blackshard"]
    },
    "bert": {
    "cannot": True
    },
    "jack": {
    "cannot": True
    },
    "ad": {
    "cannot": True
    },
    "adamantprismalgam": {
    "cannot": True
    },
    "dazzlingprismalgam": {
    "cannot": True
    },
    "iridescentprismalgam": {
    "cannot": True
    },
    "mythicprismalgam": {
    "cannot": True
    },
    "markiplier": {
    "cannot": True
    },
    "darkiplier": {
    "cannot": True
    },
}

recipes = {
    "recipe1": {
    "sell": {"emoji": ":scroll:", "name": "Contract", "amount": 1, "id": "contract"},
    "buy1": {"emoji": ":paintbrush:", "name": "Paintbrush", "amount": 1, "id": "paintbrush"},
    "buy2": {"emoji": ":label:", "name": "Label", "amount": 1, "id": "label"}
    },
    "recipe2": {
    "sell": {"emoji": ":stew:", "name": "Stew", "amount": 1, "id": "stew"},
    "buy1": {"emoji": ":cut_of_meat:", "name": "Steak", "amount": 1, "id": "steak"},
    "buy2": {"emoji": ":beans:", "name": "Beans", "amount": 1, "id": "beans"}
    },
    "recipe3": {
    "sell": {"emoji": "<:blackshard:1071862902379790468>", "name": "Black Shard", "amount": 1, "id": "blackshard"},
    "buy1": {"emoji": "<:redshard:1070017410205241374>", "name": "Red Shard", "amount": 1, "id": "redshard"},
    "buy2": {"emoji": "<:greenshard:1070017427183771799>", "name": "Green Shard", "amount": 1, "id": "greenshard"}
    }
}

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Logged in! {self.user} at your service.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description = "Hopefully pings the bot.")
async def self(interaction: discord.Interaction):

    await interaction.response.send_message(":ping_pong:")

    pingtime = random.choice(range(-1,640)) #yes ping times are random. i cba to implement actual ones
    if pingtime == 69 or pingtime == 420:
        await interaction.edit_original_response(content="nice ("+str(pingtime)+"ms)")
    elif pingtime == -1:
        await interaction.edit_original_response(content=random.choice(negative_ping_msg)+" ("+str(pingtime)+"ms)")
    elif pingtime > 0:
        if pingtime > 479:
            await interaction.edit_original_response(content=random.choice(high_ping_msg)+" ("+str(pingtime)+"ms)")
        else:
            await interaction.edit_original_response(content=random.choice(ping_msg)+" ("+str(pingtime)+"ms)")
    else:
        await interaction.edit_original_response(content=random.choice(zero_ping_msg)+" ("+str(pingtime)+"ms)")

@app_commands.checks.cooldown(1, 60, key=lambda i: (i.user.id))
@tree.command(name="shinyroll", description="Roll for a shiny Leez-rd with 1/256 odds!")
async def test(interaction: discord.Interaction):
        shiny = random.choice(range(1,7))
        if shiny == 1:
            userid = str(interaction.user.id)
            path = Path("./"+userid+".txt")

            if not (path).is_file():
                filemake = {}
                with open(path, 'w') as f:
                    f.write(str(filemake))
                f.close()

            with open(path) as f:
                data = f.read()
            f.close()

            caughtdict = ast.literal_eval(data)

            if "luckier" in caughtdict.keys():
                await interaction.response.send_message("<:albinoleezrd:838122895225782322>:sparkles: You found a **shiny** Leez-rd!\n(1 & 1)\nYou found... ANOTHER... shiny Leez-rd? I give up with you.")
            elif "lucky" in caughtdict.keys():
                caughtdict["luckier"] = 1
                await interaction.response.send_message("<:albinoleezrd:838122895225782322>:sparkles: You found a **shiny** Leez-rd!\n(1 & 1)\nWait... but haven't you... haven't you already... YOU'VE FOUND *TWO* SHINY LEEZ-RDS??! Okay, whatever, take... uhh... a <:lucky2:1071193862749569086> **Luck*ier* Trophy**?!")
            else:
                caughtdict["lucky"] = 1
                await interaction.response.send_message("<:albinoleezrd:838122895225782322>:sparkles: You found a **shiny** Leez-rd!\n(1 & 1)\nYou have earned the :sparkles: **Lucky Trophy**! Congrats!")
            
            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
            f.close()

        else:
            await interaction.response.send_message("<:leezrd:831177020108963890> You just found a regular Leez-rd. Bummer.\n(1 & "+str(shiny)+")")
@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message("You're on cooldown! Try again later.", ephemeral=True)

#bcbs

@tree.command(name="bcbs", description="Bread Crumbs and Beaver Spit. Generates a random(ish) sentence.")
async def test(interaction: discord.Interaction):
        chosensentencestr = random.choice(sentencestrs)
        chosennoun1 = (random.choice(['a ','the ']) + random.choice(nouns))
        chosennoun2 = (random.choice(['a ','the ']) + random.choice(nouns))
        chosenroot1 = random.choice(verbs)
        if chosenroot1 == "said":
            verb1used = random.choice(verbused_said)
            verb1ext = ('"' + random.choice(extension_said) + '"')
        elif chosenroot1 == "ate":
            verb1used = random.choice(verbused_ate)
            verb1ext = random.choice(extension_ate)
        elif chosenroot1 == "travel":
            verb1used = random.choice(verbused_travel)
            verb1ext = random.choice(extension_travel)
        elif chosenroot1 == "moved":
            verb1used = random.choice(verbused_moved)
            verb1ext = random.choice(extension_moved)
        elif chosenroot1 == "listened":
            verb1used = random.choice(verbused_listened)
            verb1ext = random.choice(music)
        elif chosenroot1 == "played":
            verb1used = random.choice(verbused_played)
            verb1ext = random.choice(music)+" "+random.choice(extension_played)
        else:
            verb1used = "broke"
            verb1ext = random.choice(["reality", "existence", "everything"])

        chosenroot2 = random.choice(verbs)
        if chosenroot2 == "said":
            verb2used = random.choice(verbused_said)
            verb2ext = ('"' + random.choice(extension_said) + '"')
        elif chosenroot2 == "ate":
            verb2used = random.choice(verbused_ate)
            verb2ext = random.choice(extension_ate)
        elif chosenroot2 == "travel":
            verb2used = random.choice(verbused_travel)
            verb2ext = random.choice(extension_travel)
        elif chosenroot2 == "moved":
            verb2used = random.choice(verbused_moved)
            verb2ext = random.choice(extension_moved)
        elif chosenroot2 == "listened":
            verb2used = random.choice(verbused_listened)
            verb2ext = random.choice(music)
        elif chosenroot2 == "played":
            verb2used = random.choice(verbused_played)
            verb2ext = random.choice(music)+" "+random.choice(extension_played)
        else:
            verb2used = "broke"
            verb2ext = random.choice(["reality", "existence", "everything"])

        if chosenroot1 == chosenroot2:
            verb2used = ("also " + verb2used)


        finalverb1 = (verb1used + " " + verb1ext)
        finalverb2 = (verb2used + " " + verb2ext)

        if chosensentencestr == "generic":
            finalmsg = chosennoun1 + " " + finalverb1 + " and " + chosennoun2 + " " + finalverb2 + "."
        elif chosensentencestr == "if":
            finalmsg = "if " + chosennoun1 + " hadn't " + finalverb1 + ", would " + chosennoun2 + " still have " + finalverb2 + "?"
        elif chosensentencestr == "hadthe":
            finalmsg = chosennoun1 + " wouldn't have " + finalverb1 + " had the " + chosennoun2 + " not " + finalverb2 + "."
        elif chosensentencestr == "as":
            finalmsg = chosennoun1 + " " + finalverb1 + " as " + chosennoun2 + " " + finalverb2 + "."
        elif chosensentencestr == "wouldvebut":
            finalmsg = chosennoun1 + " would've " + finalverb1 + ", but " + chosennoun2 + " " + finalverb2 + "."
        else:
            finalmsg = "This response hasn't been programmed yet, just testing"
        
        await interaction.response.send_message(finalmsg[0].upper()+finalmsg[1:len(finalmsg)])

@app_commands.checks.cooldown(1, 60, key=lambda i: (i.user.id))
@tree.command(name="pet", description="Pet the Leez-rd")
async def test(interaction: discord.Interaction):
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
        filemake = {}
        with open(path, 'w') as f:
            f.write(str(filemake))
        f.close()
            
    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)
    if "pets" in caughtdict.keys():
        caughtdict["pets"] = int(caughtdict["pets"]) + 1
    else:
        caughtdict["pets"] = 1
    
    if caughtdict["pets"] == 50:
        caughtdict["hand"] = 1
  
    with open(path, 'w') as convert_file:
        convert_file.write(json.dumps(caughtdict))
    print(caughtdict)
    f.close()

    f = open("pet.txt","r+")
    f.seek(0)
    pettrans = f.readline()
    petamt=int(pettrans)+1
    f.close()
    f = open("pet.txt", "w+")
    f.write(str(petamt))
    f.close()
    print(interaction.user.name+" petted. New pet value " + str(petamt))
    if petamt >= 200:
        petmsg = "you give the leez-rd lots of headpats"
    elif petamt >= 100:
        petmsg = "you give the leez-rd some headrubs"
    elif petamt >= 50:
        petmsg = "you boop the leez-rd"
    elif petamt >= 20:
        petmsg = "you stroke the leez-rd"
    else:
        petmsg = "you pet the leez-rd"
    if caughtdict["pets"] == 50:
        await interaction.response.send_message(":leftwards_hand: " + petmsg + "...\n`You have now petted the Leez-rd 50 times by yourself. It eagerly seeks your touch.`\nYou got the **Petting Hand**. </trophies:1069668767044472912>")
    elif petamt >= 100:
        if caughtdict["pets"] >= 50:
            await interaction.response.send_message(":leftwards_hand: " + petmsg + "...\n<:goldleezrd:1065661627178946651> the leez-rd has been pet **" + str(petamt) + "** times!")
        else:
            await interaction.response.send_message(":relieved: " + petmsg + "...\n<:goldleezrd:1065661627178946651> the leez-rd has been pet **" + str(petamt) + "** times!")
        if petamt == 100:
            await interaction.response.send_message(":sparkles: **the leez-rd has turned gold from all of the pets!**")
    else:
        if caughtdict["pets"] >= 50:
            await interaction.response.send_message(":leftwards_hand: " + petmsg + "...\n<:leezrd:831177020108963890> the leez-rd has been pet **" + str(petamt) + "** times!")
        else:
            await interaction.response.send_message(":relieved: " + petmsg + "...\n<:leezrd:831177020108963890> the leez-rd has been pet **" + str(petamt) + "** times!")

@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        print(error.cooldown)
        await interaction.response.send_message("You're on cooldown! Try again later.", ephemeral=True)

@app_commands.checks.cooldown(1, 3, key=lambda i: (i.user.id))
@tree.command(name="catch", description="Catch a character from the Leez-rd Realm!")
@app_commands.describe(item="The item to use when catching, if any.")
async def test(interaction: discord.Interaction, item: Optional[str]):
    unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")
    getitem = 0

    if item is None:
        useditem = "none"
    else:
        useditem = item

    if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)
    if not "next" in caughtdict.keys():
        caughtdict["next"] = unix
    
    if caughtdict["next"] <= unix:
        print(interaction.user.name+" caught")

        itemweight = random.choice(range(1,3))
        if itemweight == 1:
            getitem = 1
            item = random.choice(items)

        if not "guaranteedCreature" in caughtdict.keys():
            print("determined no guarantee")
            caughtdict["guaranteedCreature"] = "none"
            print("determined creature")
            
        if caughtdict["guaranteedCreature"] == "steak":
            print("guarantee identified as steak")
            caught = str(random.choice(["leez", "albino", "residue"]))
            print("determined creature")
        
        elif caughtdict["guaranteedCreature"] == "strange":
            print("guarantee identified as strange")
            caught = str(random.choice(["bert", "jack", "ad"]))
            print("determined creature")
        
        elif caughtdict["guaranteedCreature"] == "beans":
            print("guarantee identified as beans")
            caught = str(random.choice(["beth", "bryan", "carcassite"]))
            print("determined creature")
        
        elif caughtdict["guaranteedCreature"] == "stew":
            print("guarantee identified as stew")
            caught = str(random.choice(rares))
            print("determined creature")
        
        elif caughtdict["guaranteedCreature"] == "shard":
            print("guarantee identified as shard soup")
            caught = str(random.choice(["redprismalgam", "greenprismalgam", "blueprismalgam", "redprismalgam", "greenprismalgam", "blueprismalgam", "blackprismalgam"]))
            print("determined creature")

        elif "prism" in caughtdict.keys() and not caughtdict["prism"] == "none":
            print("recognised prism is in effect")
            if caughtdict["prism"] == "red":
                rarityweight = random.choice(range(1,10))
                if rarityweight > 8:
                    rarity = ["adamantprismalgam"]
                elif rarityweight >= 6:
                    rarity = ["redprismalgam"]
                else:
                    rarity = ["bryan", "carcassite"]
                caught = str(random.choice(rarity))

                print("a")

                if itemweight == 1:
                    getitem = 1
                    item = random.choice(["paintbrush", "label"])

                print("a")
            
            elif caughtdict["prism"] == "green":
                rarityweight = random.choice(range(1,10))
                if rarityweight > 8:
                    rarity = ["dazzlingprismalgam"]
                elif rarityweight >= 6:
                    rarity = ["greenprismalgam"]
                else:
                    rarity = ["leez", "albino"]
                caught = str(random.choice(rarity))

                if itemweight == 1:
                    getitem = 1
                    item = random.choice(["steak", "beans"])

            elif caughtdict["prism"] == "blue":
                rarityweight = random.choice([9])
                if rarityweight > 8:
                    rarity = ["iridescentprismalgam"]
                elif rarityweight >= 6:
                    rarity = ["blueprismalgam"]
                else:
                    rarity = ["beth", "residue"]
                caught = str(random.choice(rarity))

                if itemweight == 1:
                    getitem = 1
                    item = random.choice(["stopwatch", "compass"])
            
            elif caughtdict["prism"] == "black":
                rarityweight = random.choice(range(1,10))
                if rarityweight > 8:
                    rarity = ["mythicprismalgam"]
                elif rarityweight >= 6:
                    rarity = ["redprismalgam", "greenprismalgam", "blueprismalgam", "blackprismalgam"]
                else:
                    rarity = ["bryan", "leez", "beth"]
                caught = str(random.choice(rarity))

                if itemweight == 1:
                    getitem = 1
                    item = random.choice(["contract", "stew"])
        
        else:
            rarityweight = random.choice(range(1,10))
            print("weight "+str(rarityweight))
            if rarityweight > 8:
                rarity = list(rares)
            elif rarityweight >= 6:
                rarity = list(uncommons)
            else:
                rarity = list(commons)
            caught = str(random.choice(rarity))

        print("a")
        
        caughtdict["guaranteedCreature"] = "none"
        print("b")
        if useditem == "cherry" and "cherry" in caughtdict.keys():
            caughtdict["cherry"] = caughtdict["cherry"] - 1
            caughtamount = 2
            print("detected cherry")
        else:
            caughtamount = 1
            print("detected no cherry")


        if "embedR" in caughtdict.keys():
            embed = discord.Embed(title="You "+random.choice(catchmsgs)+" "+creaturedata[caught]["an"]+creaturedata[caught]["name"]+"!", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
        else:
            embed = discord.Embed(title="You "+random.choice(catchmsgs)+" "+creaturedata[caught]["an"]+creaturedata[caught]["name"]+"!", color=discord.Color.from_rgb(creaturedata[caught]["colour"]["red"], creaturedata[caught]["colour"]["green"], creaturedata[caught]["colour"]["blue"]))

        print("c")

        embed.set_thumbnail(url=creaturedata[caught]["catchicon"])
        if not caught in caughtdict.keys():
            embed.add_field(name=" ", value="That's a new one!", inline=False)
        
        embed.add_field(name=" ", value="`"+creaturedata[caught]["desc"]+"`", inline=False)
        
        if not caught in caughtdict.keys():
            embed.add_field(name=" ", value="The shortform/id for this creature is `"+creaturedata[caught]["id"]+"`.")

        if getitem == 1:
            if item in caughtdict.keys():
                embed.add_field(name=" ", value="Oh? It was holding "+itemdata[item]["an"]+"**"+itemdata[item]["name"]+"**!"+itemdata[item]["emoji"], inline=False)
            else:
                embed.add_field(name=" ", value="Oh? It was holding "+itemdata[item]["an"]+"**"+itemdata[item]["name"]+"**!"+itemdata[item]["emoji"]+"\nYou can view this with </items:1069358150517526538>.", inline=False)

        if getitem == 1:
            if item in caughtdict.keys():
                caughtdict[item] = int(caughtdict[item]) + 1
            else:
                caughtdict[item] = 1
        
        print("Updated item amount")

        if caught in caughtdict.keys():
            caughtdict[caught] = caughtdict[caught] + caughtamount
        else:
            caughtdict[caught] = caughtamount

        print("Updated creature amount")

        if "rexlevel" in caughtdict.keys() and caughtdict["rexlevel"] == 3:
            caughtdict["next"] = unix + 2700
        else:
            caughtdict["next"] = unix + 3600
  
        with open(path, 'w') as convert_file:
            convert_file.write(json.dumps(caughtdict))
        print(caughtdict)
        f.close()

        embed.set_footer(text="You now have "+str(caughtdict[caught])+" of this creature.")

        await interaction.response.send_message(embed=embed)

    else:
        print(interaction.user.name+"'s cooldown prevented catch")
        await interaction.response.send_message("You're on cooldown! Try again <t:"+str(caughtdict["next"])+":R>.", ephemeral=True)

@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message("Woah! Slow down there.", ephemeral=True)

@tree.command(name="creatures", description="Lists all creatures you've caught with /catch.")
@app_commands.describe(user= "The id of the user to list.")
async def test(interaction: discord.Interaction, user: Optional[discord.Member]):
    if user is None:
        useridused = str(interaction.user.id)
    else:
        useridused = str(user.id)
    
    caughttotal = 0
    registered = 0
    path = Path("./"+useridused+".txt")

    if not (path).is_file():
        await interaction.response.send_message(random.choice(nofile), ephemeral=True)

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)

    if "nickname" in caughtdict.keys():
        listtitle = caughtdict["nickname"]+"'s Creatures"
    else:
        listtitle = interaction.user.name+"'s Creatures"
    
    if "embedR" in caughtdict.keys():
        embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
    else:
        embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(125, 230, 100))

    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
        await interaction.response.send_message("You have no creatures! Use </catch:1066140364953632809> to catch a creature.", ephemeral=False)
    else:

        for item in creaturedata.keys():
            if item in caughtdict.keys() and caughtdict[item] > 0:
                embed.add_field(name=creaturedata[item]["emoji"]+creaturedata[item]["name"]+" `"+creaturedata[item]["id"]+"`", value=str(caughtdict[item])+" owned", inline=False)
                caughttotal = caughttotal + int(caughtdict[item])
                registered = registered + 1

        embed.set_footer(text="Use creature ids (keywords next to creature names) for commands needing creatures.\nYou have a total of "+str(caughttotal)+" creatures.\n"+str(registered)+"/"+str(len(creaturedata.keys()))+" species in collection")

        if registered == len(creaturedata.keys()) and not "compendium" in caughtdict.keys():
            caughtdict["compendium"] = 1

            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
            f.close()
            await interaction.response.send_message("**You have obtained every creature!**\nYou made this :notebook_with_decorative_cover: **Compendium**. </trophies:1069668767044472912>")
        
        elif caughttotal >= 100 and not "legacy" in caughtdict.keys():
            caughtdict["legacy"] = 1
  
            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
            f.close()
            await interaction.response.send_message("**You have amassed a total of 100 creatures!**\nYour :dizzy: **Legacy** has now materialised! </trophies:1069668767044472912>")
        else:
            await interaction.response.send_message(embed=embed)

@tree.command(name="items", description="Lists all the items you've obtained from /catch.")
@app_commands.describe(item='The name of a specific item to view in detail.')
async def test(interaction: discord.Interaction, item: Optional[str]):
    itemstotal = 0
    registered = 0
    path = Path("./"+str(interaction.user.id)+".txt")

    if not (path).is_file():
        await interaction.response.send_message(random.choice(nofile), ephemeral=True)
    
    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)

    if not item is None:
        if item in caughtdict.keys() and caughtdict[item] > 0:
            itemname = itemdata[item]["name"]
            listtitle = itemdata[item]["emoji"]+" "+itemname[0].upper()+itemname[1:len(itemname)].lower()

            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(255, 175, 95))
            
            embed.add_field(name="", value="**"+itemdata[item]["desc"]+"**")

            embed.set_footer(text="yell at me if i don't add item usage tmr")

            await interaction.response.send_message(embed=embed)

        else:

            await interaction.response.send_message(random.choice(noitems), ephemeral=True)

    else:

        if "nickname" in caughtdict.keys():
            listtitle = caughtdict["nickname"]+"'s Items"
        else:
            listtitle = interaction.user.name+"'s Items"

        if "embedR" in caughtdict.keys():
            embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
        else:
            embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(255, 175, 95))


        for item in itemdata.keys():
            if item in caughtdict.keys() and caughtdict[item] > 0:
                embed.add_field(name=itemdata[item]["emoji"]+itemdata[item]["name"]+" `"+itemdata[item]["id"]+"`", value=str(caughtdict[item])+" owned", inline=False)
                itemstotal = itemstotal + int(caughtdict[item])
                registered = registered + 1

        embed.set_footer(text="Use item ids (keywords next to item names) for commands requiring items.\nYou have a total of "+str(itemstotal)+" items.\n"+str(registered)+"/"+str(len(itemdata.keys()))+" unique items owned")
    
        await interaction.response.send_message(embed=embed)


@tree.command(name="colour", description="Change your embed colour to any RGB colour code! Use hex to rgb for hex. Requires a paintbrush.")
@app_commands.describe(red='The first 3 (red) digits')
@app_commands.describe(green='The middle 3 (green) digits')
@app_commands.describe(blue='The last 3 (blue) digits')
async def test(interaction: discord.Interaction, red: int, green: int, blue: int):
    userid = str(interaction.user.id)
    userfile = str(userid+".txt")
    path = Path("./"+userid+".txt")
    with open(path) as f:
        data = f.read()
    f.close()

    caughtdict = ast.literal_eval(data)
    if "paintbrush" in caughtdict.keys():
        if caughtdict["paintbrush"] == 0:
            await interaction.response.send_message(random.choice(noitems), ephemeral=True)
        else:

            # clamping to 255 and 0
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0

            caughtdict["embedR"] = red
            caughtdict["embedG"] = green
            caughtdict["embedB"] = blue
            caughtdict["paintbrush"] = caughtdict["paintbrush"] - 1
            with open(userfile, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
            f.close()
            await interaction.response.send_message("Set embed colour to "+str(red)+" red, "+str(green)+" green and "+str(blue)+" blue!\n:paintbrush: Your **paintbrush** was used up...")
    else:
        await interaction.response.send_message(random.choice(noitems), ephemeral=True)

@tree.command(name="use", description="Use an item.")
@app_commands.describe(item='The id of the item.')
async def test(interaction: discord.Interaction, item: str):
    userid = str(interaction.user.id)
    userfile = str(userid+".txt")
    unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
    path = Path("./"+userid+".txt")

    if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)
    if item in caughtdict.keys():
        if item in creaturedata.keys():
            await interaction.response.send_message(random.choice(itembutcreature), ephemeral=True)

        elif item in unusableitems:
            await interaction.response.send_message("This item is unusable in this way!\nUse </item:1069397752192188546> `"+item+"` to view the command that requires this item.", ephemeral=True)

        elif caughtdict[item] > 0 and item in itemdata.keys():
            if item == "stopwatch":
                if caughtdict["next"] <= unix:
                    await interaction.response.send_message("You don't have an active cooldown right now! Best save this for when you do.", ephemeral=True)
                elif caughtdict["next"] <= unix + 120:
                    caughtdict["next"] = unix
                    caughtdict["stopwatch"] = caughtdict["stopwatch"] -1
                    if "waste" in caughtdict.keys():
                        already = 1
                    else:
                        already = 0
                        caughtdict["waste"] = 1

                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()

                    if already == 1:
                        await interaction.response.send_message(":wastebasket: Congratulations, again, for wasting *another* stopwatch!")
                    else:
                        await interaction.response.send_message(":wastebasket: Why??? Why did you use a stopwatch?? You just had to wait sixty seconds. SIXTY. SECONDS.\nTake this **waste basket**... to put all that wasted time in. </trophies:1069668767044472912>")
                else:
                    caughtdict["next"] = caughtdict["next"] - 1800
                    caughtdict["stopwatch"] = caughtdict["stopwatch"] -1
                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    if caughtdict["next"] <= unix:
                        await interaction.response.send_message("You used your :stopwatch: **Stopwatch**! You can catch again **right now**!")
                    else:
                        await interaction.response.send_message("You used your :stopwatch: **Stopwatch**! You can catch again <t:"+str(caughtdict["next"])+":R>.")

            elif item == "compass":
                if not "questend" in caughtdict.keys():
                    await interaction.response.send_message("You've never started a quest?? And you want to use a compass??", ephemeral=True)
                elif caughtdict["questend"] <= unix:
                    await interaction.response.send_message("You don't need to remove time from your quest right now! Best save this for when you do.", ephemeral=True)
                elif caughtdict["questend"] <= unix + 360:
                    caughtdict["questend"] = unix
                    caughtdict["compass"] = caughtdict["compass"] -1
                    caughtdict["waste"] = 1

                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()

                    if "waste" in caughtdict:
                        await interaction.response.send_message(":wastebasket: *Congratulations, again, for wasting a compass!*")
                    else:
                        await interaction.response.send_message(":wastebasket: Why??? Why did you use a compass?? You just had to wait ten minutes. TEN. MINUTES.\nTake this **waste basket**... to put all that wasted time in. </trophies:1069668767044472912>")
                else:
                    caughtdict["questend"] = caughtdict["questend"] - 10800
                    caughtdict["compass"] = caughtdict["compass"] -1
                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    if caughtdict["questend"] <= unix:
                        await interaction.response.send_message("You used your :compass: **Compass**! **Your quest has now finished**!")
                    else:
                        await interaction.response.send_message("You used your :compass: **Compass**! Your quest will now finish <t:"+str(caughtdict["questend"])+":R>.")
            
            elif item == "steak":
                if not caughtdict["guaranteedCreature"] == "none":
                    await interaction.response.send_message("You already have a creature type guaranteed! Better save this for later...", ephemeral=True)
                else:
                    caughtdict["guaranteedCreature"] = "steak"
                    caughtdict["steak"] = caughtdict["steak"] -1
                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    await interaction.response.send_message("You used your :cut_of_meat: **Steak**! Your next rescue will be a **Leez-rd species**.")
            
            elif item == "beans":
                if not caughtdict["guaranteedCreature"] == "none":
                    await interaction.response.send_message("You already have a creature type guaranteed! Better save this for later...", ephemeral=True)
                else:
                    caughtdict["guaranteedCreature"] = "beans"
                    caughtdict["beans"] = caughtdict["beans"] -1
                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    await interaction.response.send_message("You used your :beans: **Beans**! Your next rescue will be a **Beth species**.")
            
            elif item == "stew":
                if not caughtdict["guaranteedCreature"] == "none":
                    await interaction.response.send_message("You already have a creature type guaranteed! Better save this for later...", ephemeral=True)
                else:
                    caughtdict["guaranteedCreature"] = "stew"
                    caughtdict["stew"] = caughtdict["stew"] -1
                    with open(userfile, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    await interaction.response.send_message("You used your :stew: **Stew**! Your next rescue will be a **rare creature**.")
            
        else:
            await interaction.response.send_message(random.choice(noitems), ephemeral=True)

    else:
        await interaction.response.send_message(random.choice(noitems), ephemeral=True)

@tree.command(name="trophies", description="View your trophies!")
async def test(interaction: discord.Interaction):
    userid = str(interaction.user.id)
    userfile = str(userid+".txt")
    unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
    path = Path("./"+userid+".txt")

    if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

    with open(path) as f:
        data = f.read()
    f.close()

    caughtdict = ast.literal_eval(data)
    if "nickname" in caughtdict.keys():
        listtitle = caughtdict["nickname"]+"'s Trophies"
    else:
        listtitle = interaction.user.name+"'s Trophies"
    if "bug" in caughtdict.keys() or "hand" in caughtdict.keys() or "legacy" in caughtdict.keys() or "duck" in caughtdict.keys() or "pillar" in caughtdict.keys():
        if "embedR" in caughtdict.keys():
            embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
        else:
            embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(250, 190, 0))
        if "duck" in caughtdict.keys():
            embed.add_field(name=f":duck: Duck", value="`/trophy duck`", inline=False)
        if "pillar" in caughtdict.keys():
            embed.add_field(name=f":bug: The Pillar", value="`/trophy pillar`", inline=False)
        if "cake" in caughtdict.keys():
            embed.add_field(name=f":birthday: Cake", value="`/trophy cake`", inline=False)
        if "cakiercake" in caughtdict.keys():
            embed.add_field(name=f":cupcake: Cakier Cake", value="`/trophy cakiercake`", inline=False)
        if "lucky" in caughtdict.keys():
            embed.add_field(name=f":sparkles: Lucky", value="`/trophy lucky`", inline=False)
        if "luckier" in caughtdict.keys():
            embed.add_field(name=f"<:lucky2:1071193862749569086> Luckier", value="`/trophy luckier`", inline=False)
        if "first" in caughtdict.keys():
            embed.add_field(name=f":first_place: First", value="`/trophy first`", inline=True)
        if "contributor" in caughtdict.keys():
            embed.add_field(name=f":star2: Contributor", value="`/trophy contributor`", inline=True)
        if "bug" in caughtdict.keys():
            embed.add_field(name=f":beetle: An Actual Bug", value="`/trophy bug`", inline=False)
        if "hand" in caughtdict.keys():
            embed.add_field(name=f":leftwards_hand: The Petting Hand", value="`/trophy hand`", inline=False)
        if "waste" in caughtdict.keys():
            embed.add_field(name=f":wastebasket: Waste (of time)", value="`/trophy waste`", inline=False)
        if "legacy" in caughtdict.keys():
            embed.add_field(name=f":dizzy: Legacy", value="`/trophy legacy`", inline=False)
        if "compendium" in caughtdict.keys():
            embed.add_field(name=f":notebook_with_decorative_cover: Compendium", value="`/trophy compendium`", inline=False)
        if "bertmedal" in caughtdict.keys():
            embed.add_field(name=f"<:bert:1079448808729104485> Bert Medal", value="`/trophy bertmedal`", inline=False)
        embed.set_footer(text="View the details of a trophy with /trophy.")
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("You don't have any trophies! Obtain trophies by doing notable things.", ephemeral=True)

@tree.command(name="trophy", description="Provides info on a trophy you have.")
@app_commands.describe(trophy='The id of the trophy.')
async def test(interaction: discord.Interaction, trophy: str):
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)

    if trophy in trophies:
        if trophy not in caughtdict.keys():
            await interaction.response.send_message("Imagine not having this trophy", ephemeral=True)
        else:
            if trophy == "bug":
                if "bug" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":beetle: An Actual Bug", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":beetle: An Actual Bug", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`After finding a bug in Lee-rd Bot it materialised as An Actual Bug. Obtained by reporting a valid bug in Leez-rd Bot.`", inline=True)
                    embed.set_footer(text=" ̶G̶a̶m̶e̶ ̶B̶r̶e̶a̶k̶e̶r̶")
                    await interaction.response.send_message(embed=embed)

            elif trophy == "hand":
                if "hand" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":leftwards_hand: The Petting Hand", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":leftwards_hand: The Petting Hand", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"", value="`The Leez-rd has learnt to eagerly await this hand's touch. Obtained by singlehandedly petting the Leez-rd 50 times.`", inline=True)
                    embed.set_footer(text="This trophy will display a hand emoji while petting.")
                    await interaction.response.send_message(embed=embed)

            elif trophy == "duck":
                if "duck" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":duck: Duck", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":duck: Duck", color=discord.Color.from_rgb(0, 106, 160))

                    embed.add_field(name=f"", value="`A very ducky duck. The duckness intensifies.`", inline=True)
                    embed.set_footer(text="Duck")
                    await interaction.response.send_message(embed=embed)
    
            elif trophy == "first":
                if "first" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":first_place: First", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":first_place: First", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"", value="`You are one of the first. Given to the first 5 people who used /catch.`", inline=True)
                    embed.set_footer(text="fomo")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "contributor":
                if "contributor" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":star2: Contributor", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":star2: Contributor", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"", value="You contributed something that made it into Leez-rd Bot!", inline=True)
                    embed.set_footer(text="Thank you!")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "compendium":
                if "compendium" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":notebook_with_decorative_cover: Compendium", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":notebook_with_decorative_cover: Compendium", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"", value="A notebook with many scribblings inside. You obtained one of every creature!", inline=True)
                    embed.set_footer(text="now for true 100%")
                    await interaction.response.send_message(embed=embed)

            elif trophy == "pillar":
                if "pillar" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":bug: The Pillar", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":bug: The Pillar", color=discord.Color.from_rgb(128, 128, 128))

                    embed.add_field(name=f"",value="`The ultimate insect, a friend of the Legend.`", inline=True)
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "lucky":
                if "lucky" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":sparkles: Lucky", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":sparkles: Lucky", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`You were just plain lucky.\nFind a shiny Leez-rd through /shinyroll.`", inline=True)
                    embed.set_footer(text="this is a flex.")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "luckier":
                if "luckier" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title="<:lucky2:1071193862749569086> Luckier", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title="<:lucky2:1071193862749569086> Luckier", color=discord.Color.from_rgb(50, 220, 255))

                    embed.add_field(name=f"",value="*Somehow*, you found *two* shiny Leez-rds from /shinyroll. The odds of that happening, let's just say, are not in your favour.", inline=True)
                    embed.set_footer(text="now THIS is a flex alright!")
                    await interaction.response.send_message(embed=embed)

            elif trophy == "legacy":
                if "legacy" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":dizzy: Legacy", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":dizzy: Legacy", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`Through catching so many creatures, your legacy has fully formed itself. Obtained by amassing a total of 100 creatures or more.`", inline=True)
                    embed.set_footer(text="")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "waste":
                if "waste" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":wastebasket: Waste (of time)", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":wastebasket: Waste (of time)", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`You essentially wasted free time (and an item). Here's a waste basket to put it in.`", inline=True)
                    embed.set_footer(text="Now just don't do it again...")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "bertmedal":
                if "bertmedal" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title="<:bert:1079448808729104485> Bert Medal", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title="<:bert:1079448808729104485> Bert Medal", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`A true Bert enthusiast, you acquired every form of Bert!`", inline=True)
                    embed.set_footer(text="Bert-tastic!")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "cake":
                if "cake" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":birthday: Cake", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":birthday: Cake", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`A spectacular cake to celebrate one's birthday. This one has "+str(caughtdict["cake"])+" candles on top to celebrate someone's big day!`", inline=True)
                    embed.set_footer(text="Here's to another year!")
                    await interaction.response.send_message(embed=embed)
            
            elif trophy == "cakiercake":
                if "cakiercake" in caughtdict.keys():
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title=":cupcake: Cakier Cake", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title=":cupcake: Cakier Cake", color=discord.Color.from_rgb(250, 190, 0))

                    embed.add_field(name=f"",value="`A second, more impressive cake with "+str(caughtdict["cakier"])+" candles atop to celebrate another big day!`", inline=True)
                    embed.set_footer(text="How can it be more impressive if it's smaller ...?")
                    await interaction.response.send_message(embed=embed)

    else:
        await interaction.response.send_message("This trophy doesn't exist!", ephemeral=True)

@tree.command(name = "help", description = "Get a list of all Leez-rd Bot commands and what they do!")
async def self(interaction: discord.Interaction):
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)

    with open("ver.txt") as f:
        data = f.read()
        f.close()

    ver = ast.literal_eval(data)

    if "embedR" in caughtdict.keys():
        embed = discord.Embed(title="Command Help", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
    else:
        embed = discord.Embed(title="Command Help", color=discord.Color.from_rgb(150, 215, 230))
    embed.add_field(name=f"</ping:1064942125059412048>", value="I wonder... maybe this pings the bot?", inline=False)
    embed.add_field(name=f"</pet:1065642903990448218>", value="Pet the Leez-rd. Gets more stimulated the more you pet it.", inline=False)
    embed.add_field(name=f"</bcbs:1064983733809192970>", value="Bread Crumbs and Beaver Spit. Generates a random(ish) sentence. An intricate remake of my first Discord CC!", inline=False)
    embed.add_field(name=f"</shinyroll:1064942125059412049>", value="Roll for a shiny Leez-rd. You get a special trophy if you find one!", inline=False)
    embed.add_field(name=f"</catch:1066140364953632809>", value="Catch a character from the Leez-rd Realm!", inline=False)
    embed.add_field(name=f"</items:1069358150517526538>", value="List your items, or view info on one item.", inline=False)
    embed.add_field(name=f"</use:1069664666667729007>", value="Use an item.", inline=False)
    embed.add_field(name=f"</trophies:1069668767044472912> / </trophy:1069670672839757834>", value="View your trophies, or view info on a trophy.", inline=False)
    embed.add_field(name=f"</release:1070060426303381625>", value="Release a creature and get some shards back for it.", inline=False)
    embed.add_field(name=f"</prismify:1070042228019437769>", value="Combine 2 shards to conjure a creature into being!", inline=False)
    embed.add_field(name=f"</startquest:1071183083467968633> / </claimquest:1071192626700755045> / </cancelquest:1072259932805681202>", value="Send creatures on quests for rewards! Every creature brings different rewards.", inline=False)
    embed.add_field(name=f"</questinfo:1071531414476042342>", value="View info on a creature's unique rewards", inline=False)
    embed.add_field(name=f"</craft:1071840430934736926>", value="View current crafting recipes, or craft something.", inline=False)
    embed.add_field(name=f"</rex:1072962869903249571>", value="View progress awakening Rex Anomaliae, or feed it.", inline=False)
    embed.add_field(name=f"</terminal:1076990886354890762>", value="Run a command in the mysterious terminal. Requires awakening Rex Anomaliae.", inline=False)
    embed.add_field(name="", value=" \n\nCurrently running v"+ver["ver"]+", last updated\n<t:"+str(ver["time"])+":R>.", inline=False)

    await interaction.response.send_message(embed=embed)

@tree.command(name="nick", description="Change the nickname the bot uses for you. Requires a label.")
@app_commands.describe(name='The name')
async def test(interaction: discord.Interaction, name: str):
    userid = str(interaction.user.id)
    userfile = str(userid+".txt")
    path = Path("./"+userid+".txt")
    with open(path) as f:
        data = f.read()
    f.close()

    caughtdict = ast.literal_eval(data)
    if "label" in caughtdict.keys():
        if caughtdict["label"] == 0:
            await interaction.response.send_message(random.choice(noitems), ephemeral=True)
        else:
            if not (name.lower() in funNicks and funNicks[name.lower()]["allowed"] is False):
                caughtdict["nickname"] = name
                caughtdict["label"] = caughtdict["label"] - 1
            with open(userfile, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
            f.close()
            if name.lower() in funNicks:
                if funNicks[name.lower()]["allowed"] is True:
                    await interaction.response.send_message("*"+funNicks[name.lower()]["msg"]+"*\n:label: Your **label** was used up...")
                else:
                    await interaction.response.send_message("*"+funNicks[name.lower()]["msg"]+"*\n:label: Your **label** was not consumed.")
            else:
                await interaction.response.send_message("I will now call you **"+name+"**!\n:label: Your **label** was used up...")
    else:
        await interaction.response.send_message(random.choice(noitems), ephemeral=True)

@tree.command(name="prismify", description="Conjure a creature into the Leez-rd Realm through the power of prismification. Requies two shards.")
@app_commands.describe(base='The first and more important shard.')
@app_commands.describe(shard='The second shard')
async def test(interaction: discord.Interaction, base: str, shard: str):
    userid = str(interaction.user.id)
    userfile = str(userid+".txt")
    path = Path("./"+userid+".txt")
    with open(path) as f:
        data = f.read()
    f.close()

    # red/green/blue/black are aliases

    if base in ["red", "green", "blue", "black"]:
        base = base+"shard"
    if shard in ["red", "green", "blue", "black"]:
        shard = shard+"shard"

    print(base+" and "+shard)

    caughtdict = ast.literal_eval(data)
    if base in caughtdict.keys() and shard in caughtdict.keys():
        if base == shard and caughtdict[base] == 1:
            await interaction.response.send_message(random.choice(noitems), ephemeral=True)
        elif caughtdict[base] + caughtdict[shard] > 1:
            if not base in shards_black or not shard in shards_black:
                await interaction.response.send_message("You have to use a shard item! Obtain shards from releasing creatures or as quest rewards.", ephemeral=True)
            elif base == "redshard":
                if shard == "redshard":
                    shardpick = ["redprismalgam"]
                    shardpick.extend(reds)
                else:
                    shardpick = reds
                    if shard == "greenshard":
                        shardpick.extend(greens)
                    if shard == "blueshard":
                        shardpick.extend(blues)
                    if shard == "blackshard":
                        shardpick.extend(blacks)
            elif base == "greenshard":
                if shard == "greenshard":
                    shardpick = ["greenprismalgam"]
                    shardpick.extend(greens)
                else:
                    shardpick = greens
                    if shard == "redshard":
                        shardpick.extend(reds)
                    if shard == "blueshard":
                        shardpick.extend(blues)
                    if shard == "blackshard":
                        shardpick.extend(blacks)
            elif base == "blueshard":
                if shard == "blueshard":
                    shardpick = ["blueprismalgam"]
                    shardpick.extend(blues)
                else:
                    shardpick = blues
                    if shard == "redshard":
                        shardpick.extend(reds)
                    if shard == "greenshard":
                        shardpick.extend(greens)
                    if shard == "blackshard":
                        shardpick.extend(blacks)
            elif base == "blackshard":
                if shard == "blackshard":
                    shardpick = ["redprismalgam", "greenprismalgam", "blueprismalgam", "blackprismalgam"]
                    shardpick.extend(blacks)
                else:
                    shardpick = blacks
                    if shard == "redshard":
                        shardpick.extend(reds)
                    if shard == "greenshard":
                        shardpick.extend(greens)
                    if shard == "blueshard":
                        shardpick.extend(blues)
            shardresult = random.choice(shardpick)
            caughtdict[base] = caughtdict[base] - 1
            caughtdict[shard] = caughtdict[shard] - 1
            if shardresult in caughtdict.keys():
                caughtdict[shardresult] = int(caughtdict[shardresult]) + 1
            else:
                caughtdict[shardresult] = 1
            with open(userfile, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
            f.close()
            resultemoji = creaturedata[shardresult]["emoji"]
            resultname = creaturedata[shardresult]["an"] + creaturedata[shardresult]["name"]

            baseemoji = itemdata[base]["emoji"]
            shardemoji = itemdata[shard]["emoji"]
            print(shardpick)

            await interaction.response.send_message(resultemoji+" You prismified **"+resultname+"**! Congratulations!\n"+baseemoji+shardemoji+"Your shards got used up.")
        else:
            await interaction.response.send_message(random.choice(noitems), ephemeral=True)
    else:
        await interaction.response.send_message(random.choice(noitems), ephemeral=True)

@tree.command(name="release", description="Release a creature back into the Leez-rd Realm. Rewards you with coloured shards.")
@app_commands.describe(creature='The creature being released')
async def test(interaction: discord.Interaction, creature: str):
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)
    if creature in caughtdict.keys() and creature in itemdata.keys():
        await interaction.response.send_message(random.choice(creaturebutitem), ephemeral=True)

    if creature in caughtdict.keys() and caughtdict[creature] > 0:
        resultname = creaturedata[creature]["an"] + creaturedata[creature]["name"]
        if creature == "redprismalgam" or creature == "greenprismalgam" or creature == "blueprismalgam":
            shardamt = 2
        elif creature == "poopyshoes" or creature == "albino":
            shardamt = random.choice(range(2, catchshardamts[creature]+1))
        else:
            shardamt = random.choice(range(1, catchshardamts[creature]+1))

        if shardamt == 4:
            guaranshard1 = catchguaranshards[creature]
            randomshard1 = random.choice(shards)
            randomshard2 = random.choice(shards)
            if guaranshard1 in caughtdict.keys():
                caughtdict[guaranshard1] = int(caughtdict[guaranshard1]) + 2
            else:
                caughtdict[guaranshard1] = 2
            if randomshard1 in caughtdict.keys():
                caughtdict[randomshard1] = int(caughtdict[randomshard1]) + 1
            else:
                caughtdict[randomshard1] = 1
            if randomshard2 in caughtdict.keys():
                caughtdict[randomshard2] = int(caughtdict[randomshard2]) + 1
            else:
                caughtdict[randomshard2] = 1

            shardsstr = str(itemdata[guaranshard1]["emoji"]+itemdata[guaranshard1]["emoji"]+itemdata[randomshard1]["emoji"]+itemdata[randomshard2]["emoji"])
            shardmsg = "It left you some **shards**!"

        elif shardamt == 3:
            guaranshard1 = catchguaranshards[creature]
            randomshard1 = random.choice(shards)
            randomshard2 = random.choice(shards)
            if guaranshard1 in caughtdict.keys():
                caughtdict[guaranshard1] = int(caughtdict[guaranshard1]) + 1
            else:
                caughtdict[guaranshard1] = 1
            if randomshard1 in caughtdict.keys():
                caughtdict[randomshard1] = int(caughtdict[randomshard1]) + 1
            else:
                caughtdict[randomshard1] = 1
            if randomshard2 in caughtdict.keys():
                caughtdict[randomshard2] = int(caughtdict[randomshard2]) + 1
            else:
                caughtdict[randomshard2] = 1
            
            shardsstr = str(itemdata[guaranshard1]["emoji"]+itemdata[randomshard1]["emoji"]+itemdata[randomshard2]["emoji"])
            shardmsg = "It left you a few **shards**!"

        elif shardamt == 2:
            guaranshard1 = catchguaranshards[creature]
            randomshard1 = random.choice(shards)
            if guaranshard1 in caughtdict.keys():
                caughtdict[guaranshard1] = int(caughtdict[guaranshard1]) + 1
            else:
                caughtdict[guaranshard1] = 1
            if randomshard1 in caughtdict.keys():
                caughtdict[randomshard1] = int(caughtdict[randomshard1]) + 1
            else:
                caughtdict[randomshard1] = 1

            shardsstr = str(itemdata[guaranshard1]["emoji"]+itemdata[randomshard1]["emoji"])
            shardmsg = "It left you a couple of **shards**!"
        
        elif shardamt == 1:
            randomshard1 = random.choice(shards)
            if randomshard1 in caughtdict.keys():
                caughtdict[randomshard1] = int(caughtdict[randomshard1]) + 1
            else:
                caughtdict[randomshard1] = 1
            
            shardsstr = str(itemdata[randomshard1]["emoji"])
            shardmsg = "It left you a **shard**!"
        
        if random.choice([1, 2, 3, 4, 5]) == 3:
            if "mythicenergy" in caughtdict.keys():
                caughtdict["mythicenergy"] = caughtdict["mythicenergy"] + 1
            else:
                caughtdict["mythicenergy"] = 1
            shardmsg = shardmsg+"\nA vessel of <:mythicenergy:1080212197797539991> **Mythic Energy** was also left behind!"

        caughtdict[creature] = caughtdict[creature] - 1
        with open(path, 'w') as convert_file:
            convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
        f.close()

        await interaction.response.send_message(":wave: You released **"+resultname+"**.\n"+shardsstr+shardmsg)
    else:
        await interaction.response.send_message(random.choice(nocreatures), ephemeral=True)

@tree.command(name="startquest", description="Start a quest with one of your creatures!")
@app_commands.describe(creature='The id of the creature being sent on a quest')
async def test(interaction: discord.Interaction, creature: str):
        unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
        userid = str(interaction.user.id)
        path = Path("./"+userid+".txt")
        canstart = 0

        if not (path).is_file():
            await interaction.response.send_message(random.choice(nofile), ephemeral=True)

        with open(path) as f:
            data = f.read()
            f.close()

        caughtdict = ast.literal_eval(data)

        if creature in caughtdict.keys() and caughtdict[creature] > 0 and not "cannot" in questrewards[creature]:
            if creature in creaturedata.keys():
                if not "questactive" in caughtdict.keys():
                    canstart = 1
                elif caughtdict["questactive"] == 0:
                    canstart = 1
                else:
                    await interaction.response.send_message("One of your creatures is already on a quest! Finish that one first.", ephemeral=True)
                if canstart == 1:
                    caughtdict["questcreature"] = creature
                    caughtdict["questactive"] = 1
                    caughtdict[creature] = caughtdict[creature] - 1
                    caughtdict["questend"] = unix + questrewards[creature]["time"]
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                    f.close()
                    await interaction.response.send_message(creaturedata[creature]["emoji"]+"You sent your **"+creaturedata[creature]["name"]+"** on a quest! It will return with rewards <t:"+str(caughtdict["questend"])+":R>.")
                else:
                    await interaction.response.send_message("If you get this error message I will be very confused...")
            elif creature in itemdata.keys():
                await interaction.response.send_message(random.choice(creaturebutitem), ephemeral=True)
            
            else:
                await interaction.response.send_message(random.choice(nocreatures), ephemeral=True)

        elif "cannot" in questrewards[creature]:
            await interaction.response.send_message("This creature is unable to quest!", ephemeral=True)

        else:
            await interaction.response.send_message(random.choice(nocreatures), ephemeral=True)

@tree.command(name="claimquest", description="Claim your quest rewards!")
async def test(interaction: discord.Interaction):
        unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
        userid = str(interaction.user.id)
        path = Path("./"+userid+".txt")

        if not (path).is_file():
            await interaction.response.send_message(random.choice(nofile), ephemeral=True)

        with open(path) as f:
            data = f.read()
            f.close()

        caughtdict = ast.literal_eval(data)
        print(caughtdict)
        if "questend" in caughtdict.keys():
            print('"questend" found')
            if caughtdict["questactive"] == 1:
                print('"questactive" is 1')
                if caughtdict["questend"] <= unix:
                    print("quest can be claimed")
                    questcreature = caughtdict["questcreature"]
                    print(questcreature)
                    rewards = questrewards[questcreature]["rewards"]
                    guaranteedReward = questrewards[questcreature]["guaranteedReward"]

                    print(str(rewards))

                    reward1 = random.choice(questrewards[questcreature]["reward1"])

                    if reward1 in caughtdict.keys():
                        caughtdict[reward1] = int(caughtdict[reward1]) + 1
                    else:
                        caughtdict[reward1] = 1

                    
                    reward2 = random.choice(questrewards[questcreature]["reward2"])

                    if reward2 in caughtdict.keys():
                        caughtdict[reward2] = int(caughtdict[reward2]) + 1
                    else:
                        caughtdict[reward2] = 1


                    if rewards > 2:

                        reward3 = random.choice(questrewards[questcreature]["reward3"])
                        if reward3 in caughtdict.keys():
                            caughtdict[reward3] = int(caughtdict[reward3]) + 1
                        else:
                            caughtdict[reward3] = 1


                    if rewards > 3:

                        reward4 = random.choice(questrewards[questcreature]["reward4"])
                        if reward4 in caughtdict.keys():
                            caughtdict[reward4] = int(caughtdict[reward4]) + 1
                        else:
                            caughtdict[reward4] = 1

                        
                    if rewards == 5:

                        reward5 = random.choice(questrewards[questcreature]["reward5"])
                        if reward5 in caughtdict.keys():
                            caughtdict[reward5] = int(caughtdict[reward5]) + 1
                        else:
                            caughtdict[reward5] = 1

                    caughtdict["questactive"] = 0
                    caughtdict[questcreature] = caughtdict[questcreature] + 1
                    
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                    f.close()

                    if rewards == 2:
                        await interaction.response.send_message(creaturedata[questcreature]["emoji"]+" **Your "+creaturedata[questcreature]["name"]+" has returned from its quest!**\n \n"+questemojis[guaranteedReward]+questemojis[reward1]+questemojis[reward2]+"Here's what it found.")
                    elif rewards == 3:
                        await interaction.response.send_message(creaturedata[questcreature]["emoji"]+" **Your "+creaturedata[questcreature]["name"]+" has returned from its quest!**\n \n"+questemojis[guaranteedReward]+questemojis[reward1]+questemojis[reward2]+questemojis[reward3]+"Here's what it found.")
                    elif rewards == 4:
                        await interaction.response.send_message(creaturedata[questcreature]["emoji"]+" **Your "+creaturedata[questcreature]["name"]+" has returned from its quest!**\n \n"+questemojis[guaranteedReward]+questemojis[reward1]+questemojis[reward2]+questemojis[reward3]+questemojis[reward4]+"Here's what it found.")
                    elif rewards == 5:
                        await interaction.response.send_message(creaturedata[questcreature]["emoji"]+" **Your "+creaturedata[questcreature]["name"]+" has returned from its quest!**\n \n"+questemojis[guaranteedReward]+questemojis[reward1]+questemojis[reward2]+questemojis[reward3]+questemojis[reward4]+questemojis[reward5]+"Here's what it found.")
                    else:
                        print("reward amount not 2-5 ("+str(rewards)+")")
                else:
                    await interaction.response.send_message("Your quest hasn't finished yet! Be patient.\nIt will return with its rewards in <t:"+str(caughtdict["questend"])+":R>.", ephemeral=True)
            else:
                await interaction.response.send_message("You've already claimed your previous quest! Start a new one first with </startquest:1071183083467968633>.", ephemeral=True)
        else:
            await interaction.response.send_message("You haven't got a quest active! Use </startquest:1071183083467968633> to begin a quest.", ephemeral=True)

@tree.command(name="questinfo", description="View info on the rewards a creature can bring from a quest.")
@app_commands.describe(creature='The id of the creature')
async def test(interaction: discord.Interaction, creature: str):
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")
    if not (path).is_file():
        await interaction.response.send_message(random.choice(nofile), ephemeral=True)

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)
    if creature in creaturedata.keys() and creature in caughtdict.keys():
        if creature == "leez":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:leezrd:831177020108963890> Leez-rd Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:leezrd:831177020108963890> Leez-rd Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Guaranteed Reward:", value="<:leezrd:831177020108963890>", inline=False)
            embed.add_field(name=f"Quest Time:", value="4 Hours", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value=":cut_of_meat: :stopwatch:", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value="<:leezrd:831177020108963890> <:beth:905871385379893289> <:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:greenshard:1070017427183771799> <:leezrd:831177020108963890>", inline=False)
        elif creature == "beth":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:beth:905871385379893289> Beth Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:beth:905871385379893289> Beth Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="4 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:beth:905871385379893289>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value=":beans: :compass:", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value="<:beth:905871385379893289> <:bryan:930494048949641227>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:blueshard:1070017442295840929> <:beth:905871385379893289>", inline=False)
        elif creature == "residue":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title=":grey_question: Leez-rd Residue Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title=":grey_question: Leez-rd Residue Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="4 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value=":grey_question:", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value="<:leezrd:831177020108963890> <:beth:905871385379893289> :grey_question:", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value=":cut_of_meat: :beans:", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:greenshard:1070017427183771799> <:blueshard:1070017442295840929>", inline=False)
        elif creature == "bryan":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:bryan:930494048949641227> Bryan Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:bryan:930494048949641227> Bryan Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="6 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:beth:905871385379893289>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value=":beans: <:beth:905871385379893289>", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value=":beans: <:bryan:930494048949641227>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:beth:905871385379893289> <:bryan:930494048949641227>", inline=False)
            embed.add_field(name=f"4th Possible Reward:", value="<:redshard:1070017410205241374> <:bryan:930494048949641227>", inline=False)
        elif creature == "carcassite":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:carcassite:1041737974947254445> Carcassite Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:carcassite:1041737974947254445> Carcassite Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="6 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:leezrd:831177020108963890>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value="<:leezrd:831177020108963890> <:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value=":label: <:carcassite:1041737974947254445>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:redshard:1070017410205241374> <:carcassite:1041737974947254445>", inline=False)
        elif creature == "albino":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:albinoleezrd:838122895225782322> Albino Leez-rd Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:albinoleezrd:838122895225782322> Albino Leez-rd Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="8 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value="<:leezrd:831177020108963890> <:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value="<:leezrd:831177020108963890> <:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:leezrd:831177020108963890> <:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"4th Possible Reward:", value="<:leezrd:831177020108963890> <:albinoleezrd:838122895225782322>", inline=False)
            embed.add_field(name=f"5th Possible Reward:", value="<:leezrd:831177020108963890> <:albinoleezrd:838122895225782322>", inline=False)
        elif creature == "poopyshoes":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:poopyshoes:963147618626723840> Poopyshoes Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:poopyshoes:963147618626723840> Poopyshoes Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="12 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:poopyshoes:963147618626723840>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value=":stopwatch: :paintbrush:", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value=":stopwatch: :label:", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:redshard:1070017410205241374> <:greenshard:1070017427183771799> <:blueshard:1070017442295840929>", inline=False)
            embed.add_field(name=f"4th Possible Reward:", value=":stopwatch: :compass:", inline=False)
        elif creature == "redprismalgam":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:redprismalgam:1070437926971912204> Red Prismalgam Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:redprismalgam:1070437926971912204> Red Prismalgam Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="6 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:redshard:1070017410205241374>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value="<:redshard:1070017410205241374> <:greenshard:1070017427183771799>", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value="<:redshard:1070017410205241374> <:blueshard:1070017442295840929>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:greenshard:1070017427183771799> <:blueshard:1070017442295840929>", inline=False)
        elif creature == "greenprismalgam":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:greenprismalgam:1070433518569656451> Green Prismalgam Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:greenprismalgam:1070433518569656451> Green Prismalgam Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="6 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:greenshard:1070017427183771799>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value="<:greenshard:1070017427183771799> <:redshard:1070017410205241374>", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value="<:greenshard:1070017427183771799> <:blueshard:1070017442295840929>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:redshard:1070017410205241374> <:blueshard:1070017442295840929>", inline=False)
        elif creature == "blueprismalgam":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:blueprismalgam:1070437016539516959> Blue Prismalgam Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:blueprismalgam:1070437016539516959> Blue Prismalgam Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="6 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:blueshard:1070017442295840929>", inline=False)
            embed.add_field(name=f"1st Possible Reward:", value="<:blueprismalgam:1070437016539516959> <:redshard:1070017410205241374>", inline=False)
            embed.add_field(name=f"2nd Possible Reward:", value="<:blueprismalgam:1070437016539516959> <:greenshard:1070017427183771799>", inline=False)
            embed.add_field(name=f"3rd Possible Reward:", value="<:redshard:1070017410205241374> <:greenshard:1070017427183771799>", inline=False)
        elif creature == "blackprismalgam":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:blackprismalgam:1071878412102283274> Black Prismalgam Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:blackprismalgam:1071878412102283274> Black Prismalgam Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="6 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:blackshard:1071862902379790468>", inline=False)
            embed.add_field(name=f"1st Reward:", value="<:redshard:1070017410205241374>", inline=False)
            embed.add_field(name=f"2nd Reward:", value="<:greenshard:1070017427183771799>", inline=False)
            embed.add_field(name=f"3rd Reward:", value="<:blueshard:1070017442295840929>", inline=False)
        
        elif creature == "frorg":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="<:frorg:1074423071248764938> Frorg Quest Rewards", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="<:frorg:1074423071248764938> Frorg Quest Rewards", color=discord.Color.from_rgb(creaturedata[creature]["colour"]["red"], creaturedata[creature]["colour"]["green"], creaturedata[creature]["colour"]["blue"]))
            embed.add_field(name=f"Quest Time:", value="4 Hours", inline=False)
            embed.add_field(name=f"Guaranteed Reward:", value="<:beth:905871385379893289>", inline=False)
            embed.add_field(name=f"1st Reward:", value=":stew: :scroll: <:blackshard:1071862902379790468>", inline=False)
            embed.add_field(name=f"2nd Reward:", value=":stew: :scroll: <:blackshard:1071862902379790468>", inline=False)
        
        await interaction.response.send_message(embed=embed)

    else:
        await interaction.response.send_message("That quest doesn't exist! You can send any creatures you have on quests.", ephemeral=True)

@tree.command(name="craft", description="View the current crafting recipes, or craft something!")
@app_commands.describe(recipe="The recipe number. Don't use this argument if you want to view recipes.")
async def test(interaction: discord.Interaction, recipe: Optional[int]):
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
        filemake = {}
        with open(path, 'w') as f:
            f.write(str(filemake))
        f.close()

    with open(path) as f:
        data = f.read()
        f.close()

    caughtdict = ast.literal_eval(data)

    if "poopyshoes" in caughtdict.keys():

        if "embedR" in caughtdict.keys():
            embed = discord.Embed(title="Crafting", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
        else:
            embed = discord.Embed(title="Crafting", color=discord.Color.from_rgb(160, 160, 160))

        if recipe == 1:
            buy1 = recipes["recipe1"]["buy1"]["id"]
            buy1amt = recipes["recipe1"]["buy1"]["amount"]
            buy2 = recipes["recipe1"]["buy2"]["id"]
            buy2amt = recipes["recipe1"]["buy2"]["amount"]
            sell = recipes["recipe1"]["sell"]["id"]
            sellamt = recipes["recipe1"]["sell"]["amount"]
            if buy1 in caughtdict.keys() and buy2 in caughtdict.keys() and caughtdict[buy1] > buy1amt-1 and caughtdict[buy2] > buy2amt-1:
                caughtdict[buy1] = caughtdict[buy1] - buy1amt
                caughtdict[buy2] = caughtdict[buy2] - buy2amt
                if sell in caughtdict.keys():
                    caughtdict[sell] = caughtdict[sell] + sellamt
                else:
                    caughtdict[sell] = sellamt
                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                f.close()
                await interaction.response.send_message("You crafted "+recipes["recipe1"]["sell"]["emoji"]+"**"+recipes["recipe1"]["sell"]["name"]+"** x"+str(recipes["recipe1"]["sell"]["amount"])+"!")
            else:
                await interaction.response.send_message(random.choice(noitems), ephemeral=True)
        
        elif recipe == 2:
            buy1 = recipes["recipe2"]["buy1"]["id"]
            buy1amt = recipes["recipe2"]["buy1"]["amount"]
            buy2 = recipes["recipe2"]["buy2"]["id"]
            buy2amt = recipes["recipe2"]["buy2"]["amount"]
            sell = recipes["recipe2"]["sell"]["id"]
            sellamt = recipes["recipe2"]["sell"]["amount"]
            if buy1 in caughtdict.keys() and buy2 in caughtdict.keys() and caughtdict[buy1] > buy1amt-1 and caughtdict[buy2] > buy2amt-1:
                caughtdict[buy1] = caughtdict[buy1] - buy1amt
                caughtdict[buy2] = caughtdict[buy2] - buy2amt
                if sell in caughtdict.keys():
                    caughtdict[sell] = caughtdict[sell] + sellamt
                else:
                    caughtdict[sell] = sellamt
                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                f.close()
                await interaction.response.send_message("You crafted "+recipes["recipe2"]["sell"]["emoji"]+"**"+recipes["recipe2"]["sell"]["name"]+"** x"+str(recipes["recipe2"]["sell"]["amount"])+"!")
            else:
                await interaction.response.send_message(random.choice(noitems), ephemeral=True)
        
        elif recipe == 3:
            buy1 = recipes["recipe3"]["buy1"]["id"]
            buy1amt = recipes["recipe3"]["buy1"]["amount"]
            buy2 = recipes["recipe3"]["buy2"]["id"]
            buy2amt = recipes["recipe3"]["buy2"]["amount"]
            sell = recipes["recipe3"]["sell"]["id"]
            sellamt = recipes["recipe3"]["sell"]["amount"]
            if buy1 in caughtdict.keys() and buy2 in caughtdict.keys() and caughtdict[buy1] > buy1amt-1 and caughtdict[buy2] > buy2amt-1:
                caughtdict[buy1] = caughtdict[buy1] - buy1amt
                caughtdict[buy2] = caughtdict[buy2] - buy2amt
                if sell in caughtdict.keys():
                    caughtdict[sell] = caughtdict[sell] + sellamt
                else:
                    caughtdict[sell] = sellamt
                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                f.close()
                await interaction.response.send_message("You crafted "+recipes["recipe3"]["sell"]["emoji"]+"**"+recipes["recipe3"]["sell"]["name"]+"** x"+str(recipes["recipe3"]["sell"]["amount"])+"!")
            else:
                await interaction.response.send_message(random.choice(noitems), ephemeral=True)

        elif recipe is None:
            buy1_1 = recipes["recipe1"]["buy1"]["emoji"]+"x"+str(recipes["recipe1"]["buy1"]["amount"])
            buy2_1 = recipes["recipe1"]["buy2"]["emoji"]+"x"+str(recipes["recipe1"]["buy2"]["amount"])
            sell_1 = recipes["recipe1"]["sell"]["emoji"]+"x"+str(recipes["recipe1"]["sell"]["amount"])
            print("`[1]` "+buy1_1+buy2_1+" -> "+sell_1)
            embed.add_field(name=f"`[1]` "+buy1_1+" "+buy2_1+" -> "+sell_1, value=" ", inline=False)

            buy1_2 = recipes["recipe2"]["buy1"]["emoji"]+"x"+str(recipes["recipe2"]["buy1"]["amount"])
            buy2_2 = recipes["recipe2"]["buy2"]["emoji"]+"x"+str(recipes["recipe2"]["buy2"]["amount"])
            sell_2 = recipes["recipe2"]["sell"]["emoji"]+"x"+str(recipes["recipe2"]["sell"]["amount"])
            print("`[2]` "+buy1_2+buy2_2+" -> "+sell_2)
            embed.add_field(name=f"`[2]` "+buy1_2+" "+buy2_2+" -> "+sell_2, value=" ", inline=False)

            buy1_3 = recipes["recipe3"]["buy1"]["emoji"]+"x"+str(recipes["recipe3"]["buy1"]["amount"])
            buy2_3 = recipes["recipe3"]["buy2"]["emoji"]+"x"+str(recipes["recipe3"]["buy2"]["amount"])
            sell_3 = recipes["recipe3"]["sell"]["emoji"]+"x"+str(recipes["recipe3"]["sell"]["amount"])
            print("`[3]` "+buy1_3+buy2_3+" -> "+sell_3)
            embed.add_field(name=f"`[3]` "+buy1_3+" "+buy2_3+" -> "+sell_3, value=" ", inline=False)

            embed.set_footer(text="To craft use /craft <recipe number>.")

            await interaction.response.send_message(embed=embed)

        else:
            await interaction.response.send_message("That's an invalid recipe number! Pick between 1-3.", ephemeral=True)
    else:
        await interaction.response.send_message("Before you can craft, you have to have caught Poopyshoes!", ephemeral=True)

@tree.command(name="cancelquest", description="Cancel a quest early.")
async def test(interaction: discord.Interaction):
        unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
        userid = str(interaction.user.id)
        path = Path("./"+userid+".txt")

        if not (path).is_file():
            await interaction.response.send_message(random.choice(nofile), ephemeral=True)

        with open(path) as f:
            data = f.read()
            f.close()

        caughtdict = ast.literal_eval(data)
        print(caughtdict)
        if "questend" in caughtdict.keys():
            print('"questend" found')
            if caughtdict["questactive"] == 1:
                print('"questactive" is 1')
                if caughtdict["questend"] > unix:

                    questcreature = caughtdict["questcreature"]

                    caughtdict["questactive"] = 0
                    caughtdict["questend"] = unix
                    caughtdict[questcreature] = caughtdict[questcreature] + 1

                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    await interaction.response.send_message(creaturedata[questcreature]["emoji"]+":octagonal_sign: **Your "+creaturedata[questcreature]["name"]+" returned early from its quest.** (Quest cancelled)")
                else:
                    await interaction.response.send_message("Your quest has already finished! You can't cancel it.", ephemeral=True)
            else:
                await interaction.response.send_message("You don't currently have a quest active! Use </startquest:1071183083467968633> to begin a quest.", ephemeral=True)
        else:
            await interaction.response.send_message("You don't currently have a quest active! Use </startquest:1071183083467968633> to begin a quest.", ephemeral=True)

@tree.command(name="rex", description="Feed Rex Anomaliae or view your progress.")
@app_commands.describe(feed="Creature or item id to sacrifice one of")
async def test(interaction: discord.Interaction, feed: Optional[str]):
        userid = str(interaction.user.id)
        path = Path("./"+userid+".txt")

        if not (path).is_file():
            filemake = {}
            with open(path, 'w') as f:
                f.write(str(filemake))
            f.close()

        with open(path) as f:
            data = f.read()
            f.close()

        caughtdict = ast.literal_eval(data)

        if "rexlevel" not in caughtdict.keys():
                caughtdict["rexlevel"] = 0
                caughtdict["rexenergy"] = 1
                print("created levels n stuff")
        
        level = caughtdict["rexlevel"]
        energy = caughtdict["rexenergy"]

        if level == 0:
            nextlevelreq = 150
        elif level == 1:
            nextlevelreq = 300
        elif level == 2:
            nextlevelreq = 450


        if feed is None:
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="Rex Anomaliae", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="Rex Anomaliae", color=discord.Color.from_rgb(0, 148, 0))

            embed.add_field(name= " ", value="Energy: **"+str(energy)+"**", inline=False)
            if level == 0:
                embed.add_field(name= "Current Level: 0/3", value="(No current perks)", inline=False)
            if level == 1:
                embed.add_field(name= "Current Level: 1/3", value="Can access the Terminal.", inline=False)
            if level == 2:
                embed.add_field(name= "Current Level: 2/3", value="Can access the Terminal.", inline=False)
            if level == 3:
                embed.add_field(name= "Current Level: 3/3", value="Can access the Terminal. The cooldown for catching is reduced to 45 minutes.", inline=False)
            
            if not level == 3:
                embed.add_field(name=" ", value="Energy for next level: **"+str(nextlevelreq - energy)+"** (Required "+str(nextlevelreq)+")", inline=False)
                embed.add_field(name="Feeding Rex Anomaliae", value="Each creature and item contains a set amount of energy. You can feed them to Rex Anomaliae to increase its energy and level it up.", inline=False)
            else:
                embed.add_field(name="Feeding Rex Anomaliae", value="Rex Anomaliae has reached its ultimate level! You can still feed it, but this will not prosper any rewards.", inline=False)
            embed.set_footer(text="Use /rex [creature/item id] to feed an item.")

            await interaction.response.send_message(embed=embed)

        elif feed in rexfoods and feed in caughtdict.keys():
            if caughtdict[feed] > 0:
                caughtdict[feed] = caughtdict[feed] - 1
                caughtdict["rexenergy"] = caughtdict["rexenergy"] + rexfoods[feed]
                if caughtdict["rexenergy"] > 449:
                    caughtdict["rexlevel"] = 3
                elif caughtdict["rexenergy"] > 299:
                    caughtdict["rexlevel"] = 2
                elif caughtdict["rexenergy"] > 149:
                    caughtdict["rexlevel"] = 1
                else:
                    caughtdict["rexlevel"] = 0

                if not caughtdict["rexlevel"] == level:
                    rexmsg = questemojis[feed]+" ...with little to no effort, the mighty beast leapt up and swallowed your offering. (+"+str(rexfoods[feed])+" energy)"+"\nIt roared with glee. **Rex Anomaliae has reached a new level**."
                else:
                    rexmsg = questemojis[feed]+" ...with little to no effort, the mighty beast leapt up and swallowed your offering. (+"+str(rexfoods[feed])+" energy)"
                
                if feed in creaturedata.keys() and random.choice([1, 2, 3, 4, 5]) == 3:
                    if "mythicenergy" in caughtdict.keys():
                        caughtdict["mythicenergy"] = caughtdict["mythicenergy"] + 1
                    else:
                        caughtdict["mythicenergy"] = 1
                    rexmsg = rexmsg+"\nA vessel of <:mythicenergy:1080212197797539991> **Mythic Energy** was also left behind."
                
                await interaction.response.send_message(rexmsg)

            elif feed in itemdata.keys():
                await interaction.response.send_message(random.choice(noitems), ephemeral=True)
            
            elif feed in creaturedata.keys():
                await interaction.response.send_message(random.choice(nocreatures), ephemeral=True)

            else:
                await interaction.response.send_message("how ... ? did you get??? this message ? ? ?? ? ? ? ?? ?? ?", ephemeral=True)

        else:
            await interaction.response.send_message("that's not possible.", ephemeral=True)
        
        with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
        f.close()

@tree.command(name="terminal", description="Run a command in the mysterious terminal.")
@app_commands.describe(command='A command to run, or "help" for help.')
async def test(interaction: discord.Interaction, command: str):
    unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")

    if not (path).is_file():
        filemake = {}
        with open(path, 'w') as f:
            f.write(str(filemake))
        f.close()

    with open(path) as f:
            data = f.read()
            f.close()

    caughtdict = ast.literal_eval(data)
    if ("rexlevel" in caughtdict.keys() and caughtdict["rexlevel"] >=1) and ((not "dream" in caughtdict.keys()) or "dreams" in command or ("dream" in caughtdict.keys() and command in valid_dreams[caughtdict["dream"]])):
        if not "directory" in caughtdict.keys() or not "knowncommands" in caughtdict.keys():
            caughtdict["directory"] = "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/terminal"
            caughtdict["knowncommands"] = ["help", "cd"]
            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
            f.close()
        
        if command in ter_validcommands and not command in caughtdict["knowncommands"]:
                knowncommands = list(caughtdict["knowncommands"])
                knowncommands.extend([command])
                print(knowncommands)
                caughtdict["knowncommands"] = knowncommands

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()

        if command == "cd" or command == "cd ":
            await interaction.response.send_message(content="`$ "+command+"`\n"+"Invalid syntax!\nUse `$ cd <directory>` to navigate to a directory, or `$ cd ..` to go up a folder.")

        elif "cd " in command:
            attempted_dir = command.removeprefix("cd ")
            invalid_dir = False

            if attempted_dir == "//":
                directory = caughtdict["directory"]
            elif attempted_dir == "home":
                directory = "/Users/emjay/Desktop/Secret/Discord/Leez-rd Bot/terminal"
            elif attempted_dir == "/":
                directory = "/"
            elif attempted_dir == "..":
                directory = ter_backdirs[caughtdict["directory"]]
            elif attempted_dir.removesuffix("/") in ter_dirs.keys():
                directory = attempted_dir.removesuffix("/")
            elif str(caughtdict["directory"]+attempted_dir).removesuffix("/") in ter_dirs.keys():
                directory = caughtdict["directory"]+attempted_dir.removesuffix("/")
            elif str(caughtdict["directory"]+"/"+attempted_dir).removesuffix("/") in ter_dirs.keys():
                directory = str(caughtdict["directory"]+"/"+attempted_dir).removesuffix("/")
            else:
                invalid_dir = True
            
            print(str("/"+caughtdict["directory"]+"/"+attempted_dir))
            
            print(attempted_dir)
            
            if invalid_dir is True:
                await interaction.response.send_message("`$ "+command+"`"+"\nThat directory does not exist!", ephemeral=True)
            elif "secured" in ter_dirs[directory] and ter_dirs[directory]["secured"] is True and (not "admin" in caughtdict.keys() or not caughtdict["admin"] == 1):
                await interaction.response.send_message("`$ "+command+"`"+"\nInsufficient permissions to access this directory.", ephemeral=True)
            elif "toolarge" in ter_dirs[directory] and ter_dirs[directory]["toolarge"] is True:
                await interaction.response.send_message("`$ "+command+"`"+"\nTarget folder is too large to access.", ephemeral=True)
            else:
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title=directory, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title=directory, color=discord.Color.from_rgb(0, 0, 0))

                caughtdict["directory"] = directory

                if "dir" in ter_dirs[directory]:
                    for dir in ter_dirs[directory]["dir"]:
                            if dir == "..":
                                embed.add_field(value=":arrow_left: ..", name="", inline=False)
                            elif caughtdict["directory"] == "/" or not "hidden" in ter_dirs[caughtdict["directory"]+"/"+dir]:
                                if not caughtdict["directory"] == "/" and "toolarge" in ter_dirs[caughtdict["directory"]+"/"+dir] and ter_dirs[caughtdict["directory"]+"/"+dir]["toolarge"] is True:
                                    embed.add_field(value=":open_file_folder: "+dir, name="", inline=False)
                                elif caughtdict["directory"] == "/" and "secured" in ter_dirs["/"+dir] and ter_dirs["/"+dir]["secured"] == 1:
                                    if "admin" in caughtdict.keys() and caughtdict["admin"] == 1:
                                        embed.add_field(value=":file_folder: "+dir, name="", inline=False)
                                    else:
                                        embed.add_field(value=":closed_lock_with_key: "+dir, name="", inline=False)
                                elif not caughtdict["directory"] == "/" and "secured" in ter_dirs[caughtdict["directory"]+"/"+dir] and ter_dirs[caughtdict["directory"]+"/"+dir]["secured"] is True:
                                    if "admin" in caughtdict.keys() and caughtdict["admin"] == 1:
                                        embed.add_field(value=":file_folder: "+dir, name="", inline=False)
                                    else:
                                        embed.add_field(value=":closed_lock_with_key: "+dir, name="", inline=False)
                                else:
                                    embed.add_field(value=":file_folder: "+dir, name="", inline=False)
                    if "txt" in ter_dirs[directory]:
                        for txt in ter_dirs[directory]["txt"]:
                            if txt == "password_piece.txt":
                                embed.add_field(value=":jigsaw: "+txt, name="", inline=False)
                            else:
                                embed.add_field(value=":notepad_spiral: "+txt, name="", inline=False)
                    if "jpeg" in ter_dirs[directory]:
                        for jpeg in ter_dirs[directory]["jpeg"]:
                            embed.add_field(value=":sunrise_over_mountains: "+jpeg, name="", inline=False)
                    if "zip" in ter_dirs[directory]:
                        for zip in ter_dirs[directory]["zip"]:
                            embed.add_field(value=":minidisc: "+zip, name="", inline=False)
                    if "cmd" in ter_dirs[directory]:
                        for cmd in ter_dirs[directory]["cmd"]:
                            embed.add_field(value=":computer: "+cmd, name="", inline=False)

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()

                await interaction.response.send_message(content="`$ "+command+"`", embed=embed, ephemeral=True)
        elif "txt" in ter_dirs[caughtdict["directory"]] and command in ter_dirs[caughtdict["directory"]]["txt"] or "jpeg" in ter_dirs[caughtdict["directory"]] and command in ter_dirs[caughtdict["directory"]]["jpeg"] or "zip" in ter_dirs[caughtdict["directory"]] and command in ter_dirs[caughtdict["directory"]]["zip"]:
            if "jpeg" in ter_dirs[caughtdict["directory"]] and command in ter_dirs[caughtdict["directory"]]["jpeg"]:
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title=command, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title=command, color=discord.Color.from_rgb(0, 0, 0))
                embed.set_image(url=ter_content[caughtdict["directory"]][command])
                await interaction.response.send_message(content="`$ "+command+"`", embed=embed, ephemeral=True)
            else:    
                if ter_content[caughtdict["directory"]][command] == "PW_ANIMAL":
                    message_content = "Remember the animal. It's "+terAdmin_animalhints[terAdmin_animal]
                elif ter_content[caughtdict["directory"]][command] == "PW_POKEMON":
                    message_content = "Remember the Pokémon. It's number "+terAdmin_pokenumber+"."
                elif ter_content[caughtdict["directory"]][command] == "PW_NUMBER":
                    message_content = "Remember the number. It's "+terAdmin_number+"."
                else:
                    message_content = ter_content[caughtdict["directory"]][command]
                await interaction.response.send_message(content="`$ "+command+"`\n```"+message_content+"```", ephemeral=True)
        elif command == "uwu":
            await interaction.response.send_message(content="`$ "+command+"`\n"+"Invalid syntax! Use `$ uwu <message>` to uwu-ify.")
        elif "uwu " in command and not command == command.removeprefix("uwu "):
            if not "uwu" in caughtdict["knowncommands"]:
                knowncommands = list(caughtdict["knowncommands"])
                knowncommands.extend(['uwu'])
                print(knowncommands)
                caughtdict["knowncommands"] = knowncommands

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()
            uwutext = command.removeprefix("uwu ")
            uwutext = uwutext.lower()
            uwutext = uwutext.replace("you", "uwu")
            uwutext = uwutext.replace("r", "w")
            uwutext = uwutext.replace("l", "w")
            uwutext = uwutext.replace(".", "")
            uwutext = uwutext.replace("!", "")
            uwutext = uwutext.replace("?", "")
            uwutext = uwutext+random.choice(["! ", ". ", "!! "])
            uwutext = uwutext+random.choice([":3 ", ">w< ", "owo ", ">//w//< ", "o3o ", "~//~ ", "✧*:･ﾟ✧ ", ":fox: ", "♡", ":sparkling_heart:", ":sparkles:", ":hearts:", ":revolving_hearts:", " "])
            await interaction.response.send_message(content="`$ "+command+"`\n"+uwutext)
        elif command == "raphael":
            await interaction.response.send_message(content="`$ "+command+"`\n"+random.choice(["staaanley", "stanley", "STANLEY", "*stanley*", "*staaaaanley*", "stanleyyyyyyyy", "**Stanley**", "Stanley", "stanley..", "`Stanley`"])+random.choice(["", ".", "!", "?"]))
        elif command == "clearcol":
            if "embedR" in caughtdict.keys():
                del caughtdict["embedR"]
                del caughtdict["embedG"]
                del caughtdict["embedB"]
                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()
                await interaction.response.send_message(content="`$ "+command+"`\nYour embed colour was cleared!")
            else:
                await interaction.response.send_message(content="`$ "+command+"`\nYou already have no custom embed colour! Nothing was changed.")
        elif command == "adminunlock":
            await interaction.response.send_message(content="`$ "+command+"`\n"+"Please input a password.")
        elif "adminunlock " in command and not command == command.removeprefix("adminunlock "):
            if not "adminunlock" in caughtdict["knowncommands"]:
                knowncommands = list(caughtdict["knowncommands"])
                knowncommands.extend(['adminunlock'])
                print(knowncommands)
                caughtdict["knowncommands"] = knowncommands

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()

            attempted_password = command.removeprefix("adminunlock ")
            attempted_password = attempted_password.replace(" ", "")
            print(interaction.user.name+" guessed the password: "+attempted_password+"\nThe correct password is "+terAdmin_password)
            if attempted_password == terAdmin_password:
                if "admin" in caughtdict.keys() and caughtdict["admin"] == 1:
                    await interaction.response.send_message(content="`$ "+command+"`\n:tada: **Password is correct!** ...but you already have admin access.")
                else:
                    caughtdict["admin"] = 1
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()

                    await interaction.response.send_message(content="`$ "+command+"`\n:tada: **Password is correct!** You can now access folders and run commands that require admin permissions.")
            elif attempted_password.lower() in funPasswords.keys():
                await interaction.response.send_message(content="`$ "+command+"`\n"+funPasswords[attempted_password.lower()])
            else:
                if "admin" in caughtdict.keys() and caughtdict["admin"] == 1:
                    await interaction.response.send_message(content="`$ "+command+"`\nPassword is incorrect. ...but you already have admin access!")
                else:
                    await interaction.response.send_message(content="`$ "+command+"`\nPassword is incorrect.")
        elif command == "garden":
            await interaction.response.send_message(content="`$ "+command+"`\nCannot run command.")
        elif command == "adventure":
            await interaction.response.send_message(content="`$ "+command+"`\nCannot run command.")
        elif command == "funky":
            caughtdict["embedR"] = random.choice(range(1, 256))
            caughtdict["embedG"] = random.choice(range(1, 256))
            caughtdict["embedB"] = random.choice(range(1, 256))
            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
            f.close()
            await interaction.response.send_message(content="`$ "+command+"`\n:mirror_ball:**Funkified your embed colour!**")
        elif command == "help":
            if "embedR" in caughtdict.keys():
                embed = discord.Embed(title="Discovered Commands", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
            else:
                embed = discord.Embed(title="Discovered Commands", color=discord.Color.from_rgb(136, 136, 136))
            embed.add_field(name=f"Type `$ help [command]` for detailed information on a command.", value=" ", inline=False)
            
            knowncommands = caughtdict["knowncommands"]

            fun = 0
            funcmds = " - "

            system = 0
            systemcmds = " - "

            tool = 0
            toolcmds = " - "

            prism_ = 0
            prismcmds = " - "

            aqua = 0
            aquacmds = " - "

            for item in knowncommands:
                if item in ter_cmdcategories["fun"]:
                    fun = 1
                elif item in ter_cmdcategories["system"]:
                    system = 1
                elif item in ter_cmdcategories["tool"]:
                    tool = 1
                elif item in ter_cmdcategories["prism"]:
                    prism_ = 1
                elif item in ter_cmdcategories["aqua"]:
                    aqua = 1
                else:
                    print("No category assigned to this command: "+item)
            for item in ter_cmdcategories["fun"]:
                if item in caughtdict["knowncommands"]:
                    funcmds = funcmds+"`"+item+"`, "
            for item in ter_cmdcategories["system"]:
                if item in caughtdict["knowncommands"]:
                    systemcmds = systemcmds+"`"+item+"`, "
            for item in ter_cmdcategories["tool"]:
                if item in caughtdict["knowncommands"]:
                    toolcmds = toolcmds+"`"+item+"`, "
            for item in ter_cmdcategories["prism"]:
                if item in caughtdict["knowncommands"]:
                    prismcmds = prismcmds+"`"+item+"`, "
            for item in ter_cmdcategories["aqua"]:
                if item in caughtdict["knowncommands"]:
                    aquacmds = aquacmds+"`"+item+"`, "

            if fun == 1:
                embed.add_field(name=" ",value=":gem: **Fun**"+funcmds.removesuffix(", "),inline=False)
            if aqua == 1:
                embed.add_field(name=" ",value=":ocean: **Aqua**"+aquacmds.removesuffix(", "),inline=False)
            if prism_ == 1:
                embed.add_field(name=" ",value="<:mythicenergy:1080212197797539991> **Prism**"+prismcmds.removesuffix(", "),inline=False)
            if system == 1:
                embed.add_field(name=" ",value=":gear: **System**"+systemcmds.removesuffix(", "),inline=False)
            if tool == 1:
                embed.add_field(name=" ",value=":tools: **Tools**"+toolcmds.removesuffix(", "),inline=False)
            
            await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed, ephemeral=True)

        elif "help " in command and not command == command.removeprefix("help "):
            helpcmd = command.removeprefix("help ")
            helpcmd = helpcmd.lower()
            if helpcmd in ter_validcommands:
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="$ "+helpcmd, color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="$ "+helpcmd, color=discord.Color.from_rgb(136, 136, 136))

                if helpcmd in ter_validcommands and not helpcmd in caughtdict["knowncommands"]:
                    knowncommands = list(caughtdict["knowncommands"])
                    knowncommands.extend([helpcmd])
                    print(knowncommands)
                    caughtdict["knowncommands"] = knowncommands

                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
            
                embed.add_field(value=ter_cmds[helpcmd]["help"], name=" ", inline=False)
                embed.add_field(name="Usage", value=ter_cmds[helpcmd]["usage"], inline=True)
                if "examples" in ter_cmds[helpcmd]:
                    embed.add_field(name="Example", value=ter_cmds[helpcmd]["examples"], inline=True)
            
                await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)

            else:
                await interaction.response.send_message(content="`$ "+command+"`\nThat command doesn't exist :/",ephemeral=True)
        elif command == "rebuild":
            await interaction.response.send_message(content="`$ "+command+"`\n"+"Invalid syntax! Use `$ help rebuild` for info on how to use this command.")
        elif command == "bert":
            if not "bertsanct" in caughtdict.keys():
                if "bert" in caughtdict.keys() and caughtdict["bert"] >= 5:
                    caughtdict["bertsanct"] = {}

                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    await interaction.response.send_message("**Welcome to your very own *Bertery***! Here you can collect various forms of Bert, the mushroom-shaped creature.\nUse `$ bert exchange` to transform one of your regular Berts into another form.")
                else:
                    await interaction.response.send_message("<:bert:1079448808729104485> You must first acquire **5** Berts before being able to access this command!")
            
            else:
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title=interaction.user.display_name+"'s Bertery", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title=interaction.user.display_name+"'s Bertery", color=discord.Color.from_rgb(255, 12, 12))
                
                text = ""

                for bert in berts.keys():
                    if bert in caughtdict["bertsanct"]:
                        text += "\n**"+berts[bert]["emoji"]+berts[bert]["name"]+"** x"+str(caughtdict["bertsanct"][bert])
                    else:
                        text += "\n:grey_question: Undiscovered Bert"

                bertsanct = caughtdict["bertsanct"]

                embed.add_field(name="Berts obtained ("+str(len(bertsanct.keys()))+"/"+str(len(berts.keys()))+")", value=text, inline=False)

                embed.add_field(name="", value="Use `$ bert exchange` to swap a regular Bert for a different Bert form.", inline=False)

                await interaction.response.send_message(embed=embed)
                
        
        elif "bert " in command and not command == command.removeprefix("bert "):
            if "bertsanct" in caughtdict.keys():
                if command == "bert exchange":
                    if caughtdict["bert"] > 0:
                        bertobtained = random.choice(list(berts.keys()))
                        caughtdict["bert"] -= 1

                        if bertobtained in caughtdict["bertsanct"]:
                            caughtdict["bertsanct"][bertobtained] += 1
                        else:
                            caughtdict["bertsanct"][bertobtained] = 1


                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()

                        bertsanct = caughtdict["bertsanct"]


                        await interaction.response.send_message("<:bert:1079448808729104485>:wave: You wave goodbye to a **Bert**.\n"+berts[bertobtained]["emoji"]+" You got a special **"+berts[bertobtained]["name"]+"**! View your collection of berts with `$ bert`.")
                        if not "bertmedal" in caughtdict.keys() and len(bertsanct.keys()) == 9:

                            caughtdict["bertmedal"] = 1

                            with open(path, 'w') as convert_file:
                                convert_file.write(json.dumps(caughtdict))
                            print(caughtdict)
                            f.close()

                            await interaction.followup.send("<:bert:1079448808729104485> You earned the **Bert Medal** for completing your Bert collection! </trophies:1069668767044472912>")
                    else:
                        await interaction.response.send_message("You are missing a **regular Bert** to swap for a special form!")
                
                else:
                    await interaction.response.send_message("Command invalid! Look at `$ help bert` for valid Bert-related commands.")

            else:
                await interaction.response.send_message("Please acquire access to this command through `$ bert` first!")
        
        elif command == "remove":
            if "prism" in caughtdict.keys() and not caughtdict["prism"] == "none":
                if caughtdict["prism"] == "red":
                    caughtdict["redshard"] = caughtdict["redshard"] + 8
                    caughtdict["mythicenergy"] = caughtdict["mythicenergy"] + 2

                elif caughtdict["prism"] == "green":
                    caughtdict["greenshard"] = caughtdict["greenshard"] + 8
                    caughtdict["mythicenergy"] = caughtdict["mythicenergy"] + 2

                elif caughtdict["prism"] == "blue":
                    caughtdict["blueshard"] = caughtdict["blueshard"] + 8
                    caughtdict["mythicenergy"] = caughtdict["mythicenergy"] + 2

                elif caughtdict["prism"] == "black":
                    caughtdict["blackshard"] = caughtdict["blackshard"] + 8
                    caughtdict["mythicenergy"] = caughtdict["mythicenergy"] + 2

                caughtdict["prism"] = "none"
                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()

                await interaction.response.send_message(content="`$ "+command+"`\n"+"You removed your prism, and salvaged some parts back from it!")
            else:
                await interaction.response.send_message(content="`$ "+command+"`\n"+"You don't have a prism active!", ephemeral=True)
        elif command == "prism":
            if "prism" in caughtdict.keys() and caughtdict["prism"] == "red":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Red Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Red Prism", color=discord.Color.from_rgb(255, 0, 0))
                embed.add_field(name=" ",value="The Red Prism will force only creatures of red light, and additionally Adamant Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :paintbrush: :label:")
                await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            elif "prism" in caughtdict.keys() and caughtdict["prism"] == "green":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Green Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Green Prism", color=discord.Color.from_rgb(0, 255, 0))
                embed.add_field(name=" ",value="The Green Prism will force only creatures of green light, and additionally Dazzling Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :cut_of_meat: :beans:")
                await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            elif "prism" in caughtdict.keys() and caughtdict["prism"] == "blue":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Blue Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Blue Prism", color=discord.Color.from_rgb(0, 0, 255))
                embed.add_field(name=" ",value="The Blue Prism will force only creatures of blue light, and additionally Iridescent Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :stopwatch: :compass:")
                await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            elif "prism" in caughtdict.keys() and caughtdict["prism"] == "black":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Original Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Original Prism", color=discord.Color.from_rgb(0, 0, 0))
                embed.add_field(name=" ",value="The Original Prism will force only creatures of black light, and additionally Mythic Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :scroll: :stew:")
                await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)

            else:
                await interaction.response.send_message(content="`$ "+command+"`\n"+"You have no active prism!")
        elif "rebuild " in command and not command == command.removeprefix("rebuild "):
            prism = command.removeprefix("rebuild ")
            if not "rebuild" in caughtdict["knowncommands"]:
                knowncommands = list(caughtdict["knowncommands"])
                knowncommands.extend(['rebuild'])
                print(knowncommands)
                caughtdict["knowncommands"] = knowncommands

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()
            if prism == "red":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Rebuilding the Red Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Rebuilding the Red Prism", color=discord.Color.from_rgb(255, 0, 0))
                embed.add_field(name=" ",value="Rebuilding the Red Prism will force only creatures of red light, and additionally Adamant Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :paintbrush: :label:\n \n**Required materials**\n<:mythicenergy:1080212197797539991>x5 <:redshard:1070017410205241374>x15\n\n**If there is any existing prism in effect, it will be destroyed.** You should remove it first with `$ remove`!")
                if "mythicenergy" in caughtdict.keys() and "redshard" in caughtdict.keys() and caughtdict["mythicenergy"] > 4 and caughtdict["redshard"] > 14:
                    if "att_rebuild" not in caughtdict.keys() or not caughtdict["att_rebuild"] == "red":
                        caughtdict["att_rebuild"] = "red"
                        embed.set_footer(text="Type this command again to confirm your decision!")
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
                    else:
                        caughtdict["prism"] = "red"
                        caughtdict["mythicenergy"] = caughtdict["mythicenergy"] - 5
                        caughtdict["redshard"] = caughtdict["redshard"] - 15
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n**The Red Prism was successfully rebuilt!**")
                else:
                    caughtdict["att_rebuild"] = "none"
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    embed.set_footer(text="Insufficient materials!")
                    await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            elif prism == "green":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Rebuilding the Green Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Rebuilding the Green Prism", color=discord.Color.from_rgb(0, 255, 0))
                embed.add_field(name=" ",value="Rebuilding the Green Prism will force only creatures of green light, and additionally Dazzling Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :cut_of_meat: :beans:\n \n**Required materials**\n<:mythicenergy:1080212197797539991>x5 <:greenshard:1070017427183771799>x15\n\n**If there is any existing prism in effect, it will be destroyed.** You should remove it first with `$ remove`!")
                if "mythicenergy" in caughtdict.keys() and "greenshard" in caughtdict.keys() and caughtdict["mythicenergy"] > 4 and caughtdict["greenshard"] > 14:
                    if "att_rebuild" not in caughtdict.keys() or not caughtdict["att_rebuild"] == "green":
                        caughtdict["att_rebuild"] = "green"
                        embed.set_footer(text="Type this command again to confirm your decision!")
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
                    else:
                        caughtdict["prism"] = "green"
                        caughtdict["mythicenergy"] = caughtdict["mythicenergy"] - 5
                        caughtdict["greenshard"] = caughtdict["greenshard"] - 15
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n**The Green Prism was successfully rebuilt!**")
                else:
                    caughtdict["att_rebuild"] = "none"
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    embed.set_footer(text="Insufficient materials!")
                    await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            elif prism == "blue":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Rebuilding the Blue Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Rebuilding the Blue Prism", color=discord.Color.from_rgb(0, 0, 255))
                embed.add_field(name=" ",value="Rebuilding the Blue Prism will force only creatures of blue light, and additionally Iridescent Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :stopwatch: :compass:\n \n**Required materials**\n<:mythicenergy:1080212197797539991>x5 <:blueshard:1070017442295840929>x15\n\n**If there is any existing prism in effect, it will be destroyed.** You should remove it first with `$ remove`!")
                if "mythicenergy" in caughtdict.keys() and "blueshard" in caughtdict.keys() and caughtdict["mythicenergy"] > 4 and caughtdict["blueshard"] > 14:
                    if "att_rebuild" not in caughtdict.keys() or not caughtdict["att_rebuild"] == "blue":
                        caughtdict["att_rebuild"] = "blue"
                        embed.set_footer(text="Type this command again to confirm your decision!")
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
                    else:
                        caughtdict["prism"] = "blue"
                        caughtdict["mythicenergy"] = caughtdict["mythicenergy"] - 5
                        caughtdict["blueshard"] = caughtdict["blueshard"] - 15
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n**The Blue Prism was successfully rebuilt!**")
                else:
                    caughtdict["att_rebuild"] = "none"
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    embed.set_footer(text="Insufficient materials!")
                    await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            elif prism == "black" or prism == "original":
                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="Rebuilding the Original Prism", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="Rebuilding the Original Prism", color=discord.Color.from_rgb(0, 0, 0))
                embed.add_field(name=" ",value="Rebuilding the Original Prism will force only creatures of black light, and additionally Mythic Prismalgams to appear from catching. Additionally, the only items that can be found when catching are: :scroll: :stew:\n \n**Required materials**\n<:mythicenergy:1080212197797539991>x5 <:blackshard:1071862902379790468>x15\n\n**If there is any existing prism in effect, it will be destroyed.** You should remove it first with `$ remove`!")
                if "mythicenergy" in caughtdict.keys() and "blackshard" in caughtdict.keys() and caughtdict["mythicenergy"] > 4 and caughtdict["blackshard"] > 14:
                    if "att_rebuild" not in caughtdict.keys() or not caughtdict["att_rebuild"] == "black":
                        caughtdict["att_rebuild"] = "black"
                        embed.set_footer(text="Type this command again to confirm your decision!")
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
                    else:
                        caughtdict["prism"] = "black"
                        caughtdict["mythicenergy"] = caughtdict["mythicenergy"] - 5
                        caughtdict["blackshard"] = caughtdict["blackshard"] - 15
                        with open(path, 'w') as convert_file:
                            convert_file.write(json.dumps(caughtdict))
                        print(caughtdict)
                        f.close()
                        await interaction.response.send_message(content="`$ "+command+"`\n**The Original Prism was successfully rebuilt!**")
                else:
                    caughtdict["att_rebuild"] = "none"
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()
                    embed.set_footer(text="Insufficient materials!")
                    await interaction.response.send_message(content="`$ "+command+"`\n",embed=embed)
            else:
                await interaction.response.send_message(content="`$ "+command+"`\nThis prism does not exist!", ephemeral=True)
        elif command == "alter":
            if (not "altercd" in caughtdict.keys()) or caughtdict["altercd"] < unix:
                caughtdict["guaranteedCreature"] = "strange"
                caughtdict["altercd"] = int(unix+1)
                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()
                await interaction.response.send_message("`$ "+command+"`\nYour next catch will be a *strange creature*...", ephemeral=True)
            else:
                await interaction.response.send_message("`$ "+command+"`\nYou are on cooldown! You can alter a catch again <t:"+str(caughtdict["altercd"])+":R>.", ephemeral=True)
        elif "dev " in command and not command == command.removeprefix("dev "):
            if interaction.user.id in specialprivileges:
                devcmd = command.removeprefix("dev ")
                if "ver " in devcmd and not devcmd == devcmd.removeprefix("ver "):
                    ver = devcmd.removeprefix("ver ")
                    with open("ver.txt", 'w') as convert_file:
                        convert_file.write(json.dumps({"ver": ver, "time": unix}))
                    f.close()
                    await interaction.response.send_message("Set ver to "+ver+".", ephemeral=True)
                elif devcmd == "pfp":
                    with open('pfp.png', 'rb') as pfp:
                        await client.user.edit(avatar=pfp.read())
                        await interaction.response.send_message("Set pfp.", ephemeral=True)
                elif devcmd == "testping":
                    await interaction.response.send_message("<@990710399043264524>")
                elif devcmd == "username":
                    await interaction.response.send_message(f"{interaction.user.global_name}")
                elif "getdata " in devcmd and not devcmd == devcmd.removeprefix("getdata "):
                    id = devcmd.removeprefix("getdata ")
                    if interaction.user.id in specialprivileges:
                        path = Path("./"+id+".txt")

                        if (path).is_file():

                            with open(path) as f:
                                data = f.read()
                            f.close()

                            message = str(ast.literal_eval(data))

                        else:
                            message = "This user has no data!"

                        await interaction.response.send_message(message)
                    else:
                        await interaction.response.send_message(random.choice(notdev), ephemeral=True)
                elif "setval " in devcmd and not devcmd == devcmd.removeprefix("setval ") and interaction.user.id in dev:
                    buffer = devcmd.removeprefix("setval ")

                    id = buffer[0:18]
                    buffer = buffer.removeprefix(buffer[0:18]+" ")

                    value_find = buffer.find(" ")
                    print(value_find)
                    if not value_find == -1:
                        value = buffer[0:int(value_find)]
                        buffer = buffer.removeprefix(buffer[0:int(value_find)])
                        buffer = buffer.replace(" ", "")
                        amount = int(buffer)


                        path = Path("./"+id+".txt")

                        if (path).is_file():

                            with open(path) as f:
                                data = f.read()
                            f.close()

                            caughtdict = ast.literal_eval(data)

                            caughtdict[value] = amount

                            with open(path, 'w') as convert_file:
                                convert_file.write(json.dumps(caughtdict))
                            print(caughtdict)
                            f.close()

                            await interaction.response.send_message("Set value of "+value+" for <@"+id+"> to "+str(amount)+".")
                        else:
                            await interaction.response.send_message("No file exists for this user.")

                    else:
                        await interaction.response.send_message("Insufficient parameters given. Format:\nsetval <user id> <value> <amount>")
                elif "remval " in devcmd and not devcmd == devcmd.removeprefix("remval ") and interaction.user.id in dev:
                    buffer = devcmd.removeprefix("remval ")

                    id = buffer[0:18]
                    buffer = buffer.removeprefix(buffer[0:18]+" ")

                    value_find = buffer.find(" ")
                    print(value_find)
                    if value_find == -1:
                        value = buffer

                        path = Path("./"+id+".txt")

                        if (path).is_file():

                            with open(path) as f:
                                data = f.read()
                            f.close()

                            caughtdict = ast.literal_eval(data)

                            if value in caughtdict.keys():
                                del caughtdict[value]

                                with open(path, 'w') as convert_file:
                                    convert_file.write(json.dumps(caughtdict))
                                print(caughtdict)
                                f.close()

                                await interaction.response.send_message("Removed "+value+" from <@"+id+">.")
                            else:
                                await interaction.response.send_message("Value "+'"'+value+'" not found on this user')
                        else:
                            await interaction.response.send_message("No file exists for this user.")

                    else:
                        await interaction.response.send_message("Insufficient parameters given. Format:\nremval <user id> <value>")
            else:
                await interaction.response.send_message(random.choice(notdev), ephemeral=True)
        elif command == "aqua":
            if not "aqua" in caughtdict.keys():
                caughtdict["aqua"] = {"animals": 0, "alt": 0}

            animals = caughtdict["aqua"]

            if "nextaqua" in animals.keys() and animals["nextaqua"] > unix:
                await interaction.response.send_message("`$ "+command+"`\nYou can dive again <t:"+str(animals["nextaqua"])+":R>.", ephemeral=True)
            else:
                if random.choice(range(1,8)) == 1:
                    gold = 1
                else:
                    gold = 0

                if gold == 1:
                    if "gold" in animals.keys():
                        animals["gold"] = animals["gold"] + 1
                    else:
                        animals["gold"] = 1
                    animals["nextaqua"] = unix+21600
                    caughtdict["aqua"] = animals
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    f.close()
                    
                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title="", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title="", color=discord.Color.from_rgb(255, 216, 0))

                    embed.add_field(name="", value="Oh? You "+random.choice(["went diving and found", "brought back", "brought home", "rescued"])+" a **"+random.choice(["<:goldfish:1081706696742797392> Gold Fish", "<:goldshark:1081706698395369522> Gold Shark", "<:goldwhale:1081706702489010236> Gold Whale", "<:goldsquid:1081706700005986404> Gold Squid", "<:goldcrab:1081706694754717797> Gold Crab"])+"**!?")
                    embed.set_footer(text="How lucky!! You can find another animal in 6 hours")

                    await interaction.response.send_message(content="`$ "+command+"`",embed=embed)
                else:
                    animals["animals"] = animals["animals"] + 1
                    animals["nextaqua"] = unix+21600
                    caughtdict["aqua"] = animals
                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    f.close()

                    if "embedR" in caughtdict.keys():
                        embed = discord.Embed(title="", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                    else:
                        embed = discord.Embed(title="", color=discord.Color.from_rgb(72, 169, 173))

                    embed.add_field(name="", value="You "+random.choice(["went diving and found", "brought back", "brought home", "rescued"])+" a **"+random.choice([":fish: Fish", ":shark: Shark", ":whale: Whale", ":squid: Squid", ":crab: Crab"])+"**!")
                    embed.set_footer(text="You can find another animal in 6 hours")

                    await interaction.response.send_message(content="`$ "+command+"`",embed=embed)
        elif command == "markiplier":
            view = Markiplier(interaction)

            await interaction.response.send_message("You is Markiplier\nYou want to make the videos\n \n:one: Yes\n:two: Fuck no", view=view)

            await view.wait()

            if view.value:
                await interaction.response.edit_message("You is Markiplier\nYou want to make the videos\n \n:one: Yes\n:two: Fuck no", view=None)

            else:
                await interaction.response.edit_message("You is not Markiplier\nYou want to make the videos\n \n:one: Yes\n:two: Fuck no", view=None)


        elif command == "altaqua":
            if not "aqua" in caughtdict.keys():
                caughtdict["aqua"] = {"animals": 0, "alt": 0}

            animals = caughtdict["aqua"]

            if "nextalt" in animals.keys() and animals["nextalt"] > unix:
                await interaction.response.send_message("`$ "+command+"`\nYou can dive again <t:"+str(animals["nextalt"])+":R>.", ephemeral=True)
            else:
                animals["alt"] = animals["alt"] + 1
                animals["nextalt"] = unix+86400
                caughtdict["aqua"] = animals

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                f.close()

                if "embedR" in caughtdict.keys():
                    embed = discord.Embed(title="", color=discord.Color.from_rgb(caughtdict["embedR"], caughtdict["embedG"], caughtdict["embedB"]))
                else:
                    embed = discord.Embed(title="", color=discord.Color.from_rgb(211, 52, 132))

                embed.add_field(name="", value="You "+random.choice(["went diving and found", "brought back", "brought home", "rescued"])+" an **"+random.choice(["<:alt_fish:1070437943371628564> Alt Fish", "<:alt_shark:1070438057297317953> Alt Shark", "<:alt_whale:1070438114167894127> Alt Whale", "<:alt_squid:1070437999692759050> Alt Squid", "<:alt_crab:1081347106016608327> Alt Crab"])+"**?!")
                embed.set_footer(text="You can find another alt animal in 24 hours")

                await interaction.response.send_message(content="`$ "+command+"`",embed=embed)

        elif "list" in command:
            if not "list" in caughtdict["knowncommands"]:
                knowncommands = list(caughtdict["knowncommands"])
                knowncommands.extend(['list'])
                print(knowncommands)
                caughtdict["knowncommands"] = knowncommands

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()
            if command == "list":
                att_userid = str(interaction.user.id)
                path = Path("./"+att_userid+".txt")
                if (path).is_file():
                    with open(path) as f:
                        data = f.read()
                    f.close()

                    caughtdict = ast.literal_eval(data)
                    animals = caughtdict["aqua"]

                    emojis = ""
                    if animals["animals"] > 99:
                        emojis = emojis+"👑 "
                    if animals["alt"] > 24:
                        emojis = emojis+"<:alt_crown:1082073824234844232> "
                    if "gold" in animals and animals["gold"] > 9:
                        emojis = emojis+"<:gold_crown:1082075014788038707> "
                    if att_userid == "705750043671658537":
                        emojis = emojis+"<:wither_crown:1082331845083017216> "
                    if "gamebreaker" in animals.keys():
                        emojis = emojis+"💣 "

                    listtitle = "The Aquarium:tm: "+emojis

                    embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(72, 169, 173))
                    embed.add_field(name="", value=":fish: **Animals:** "+str(animals["animals"]), inline=False)
                    embed.add_field(name="", value="<:alt_fish:1070437943371628564> **Alt Animals:** "+str(animals["alt"]), inline=False)
                    if "gold" in animals.keys() and animals["gold"] > 0:
                        embed.add_field(name="", value="<:goldfish:1081706696742797392> **Gold Animals:** "+str(animals["gold"]), inline=False)
                    if att_userid == "705750043671658537":
                        embed.add_field(name="", value=":bug: **Caterpillars:** "+str(random.choice(range(1,1000))), inline=False)

                    await interaction.response.send_message(embed=embed)

                else:
                    await interaction.response.send_message(content="`$ "+command+"`\nHow did you get this message")
            elif not command == command.removeprefix("list "):
                att_userid = command.removeprefix("list ")
                path = Path("./"+att_userid+".txt")
                if (path).is_file():
                    with open(path) as f:
                        data = f.read()
                    f.close()

                    caughtdict = ast.literal_eval(data)
                    animals = caughtdict["aqua"]

                    emojis = ""
                    if animals["animals"] > 99:
                        emojis = emojis+"👑 "
                    if animals["alt"] > 24:
                        emojis = emojis+"<:alt_crown:1082073824234844232> "
                    if "gold" in animals and animals["gold"] > 9:
                        emojis = emojis+"<:gold_crown:1082075014788038707> "
                    if att_userid == "705750043671658537":
                        emojis = emojis+"<:wither_crown:1082331845083017216> "
                    if "gamebreaker" in animals.keys():
                        emojis = emojis+"💣 "

                    listtitle = "The Aquarium:tm: "+emojis

                    embed = discord.Embed(title=listtitle, color=discord.Color.from_rgb(72, 169, 173))
                    embed.add_field(name="", value=":fish: **Animals:** "+str(animals["animals"]), inline=False)
                    embed.add_field(name="", value="<:alt_fish:1070437943371628564> **Alt Animals:** "+str(animals["alt"]), inline=False)
                    if "gold" in animals.keys() and animals["gold"] > 0:
                        embed.add_field(name="", value="<:goldfish:1081706696742797392> **Gold Animals:** "+str(animals["gold"]), inline=False)
                    if att_userid == "705750043671658537":
                        embed.add_field(name="", value=":bug: **Caterpillars:** "+str(random.choice(range(1,1000))), inline=False)

                    await interaction.response.send_message(embed=embed)

                    
                else:
                    await interaction.response.send_message(content="`$ "+command+"`\nThis user doesn't exist!", ephemeral=True)
            else:
                await interaction.response.send_message(content="`$ "+command+"`\nHow did you get this message")
        elif command == "dreams in":
            await interaction.response.send_message(content="`$ "+command+"`\n"+"Invalid syntax! Use `$ help dreams` for info on how to use this command.", ephemeral=True)

        elif command == "yomama":
            embed = discord.Embed(title="", color=discord.Color.from_rgb(255, 128, 0))
            embed.set_author(name="Creative Mode", icon_url="https://images-ext-1.discordapp.net/external/y2RU3-G6In5POF2sUIHxwlosyPsIz9XiVlw-owOBvZ4/https/cdn.discordapp.com/avatars/309104296362901505/b475e4533ec32f31e7369f65c670b52c.webp")
            embed.add_field(name="", value=":fox:\n`you could still put stuff here if a profile is private`", inline=False)
            embed.add_field(name="", value=":lock: This profile is **private**! Stats cannot be viewed.", inline=False)
            await interaction.response.send_message(embed=embed)

        elif command == "dreams":
            if "dream" in caughtdict.keys():
                dreamstate = "```\nDREAM STATE ("+caughtdict["dream"].upper()+")\n"

                if caughtdict["dream"] == "leez":
                    dreamstate += "- 82359\n- 14631\n- 72586"
                
                elif caughtdict["dream"] == "beth":
                    dreamstate += "- 51312\n- 68730"

                dreamstate += "\n\n(View a dream by typing its number into the terminal)\n```"

                await interaction.response.send_message(content=dreamstate, ephemeral=True)
            else:
                await interaction.response.send_message(content="`$ "+command+"`\nTo be able to view the dreams of a creature, you must first ENTER the dreams of a creature!\n Use `$ help dreams` for info on how to use this command.", ephemeral=True)
        
        elif command == "dreams out":
            if "dream" in caughtdict.keys():
                del caughtdict["dream"]

                with open(path, 'w') as convert_file:
                    convert_file.write(json.dumps(caughtdict))
                print(caughtdict)
                f.close()

                await interaction.response.send_message(content="`$ "+command+"`\nYou have returned from the dream state.", ephemeral=True)

            else:
                await interaction.response.send_message(content="`$ "+command+"`\nLook... I hate to break it to you, but you can't really leave a dream if you never entered one.", ephemeral=True)

        elif "dreams in " in command and not command == command.removeprefix("dreams in "):

            dreamtry = command.removeprefix("dreams in ")

            if dreamtry in creaturedata.keys():
                if dreamtry in ["leez", "beth"]:

                    caughtdict["dream"] = dreamtry

                    with open(path, 'w') as convert_file:
                        convert_file.write(json.dumps(caughtdict))
                    print(caughtdict)
                    f.close()

                    await interaction.response.send_message(content="`$ "+command+"`\n"+creaturedata[dreamtry]["emoji"]+"You have entered the dreams of your **"+creaturedata[dreamtry]["name"]+"**...", ephemeral=True)
            else:
                await interaction.response.send_message(content="`$ "+command+"`\nYou can only enter the dreams of a valid creature!", ephemeral=True)

        elif "dream" in caughtdict.keys() and command in valid_dreams[caughtdict["dream"]]:
            dream_message = "You broke the dream world... (this message should not appear)"
            if command == "82359":
                if "longlength" in caughtdict.keys() and caughtdict["longlength"] < 30:
                    caughtdict["longlength"] += 1
                else:
                    caughtdict["longlength"] = 1
            
                long = "<:longzrd_top:1041744470913327134>\n"

                for i in range(0, caughtdict["longlength"]):
                    long += "<:longzrd_middle:1041744099956494408>\n"
            
                long += "<:longzrd_bottom:1041744084517269545>"

                dream_message = long
            
            elif command == "14631":
                if "leez" in caughtdict.keys():
                    dream_message = str(math.floor(caughtdict["leez"]*1.6))
                else:
                    dream_message = "0"

            elif command == "72586":
                dream_message = "R1JFRU4gR1JFRU4gR1JFRU4gR1JFRU4gR1JFRU4gR1JFRU4gR1JFRU4gR1JFRU4gR1JFRU4="
            
            elif command == "51312":
                dream_message = "\\_/ \\ / \\\n<  |      |\n\\_\\ / \\ /"

            elif command == "68730":
                if random.choice([1,2]) == 1:
                    dream_message = "Beth"
                else:
                    dream_message = "Bryan"



            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
            f.close()

            await interaction.response.send_message(content=dream_message, ephemeral=True)

        else:
            await interaction.response.send_message(content="`$ "+command+"`\nNot recognised as a file or command.\n \n(If you're trying to access a directory, use `$ cd <directory>`, or `$ cd ..` to go up one folder. If you're trying to access a file or command, type its name.)")
    else:
        if "dream" in caughtdict.keys():
            await interaction.response.send_message("You need to leave the dream you are currently in first!\n`$ dreams out`", ephemeral=True)
        else:
            await interaction.response.send_message(random.choice(notrex), ephemeral=True)

@tree.command(name="sign", description="Sign a contract and remove a cooldown of your choice. Requires a contract.")
@app_commands.describe(cooldown='The cooldown being removed (catch, quest, etc.)')
async def test(interaction: discord.Interaction, cooldown: str):
    unix = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
    userid = str(interaction.user.id)
    path = Path("./"+userid+".txt")
    with open(path) as f:
        data = f.read()
    f.close()

    caughtdict = ast.literal_eval(data)
    if "contract" in caughtdict.keys():
        if caughtdict["contract"] == 0:
            await interaction.response.send_message(random.choice(noitems), ephemeral=True)
        else:
            if cooldown == "catch" and caughtdict["next"] > unix:
                caughtdict["contract"] = caughtdict["contract"] - 1
                caughtdict["next"] = 0
            elif cooldown == "quest" and "questend" in caughtdict.keys() and caughtdict["questend"] > unix:
                caughtdict["contract"] = caughtdict["contract"] - 1
                caughtdict["questend"] = 0
            elif cooldown == "alter" and "altercd" in caughtdict.keys() and caughtdict["altercd"] > unix:
                caughtdict["contract"] = caughtdict["contract"] - 1
                caughtdict["altercd"] = 0
            elif cooldown == "aqua" and "aqua" in caughtdict.keys() and "nextaqua" in caughtdict and caughtdict["aqua"]["nextaqua"] <= unix:
                caughtdict["contract"] = caughtdict["contract"] - 1
                caughtdict["aqua"]["nextaqua"] = 0
            elif cooldown == "altaqua" and "aqua" in caughtdict.keys() and "nextalt" in caughtdict and caughtdict["aqua"]["nextalt"] <= unix:
                caughtdict["contract"] = caughtdict["contract"] - 1
                caughtdict["aqua"]["nextalt"] = 0
            else:
                await interaction.response.send_message("Could not remove cooldown! Make sure you type the name of an existing cooldown. (catch, quest, etc.)", ephemeral=True)
            
            with open(path, 'w') as convert_file:
                convert_file.write(json.dumps(caughtdict))
            print(caughtdict)
            f.close()

            await interaction.response.send_message("**Removed cooldown **("+cooldown+")**!**")

    else:
        await interaction.response.send_message(random.choice(noitems), ephemeral=True)

class Markiplier(discord.ui.View):
    def __init__(self, inter: discord.Interaction, timeout: float = 240.0):
        super().__init__(timeout=timeout)
        self.inter = inter
        self.value = None

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)
    async def confirm_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()
        await interaction.response.send_message(content="")
    
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)
    async def cancel_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = False
        self.stop()
        await interaction.response.send_message(content="")
    
    async def  interaction_check(self, interaction: discord.Interaction, /) -> bool:
        if self.inter.user.id == interaction.user.id: 
            return True
        else: # not the intended user.
            await interaction.response.send_message("That's not your fucking button", ephemeral=True)
            return False
    
    async def on_timeout(self) -> Optional[float]:
        for child in self.children:
            if isinstance(child, discord.ui.Button):
                child.disabled = True

        await self.inter.edit_original_response(view=self)


@tree.command(name="feces", description="fecal matter")
async def test(interaction: discord.Interaction):
    embed = discord.Embed(title="", color=discord.Color.from_rgb(255, 128, 0))
    embed.add_field(name="", value="**Legacy Polar Star**\nObtained the Polar Star cosmetic from the original /rank method before Polaris was shut down in May 2024.")

    await interaction.response.send_message(embed=embed)

client.run(TOKEN)