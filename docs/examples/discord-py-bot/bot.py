import os
import discord
from discord.ext import commands
from discord import app_commands
import openai
from dotenv import load_dotenv
import logging
import re

# Basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Perplexity client
perplexity_client = openai.OpenAI(
    api_key=PERPLEXITY_API_KEY,
    base_url="https://api.perplexity.ai"
) if PERPLEXITY_API_KEY else None

@bot.event
async def on_ready():
    """Bot startup"""
    logger.info(f"Bot {bot.user} is ready!")
    await bot.tree.sync()
    logger.info("Commands synced")

@bot.tree.command(name="ask", description="Ask Perplexity AI a question")
@app_commands.describe(question="Your question")
async def ask(interaction: discord.Interaction, question: str):
    """Ask Perplexity AI a question"""
    if not perplexity_client:
        await interaction.response.send_message("❌ Perplexity AI not configured", ephemeral=True)
        return

    await interaction.response.defer()
    
    try:
        response = perplexity_client.chat.completions.create(
            model="sonar-pro",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful AI assistant. Provide clear, accurate answers with citations."
                },
                {"role": "user", "content": question}
            ],
            max_tokens=2000,
            temperature=0.2
        )
        
        answer = response.choices[0].message.content
        formatted_answer = format_citations(answer, response)
        
        # Truncate if too long
        if len(formatted_answer) > 2000:
            formatted_answer = formatted_answer[:1997] + "..."
        
        await interaction.followup.send(formatted_answer)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        await interaction.followup.send("❌ Sorry, an error occurred. Please try again.", ephemeral=True)

@bot.event
async def on_message(message):
    """Handle mentions"""
    if message.author == bot.user or message.author.bot:
        return
    
    # Check if bot is mentioned
    if bot.user in message.mentions and perplexity_client:
        # Remove mention from content
        content = message.content.replace(f'<@{bot.user.id}>', '').replace(f'<@!{bot.user.id}>', '').strip()
        
        if not content:
            await message.reply("Hello! Ask me any question.")
            return
        
        async with message.channel.typing():
            try:
                response = perplexity_client.chat.completions.create(
                    model="sonar-pro",
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are a helpful AI assistant. Provide clear, accurate answers with citations."
                        },
                        {"role": "user", "content": content}
                    ],
                    max_tokens=2000,
                    temperature=0.2
                )
                
                answer = response.choices[0].message.content
                formatted_answer = format_citations(answer, response)
                
                # Truncate if too long
                if len(formatted_answer) > 2000:
                    formatted_answer = formatted_answer[:1997] + "..."
                
                await message.reply(formatted_answer)
                
            except Exception as e:
                logger.error(f"Error: {e}")
                await message.reply("❌ Sorry, an error occurred. Please try again.")
    
    await bot.process_commands(message)

def format_citations(text: str, response_obj) -> str:
    """Simple citation formatting that actually works"""
    # Get search results from response
    search_results = []
    
    if hasattr(response_obj, 'search_results') and response_obj.search_results:
        search_results = response_obj.search_results
    elif hasattr(response_obj, 'model_dump'):
        dumped = response_obj.model_dump()
        search_results = dumped.get('search_results', [])
    
    if not search_results:
        return text
    
    # Find existing citations like [1], [2], etc.
    citation_pattern = r'\[(\d+)\]'
    citations = re.findall(citation_pattern, text)
    
    if citations:
        # Replace existing citations with clickable links
        def replace_citation(match):
            num = int(match.group(1))
            idx = num - 1
            
            if 0 <= idx < len(search_results):
                result = search_results[idx]
                
                # Extract URL from search result
                url = ""
                if isinstance(result, dict):
                    url = result.get('url', '')
                elif hasattr(result, 'url'):
                    url = result.url
                
                if url:
                    return f"[[{num}]](<{url}>)"
            
            return f"[{num}]"
        
        text = re.sub(citation_pattern, replace_citation, text)
    else:
        # No citations in text, add them at the end
        citations_list = []
        for i, result in enumerate(search_results[:5]):  # Limit to 5
            url = ""
            if isinstance(result, dict):
                url = result.get('url', '')
            elif hasattr(result, 'url'):
                url = result.url
            
            if url:
                citations_list.append(f"[[{i+1}]](<{url}>)")
        
        if citations_list:
            text += "\n\n**Sources:** " + " ".join(citations_list)
    
    return text

if __name__ == "__main__":
    if not DISCORD_TOKEN or not PERPLEXITY_API_KEY:
        print("❌ Missing DISCORD_TOKEN or PERPLEXITY_API_KEY in .env file")
    else:
        bot.run(DISCORD_TOKEN)