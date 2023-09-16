# NBA API Discord Bot README
## Add bot to your Discord server
To add this bot to your Discord server, follow the link here: https://discord.com/api/oauth2/authorize?client_id=1146552831487254579&permissions=8&scope=bot

## Run bot on local machine
To run the bot from your local machine, head over to the developer portal and create a new application: https://discord.com/developers/applications

From there, you will need to generate a token. Click on the 'Bot' tab on the left, and there should be a button to reset/create token.

![image](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/4d3806d5-0e79-4179-8307-44605de7bcb3)

After you get your token, you will have to go to the file 'bot.py' and, on line 29, replace 'Token' with your string token.

Next, you will need to install the following packages through the terminal (assuming you already have Python/pip installed):

```python -m pip install requests```

```pip install numpy```

```pip install pandas```

```pip install nba_api```

Lastly, you will need to update the sys.paths on the files in the cogs folder to the path where the NBA Discord API Bot is located.

Finally, head over to 'bot.py' and run the file to get your bot running. To stop the bot, set your cursor in the terminal and click 'control c'.

## Features
#### Get an NBA player's stats from most recent/current season.
#### Get an NBA player's awards they have won throughout their entire career.
#### Get an NBA player's advanced stats from most recent/current season.
#### Get the upcoming 2023-2034 NBA Finals winner prediction based on pre-season stats.
#### Get an NBA player's recent shooting performances against any given team.
#### Compare two NBA player's career awards and career stats.
#### Get an NBA player's career stats.


## Future updates
+ Add a live NBA finals/regular season MVP predictor as the seasons starts.
+ Add more advanced metrics.

