def rec(s):
    if not s:
        return 0
    else:
        if s.pop() == 'f':
            return rec(s) + 1
        else:
            return rec(s) - 1
string = input('Digite a movimentacao do robo: ')
move = rec(list(string))
if move > 0:
	print("Robo andou %d para frente" % move)
elif move == 0:
	print("Robo nao andou nada")
else:
	print("Robo andou %d para trás" % abs(move))
