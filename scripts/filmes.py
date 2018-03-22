from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot('Test')

convfilmes = ['Hey, qual seu filme preferido?', 'Eu adoro o filme Meu Malvado favorito!','Eu também!', 'Já assistiu Harry Potter?Eu amo Harry Potter!', 'Jaaa! Eu amo Harry Potter!']
bot.set_trainer(ListTrainer)
bot.train(convfilmes)
while(True):
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot: ', response)
