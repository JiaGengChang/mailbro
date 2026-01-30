<p align="center"><img src="./logo.png" alt="MailBro Logo" width="600px" /></p>

# MailBro: API to send emails

Tired of being on the receiving end of spam mails? Use **antispam** to spam them back.

antispam is a barebones FastAPI application that sends pre-configured or user-specified emails to a list of addresses.

## Use Cases

- Spam back emails that are spamming you
- Test if your mail server is working
- Send emails using API requests

## Requirements

- A mail server to send emails (e.g., Google: `smtp.gmail.com`)
- Environment variables: `MAIL_USERNAME`, `MAIL_PASSWORD` for the mail server

## Setup Instructions

1. Provide a list of whitelisted keys in `apikeys.txt`
2. Build the container: `docker build -t antispam .`
3. Deploy on the cloud with environment variables: `MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_SERVER`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/docs` | Usage guide |
| POST | `/send` | Send emails - specify recipient, header, and body |
| POST | `/configure` | Create template email - specify recipient, header, and body |
| POST | `/send_preconfigured` | Send template email |

## License

This project is licensed under the [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).