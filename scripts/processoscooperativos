from subprocess import PIPE, Popen
p1 = Popen(["python3", "bot.py"], stdin=PIPE,stdout=PIPE, bufsize=1)
p2 = Popen(["python3", "filmes.py"], stdin=PIPE,stdout=PIPE, bufsize=1)

print('imprimir uma linha do processo filho:')
print p1.stdout.readline()
print p2.stdout.readline()
while True:
	print True
