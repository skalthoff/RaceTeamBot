# WWU Sailing Team Discord Bot

This Discord bot is designed to help manage the logistics of the WWU Sailing Team. The bot features a modular architecture, allowing you to easily add new functionality as needed. It's built using the `discord.py` library and requires Python 3.7+.

## Features

- Easily create custom modules for added functionality.
- Example modules:
  - Attendance check: Sends a message with a description and allows users to react with check (✅) and cross (❌) emojis to indicate their attendance at practice.

## Installation

1. Install Python 3.7+ if you haven't already.
2. Clone this repository or download it as a ZIP file.
3. Open a terminal/command prompt and navigate to the project directory.
4. Install the required dependencies:

   ```
   pip install discord.py
   ```

5. Set up a Discord bot and obtain its token. Follow the instructions in the [official Discord.py guide](https://discordpy.readthedocs.io/en/stable/discord.html) to create a bot and invite it to your server.
6. Open `Raceteambot.py` and replace `YOUR_DISCORD_BOT_TOKEN` with your actual Discord bot token.

## Usage

To run the bot:

```
python Raceteambot.py
```

The bot will log in to your Discord server and be ready to use.

### Commands

- `!ping`: Test command that replies with "Pong!".
- `!create_attendance <description>`: Sends an embed message with the given description, and adds check (✅) and cross (❌) reactions for users to indicate their attendance at practice.

## Adding Custom Modules

1. Create a new Python file inside the `modules` folder, e.g., `my_module.py`.
2. Define your module as a class that inherits from `commands.Cog`, and include a constructor that accepts a `bot` argument.
3. Add any commands or event listeners as methods of your module class, using decorators from the `commands` module.
4. Define a `setup` function at the bottom of your file that accepts a `bot` argument, creates an instance of your module class, and adds it to the bot using `bot.add_cog()`.
5. Restart your bot to load the new module.

Refer to the provided example module `attendance.py` for an example of how to structure your custom module.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
