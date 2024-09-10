"""
Schreiben Sie ein Programm, das das Spiel "Tic, Tac, Toe" zu spielen erlaubt.

"Tic, Tac, Toe" ist ein Spiel für zwei Personen, wie z.B. in diesem Artikel der
deutschen Wikipedia beschrieben: https://de.wikipedia.org/wiki/Tic-Tac-Toe.

Diese Implementierung geht von zwei spielenden Personen aus, deren Spielzüge
abwechselnd erfragt und dann in der Logik des Spiels umgesetzt werden. Ein Spiel
besteht aus einer beliebigen Zahl von einzelnen Durchgängen, die jeweils mit einem
leeren Spielfeld beginnen. Ein Durchgang endet, wenn eine der spielenden Personen
zuerst drei ihrer Spielsymbole ("Spielsteine") in einer Senkrechten, Waagerechten
oder Diagonale des Spielfeldes setzen kann, oder das Spielfeld vollständig besetzt
ist, ohne dass eine Senkrechte, Waagerechte oder Diagonale mit drei gleichen
Spielsteinen belegt wurde.

Das Spielbrett besteht aus neun Feldern in drei Reihen mit je drei Feldern und kann
etwa so dargestellt werden, wobei die Felder von 1 bis 9 nummeriert werden.

    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9

Ein mit einer Ziffer markiertes Feld gilt als leer. Als Spielzug kann eine der im Feld
noch verbliebenen Ziffern von der Person, die gerade am Zug ist, eingegeben werden.

Ein mit einem der Spielsymbole (O oder X) markiertes Feld gilt als belegt, und kann
während des laufenden Durchganges nicht mehr geändert werden.

Nachdem jede der beiden spielenden Personen einen Spielzug durchlaufen hat, könnte das
Spielbrett zum Beispiel wie folgt aussehen:

    1 | 2 | X
    4 | O | 6
    7 | 8 | 9

Im Beispiel stehen dann für den nächsten Spielzug noch als gültige Eingaben zur
Verfügung, die Ziffern: 1 2 4 6 7 8 9.

Nach jedem Zug wird überprüft, ob eine Gewinnbedingung für die zuletzt aktive Person
eingetreten ist (Waagerechte, Senkrechte oder diagonale Dreiergruppe). Falls ja,
ist der aktuelle Durchgang des Spiels beendet, und es gibt eine Person, die gewonnen
hat. Andernfalls wechselt die Aktivität zur jeweils anderen spielenden Person.

Ein Durchgang endet in jedem Fall, sobald keine freien Felder mehr übrig sind, jedoch
keine der beiden spielenden Personen bisher gewinnen konnte. In diesem Fall gilt der
Durchgang als unentschieden.

Nach jedem Durchgang kann entschieden werden, ob ein weiterer Durchgang gespielt werden
soll. Falls nein, endet das Programm. Falls ja, wechselt das Spielsymbol zwischen den
beiden spielenden Personen (d.h. X wird O und O wird X). Die spielende Person mit
X beginnt den nächsten Durchgang.

Ein gewonnener Durchgang bringt der erfolgreichen Person drei Punkte. Ein unentschiedener
Durchgang bringt beiden spielenden Personen je einen Punkt. Der aktuelle Punktestand
beider spielenden Personen wird am Ende eines Durchganges vom Programm angezeigt.
"""


class Player:

    def __init__(self, name, s):
        self.name = name.capitalize()
        self.symbol = s
        self.result = 0

    def score(self, points):
        self.result += points

    def __str__(self):
        return f'{self.name} hat {self.result} Punkt{"e" if self.result != 1 else ""} erzielt.'


class Board:

    def __init__(self):
        """Das Feld mit der Null wird ignoriert."""
        self.fields = [n for n in range(10)]

    def set(self, s, index):
        self.fields[index] = s

    def choices(self):
        return [n for n in self.fields[1:] if str(n) not in 'XO']

    def __str__(self):
        return '\n'.join((
            ' | '.join(map(str, self.fields[1:4])),
            ' | '.join(map(str, self.fields[4:7])),
            ' | '.join(map(str, self.fields[7:]))
        ))


def swap_symbols(a, b):
    a.symbol, b.symbol = b.symbol, a.symbol


def symbol(player):
    return f'{player.name} spielt mit "{player.symbol}".'


class Game:
    triples = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3])

    def __init__(self, a, b):
        self.active = a
        self.waiting = b
        self.board = Board()
        self.result = 0

    def running(self):
        return self.result == 0

    def next_move(self):
        choices = self.board.choices()
        move = None
        while len(choices) and move not in choices:
            try:
                move = int(input(f'Gib eine Ziffer aus {choices} ein: '))
            except ValueError:
                move = None
            if move not in choices:
                print('Diese Position steht nicht zur Verfügung.')
        if move is None:
            self.result = 1
        else:
            self.board.set(self.active.symbol, move)
            self.result = self.score()
        if self.result == 3:
            self.active.score(self.result)
        elif self.result == 1:
            self.active.score(self.result)
            self.waiting.score(self.result)
        else:
            self.active, self.waiting = self.waiting, self.active

    def score(self):
        if any(self.is_triple(t) for t in self.triples):
            return 3
        else:
            return 0

    def is_triple(self, candidate):
        return self.board.fields[candidate[0]] == self.board.fields[candidate[1]] == self.board.fields[candidate[2]]

    def __str__(self):
        prefix = f'\nSpielbrett:\n{self.board}\n'
        if self.result == 1:
            return f'{prefix}Der Durchgang endete unentschieden.'
        elif self.result == 3:
            return f'{prefix}{self.active.name} hat gewonnen.'
        else:
            return f'{prefix}{self.active.name} ist am Zug.'


def play_again(prompt):
    answer = None
    while answer not in 'j n'.split():
        answer = input(prompt + '(j/n) => ')
    return answer == 'j'


if __name__ == '__main__':
    print('T i c ,  T a c ,  T o e')
    print('-' * 72)
    print()
    player_a = Player(input('Name der ersten Person:  '), 'X')
    player_b = Player(input('Name der zweiten Person: '), 'O')
    print()
    while True:
        print(symbol(player_a))
        print(symbol(player_b))
        game = Game(player_a, player_b)
        print(game)
        while game.running():
            game.next_move()
            print(game)
        print(player_a)
        print(player_b)
        print()
        if not play_again('Soll nochmals gespielt werden? '):
            break
        swap_symbols(player_a, player_b)
    print()
    print('Bis zum nächsten Mal!')
