from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot 
novo = ChatBot('Test')
ref_arquivo = open("/media/yane/Karol/pendrive.py", "r")
string_arquivo = ref_arquivo.readlines()
conv = ['oi', 'ola','quero atendimento', 'o que você deseja fazer hoje?', 'quero consultar um atendente', 'ok, vamos te ligar' ,'obrigada!', 'tenha um bom dia!']
novo.set_trainer(ListTrainer)
novo.train(conv)
quest = ""
for i in range(4):
    quest = string_arquivo[i]
    print('Você: ', quest)
    response = novo.get_response(quest)
    print('Bot: ', response)

