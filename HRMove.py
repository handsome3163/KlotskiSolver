from HRConsts import DIR_NAMES
from HRException import InvalidMove

class HRMove:
    def __init__(self, piece, dir):
        self.piece = piece
        self.dir = dir
        self.tried = False
        self.applied = False
    def __repr__(self):
        ret_str = '#{0}'.format(self.piece.id)
        for d in self.dir:
            ret_str += ' {0}'.format(DIR_NAMES[d])
        return ret_str
        #'#{0} {1}'.format(self.piece.id, DIR_NAMES[self.dir])

    def apply(self):
        if not self.tried:
            for d in self.dir:
                self.piece.x += d[0]
                self.piece.y += d[1]
            self.tried = True
        self.applied = True

    def attempt(self):
        if self.tried and self.applied: raise InvalidMove
        for d in self.dir:
            self.piece.x += d[0]
            self.piece.y += d[1]
        self.tried = True

    def cancel(self):
        if self.applied or not self.tried: raise InvalidMove

        for d in reversed(self.dir):
            self.piece.x -= d[0]
            self.piece.y -= d[1]
        self.tried = False