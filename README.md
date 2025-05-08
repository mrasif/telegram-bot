# telegram-bot

Telegram bot backend written using python. It has integration with Artificial Intelligence.

## Deployment

To deploy the Telegram bot, follow these steps:

1. **Set up environment variables**:
   Ensure you have the necessary environment variables configured. Create a `.env` file in the root directory and add the following:

2. **Deployment**:
   - Activate the virtual environment:
     ```sh
     source .venv/bin/activate
     ```
   - Run the bot:
     ```sh
     python bot.py
     ```

3. **Domain**:
   - Need to attach public domain.


## Docker compose based deployment

- Create `docker-compose.yaml`

```yaml
version: "3.8"
services:
  telegram:
    image: ghcr.io/mrasif/telegram-bot
    container_name: telegram-bot
    restart: unless-stopped
    env_file: .env
    ports:
      - 3000:3000
networks: {}
```

- Run `docker-compose up -d`
