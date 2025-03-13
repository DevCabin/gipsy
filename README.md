# Gipsy - AI Chat with Notion Integration

A modern chat application that integrates with OpenAI's GPT-4 and optionally saves conversations to Notion.

## Features

- Real-time chat interface with GPT-4
- Optional Notion integration for saving conversations
- Modern, minimalistic UI inspired by ChatGPT
- FastAPI backend for reliable performance
- Next.js frontend for smooth user experience

## Setup

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_key
NOTION_API_TOKEN=your_notion_token
NOTION_PAGE_ID=your_notion_page_id
```

4. Run the backend:
```bash
cd backend
uvicorn main:app --reload
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run dev
```

## Development

- Backend runs on `http://localhost:8000`
- Frontend runs on `http://localhost:3000`
- API documentation available at `http://localhost:8000/docs`

## Deployment

This project is configured for deployment on Vercel. Simply push to your GitHub repository and connect it to Vercel for automatic deployments.

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `NOTION_API_TOKEN`: Your Notion API token
- `NOTION_PAGE_ID`: The ID of the Notion page to save conversations to

## License

MIT 