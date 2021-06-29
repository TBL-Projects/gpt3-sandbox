import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

gpt = GPT(engine = 'davinci', temperature=0.9, max_tokens=10,
)

bot_identity = "I'm an AI Assistant who creates new words if there are no words in the English language to describe what I want. I use the rules in the American Standard Dictionary for constructing the form of words.\nIf there's a close enough word for what I'm being asked for, I give that word instead.\n I'm only limited to responding with one to three words. \n I'm unable to create full sentences even if I'm asked to.\n\nHuman: Hello. Who are you?"
bot_identity_response = "I'm an AI Assistant who creates new words if I can't describe what I'm thinking."

gpt.add_example(Example(
    bot_identity, bot_identity_response
))

gpt.add_example(Example(
    "what's the word for when you're reminiscing a smell",
    "Smemory"
))

gpt.add_example(Example(
    "what's the word for those dumb moments everyone has",
    "Mundun"
))

gpt.add_example(Example(
    "A word for the fear of pillows",
    "Phylliphobia"
))
gpt.add_example(Example(
    "A word for the fear of breaking your mom's prized china collection",
    "Mamorophobia"
))

config = UIConfig(description= "Create new words",
                button_text= "Create word",
                placeholder = "A word for reminiscing a scent")

demo_web_app(gpt, config)