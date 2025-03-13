# Gipsy - AI Chat with Notion Integration

A modern chat application that integrates with OpenAI's GPT-4 and optionally saves conversations to Notion.

## Features

- Real-time chat interface with GPT-4
- Optional Notion integration for saving conversations
- Modern, minimalistic UI inspired by ChatGPT
- FastAPI backend for reliable performance
- Next.js frontend for smooth user experience

## Deployment Status

🚀 Live Demo: [Frontend](https://gipsy-frontend.vercel.app) | [Backend](https://gipsy-api.vercel.app)

## Deployment

This project is configured for deployment on Vercel. The application consists of two parts:

1. Frontend (Next.js)
2. Backend (FastAPI)

### Environment Variables

The following environment variables need to be set in your Vercel project settings:

#### Frontend
- `NEXT_PUBLIC_API_URL`: URL of your deployed backend API

#### Backend
- `OPENAI_API_KEY`: Your OpenAI API key
- `NOTION_API_TOKEN`: Your Notion API token
- `NOTION_PAGE_ID`: The ID of the Notion page to save conversations to

### Deployment Steps

1. Fork this repository
2. Create two new projects on Vercel:
   - One for the frontend (point to the `frontend` directory)
   - One for the backend (point to the `backend` directory)
3. Configure the environment variables in both Vercel projects
4. Deploy!

## Development

This project is designed for deployment on Vercel without requiring local development. However, if you need to make changes:

1. Make your changes in the appropriate directory (frontend or backend)
2. Commit and push to your fork
3. Vercel will automatically deploy the changes

## License

MIT 