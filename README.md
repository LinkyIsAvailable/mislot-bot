# mislot-bot

# Assistance Bot Discord

This is a disnake Discord bot. It lets users easily search for information on various services (employment, housing, training, mobility, health) in their department in France. The main code is based in french language, you can edit it on yours if you want to.

## Features 

- Interactive user interface with drop-down menu
- Search by service category
- Personalized department entry
- Clearly structured results
- Access restricted to authorized servers only

## Commands available 

### `/request
The only command available to :
1. Select a category from the drop-down menu:
   - Employment
   - Housing
   - Training
   - Mobility
   - Health
2. Enter the desired department
3. Receive relevant results with links

## Prerequisites 

- Python 3.8 or higher
- Libraries required :
  ```
  disnake
  tavily
  ```

## Installation 

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the variables in the code:
   - Replace `AUTHORIZED_SERVERS` with your server IDs
   - Update the Discord bot token
   - Configure your Tavily API key

## Configuration 

### Important variables to configure :

1. List of authorized servers:
```python
AUTHORIZED_SERVERS = [
    YOUR_SERVER_ID_1,
    YOUR_SERVER_ID_2
]
```

2. Discord bot token:
```python
bot.run(“YOUR_TOKEN_BOT”)
```

3. Tavily API key :
```python
client = TavilyClient(api_key=“VOTRE_CLE_API_TAVILY”)
```

## Usage

1. Invite the bot to your Discord server
2. Use the `/request` command
3. Select a category from the drop-down menu
4. Enter your department in the window that opens
5. The bot will send you the relevant results

## Results structure 

Results are presented as a Discord embed containing:
- A title indicating category and department
- Up to 5 most relevant results
- For each result :
  - The title
  - A description
  - A link to the source

## Security 

- The bot only works on authorized servers
- Interactions are limited to 5 minutes (timeout)
- Error messages are sent privately (ephemeral)

## Contribution 

Feel free to contribute to the project by:
1. Fork the repository
2. Creating a new branch
3. Commit your changes
4. Push on your fork
5. Create a pull request

## License 

This project is licensed under the MIT license. See the LICENSE file for more details.

## Support 

If you have any questions or problems, please feel free to open an issue on GitHub.
