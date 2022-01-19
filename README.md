# discord-glyphbot
sample code to detect homoglyphed names in discord

additional info on the issue of homoglyphs:
https://twitter.com/Danny_one_/status/1461365315057553410

this code only warns admins/mods via the discord assigned system channel (wherever you receive discord official communications). a bot operator can add desired action such as assigning a particular role for action, forcing a new nick (e.g. "potential scammer"), kicking, or banning.

requires:
- homoglyphs_fork
- nest_asyncio
- asyncio
- discord
