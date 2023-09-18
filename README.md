# NBA API Discord Bot README
## Add bot to your Discord server
To add this bot to your Discord server, follow the link here: https://discord.com/api/oauth2/authorize?client_id=1146552831487254579&permissions=8&scope=bot

## Run bot on local machine
To run the bot from your local machine, head over to the developer portal and create a new application: https://discord.com/developers/applications

Next, click on the 'OAuth2' tab on the left, and click on 'General'. 

From there, checkmark the 'bot' box, then choose the bot permissions (bot is only capable of sending messages, but feel free to customize this as you desire).

After you save changes, click on the 'URL Generator' tab under 'OAuth2' and under 'scopes' checkmark the 'bot' box.

From there, choose the bot permissions (can only send messages but feel free to customize).

After, you will get the Generated URL at the bottom, which is the bot invite link. Save this link so you can invite the bot to your server.

Next, head over to the 'Bot' tab on the left and click on 'Add Bot'.

From there, you will need to generate a token. On the 'Bot' tab, click on the 'Reset Token' button to generate your token.

![image](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/4d3806d5-0e79-4179-8307-44605de7bcb3)

After you get your token, you will have to go to the file 'bot.py' and, on line 29, replace 'Token' with your string token.

Next, you will need to install the following packages through the terminal (assuming you already have Python/pip installed):

```python -m pip install requests```

```pip install numpy```

```pip install pandas```

```pip install nba_api```

```pip install discord.py```

Lastly, you will need to update the sys.paths on the files in the cogs folder to the path where the NBA Discord API Bot is located.

Finally, head over to 'bot.py' and run the file to get your bot running. To stop the bot, set your cursor in the terminal and click 'control c'.

## Features
#### Get an NBA player's stats from most recent/current season.
![!find](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/caac115e-54d3-4fa5-aff4-c2c4cea27ffb)

#### Get an NBA player's awards they have won throughout their entire career.
![!awards](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/af8d4ae9-f5ff-448b-b8e9-9da4e5d27e8e)

#### Get an NBA player's advanced stats from most recent/current season.
![!advanced](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/bdfe4fb7-e483-4619-b8ad-29499a4a60b3)

#### Get the upcoming 2023-2034 NBA Finals winner prediction based on pre-season stats.
![!predict](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/97fed2e3-e3b8-47a7-b72f-cbd2ac4a5314)

#### Get an NBA player's recent shooting performances against any given team.
![!oppshot](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/5f3e83be-1b1b-4523-a109-1e8f1166b7bf)

#### Compare two NBA player's career awards and career stats.
![!compare](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/4c6eac02-a7d1-4092-a158-1925556b3348)

#### Get an NBA player's career stats.
![!career](https://github.com/mattfrench1/NBA-Discord-API-Bot/assets/114099168/73308818-7e35-43b4-98b9-0695bbfa5d1c)

## Future updates
+ Add a live NBA finals/regular season MVP predictor as the seasons starts.
+ Add more advanced metrics.

