from chatterbot.trainers import ListTrainer
from chatterbot.chatterbot import ChatBot
bot = ChatBot(
    'ARISTOTLE',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',])

Tell = input("Input numbers to sum.Format(a+b) ")
response = bot.get_response(Tell)
print(response)

