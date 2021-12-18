class RuleSet(object):

    def __init__(self, moves):
        self.moves = moves
        pass

    def match(self, player, cpu):
        threshold = len(self.moves)/2
        if(player < cpu and cpu <= player + threshold or
           player > cpu and cpu < player - threshold):
            return -1
        elif(player == cpu):
            return 0;
        else:
            return 1;
