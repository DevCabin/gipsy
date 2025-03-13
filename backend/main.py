from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import openai
from notion_client import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_TOKEN"))
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

class ChatRequest(BaseModel):
    message: str
    use_notion: bool = False

class ChatResponse(BaseModel):
    response: str
    notion_saved: bool = False

def write_to_notion(content: str) -> bool:
    try:
        notion.blocks.children.append(
            block_id=NOTION_PAGE_ID,
            children=[{
                "object": "block",
                "type": "paragraph",
                "paragraph": {"text": [{"type": "text", "text": {"content": content}}]}
            }]
        )
        return True
    except Exception as e:
        print(f"Error writing to Notion: {e}")
        return False

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Get response from OpenAI
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": request.message}]
        )
        
        chat_response = response.choices[0].message.content
        notion_saved = False
        
        # Save to Notion if requested
        if request.use_notion:
            notion_saved = write_to_notion(chat_response)
        
        return ChatResponse(response=chat_response, notion_saved=notion_saved)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"} 