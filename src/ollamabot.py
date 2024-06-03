import ollama


"""Music player manager"""
class Ollamabot:
    def __init__(self, bot, ollama):
      self.bot = bot  # bot main object
      self.ollama = ollama
    
    async def ask(self, ctx, msg):
        response = self.ollama.chat(model='llama2', messages=[
          {
            'role': 'user',
            'content': msg,
          },
        ])
        
        await ctx.send(response['message']['content'])