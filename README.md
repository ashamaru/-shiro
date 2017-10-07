# •shiro #
## Discord bot in Python ##
The used Pythonframework is [discord.py](https://github.com/Rapptz/discord.py).  
You can find more information about developing with discord on [discord's dev docs](https://discordapp.com/developers/docs/intro).

## Creating the bot and adding to the server ##
From [here]() navigate to 'My Apps' and log into your account.  
Afterwards you should see the possibility to create a new App, do that.  
Choose a name, but be wary of picture... (firefox death trap on my comp).
Upon success select 'Create Bot User'.  
Something like that should appear:  
`Great Success!
A wild bot has appeared!`  
You are almost done.  
You can use this link to connect the bot with your server, but before simply replace <Bot ID> with your app's client id.  
  `https://discordapp.com/oauth2/authorize?client_id=<Bot ID>&scope=bot`.  
  Select the server and click 'Authorize', ipon success you should see your bot at the server.  
  You need to be admin or have the Manage Server rights thou.  
  Further keep your bot token secret, you will use it in your code to connect to discord as the bot client.  
  You can copy and paste a code template from [discord.py's](https://github.com/Rapptz/discord.py) readme.

## Python and virtual environments ##
For personal development as a Phyton dev, use virtual environments is recommended. It isn't as much as a hassle as it sounds thou, but rather gives you more flexibility while working with python. A short, simple but useful introduction from the official python docs/tutorial: [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html). Because it's wasn't mentioned, to exit from the venv on the terminal, simply type `deactivate`, a command added by the <venv>/bin/activate script.
