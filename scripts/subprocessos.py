from subprocess import PIPE,Popen
p1 = Popen(["python3", "bot.py"], stdin=PIPE,stdout=PIPE, bufsize=1)
p2 = Popen(["python3", "filmes.py"], stdin=PIPE,stdout=PIPE, bufsize=1)
