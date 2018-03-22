from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot('Test')

conv = ['Oi', 'olá']
bot.set_trainer(ListTrainer)
bot.train(conv)
while(True):
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot: ', response)
