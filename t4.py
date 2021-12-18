import helptable
import ruleset
import roundsession
import secrets
import sys

def showHelp(hint):
    for i in range(len(hint.helpTable)):
        for j in range(len(hint.helpTable)):
            print(hint.helpTable[i][j] + " ", end = '')
        print()
    print()

def showAvailableMoves(moves):
    print("Available moves:")
    for i in range(len(moves)):
        print(str(i + 1) + " - " + moves[i])
    print("0 - exit\n? - help")

def showHMACkey(session):
    print("HMAC key:\n" + session.key)

def showHMAC(session):
    print("HMAC:\n" + session.hmac)

def checkInput(userInput, moves):
    validOptions = []
    for i in range(len(moves)):
        validOptions.append(str(i + 1))
    validOptions.append("?")
    validOptions.append("0")
    return userInput in validOptions

def showResult(player, cpu, rules):
    result = ["You Lose", "A Draw", "You Win"]
    print("Your move: " + rules.moves[player])
    print("Computer move: " + rules.moves[cpu])
    print(result[rules.match(player, cpu) + 1])

def showResponse(player, cpu, rules, hint, session):
    match player:
        case "0":
            return False
        case "?":
            showHelp(hint)
        case _:
            showResult(int(player) - 1, cpu, rules)
            showHMACkey(session)
    print()
    return True
                    
def play(moves, rules, hint):
    while True:
        cpuMove = secrets.randbelow(len(moves))
        session = roundsession.RoundSession(moves[cpuMove])
        userInput = ""
        while True:
            showHMAC(session)
            showAvailableMoves(moves)
            userInput = input()
            if(checkInput(userInput, moves)):
                break
            else:
                print("Invalid input, please choose one of the available moves\n")
        if(not showResponse(userInput, cpuMove, rules, hint, session)):
            break

def checkArgs(args):
    errorMsg = ", please type in an uneven\n \
     number of unique arguments equal to or larger than 3, for example:\n \
     python t4.py rock paper scissors\n \
     python t4.py 1 2 3 4 5\n \
     python t4.py A B C D E F G"
    if(len(args) < 3):
        print("Error: not enough arguments" + errorMsg)
        sys.exit()
    if(len(args) % 2 == 0):
        print("Error: even number of arguments" + errorMsg)
        sys.exit()
    if(len(set(args)) < len(args)):
        print("Error: duplicate arguments" + errorMsg)
        sys.exit()

moves = []
for i in range(len(sys.argv) - 1):
    moves.append(sys.argv[i + 1])
checkArgs(moves)
rules = ruleset.RuleSet(moves)
hint = helptable.HelpTable(rules)
play(moves, rules, hint)


