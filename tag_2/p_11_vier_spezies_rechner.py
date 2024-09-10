"""
11 Taschenrechner (Tag 2)

Schreibe eine kleine Taschenrechner-Applikation, der die Methoden Addieren, Subtrahieren, Multiplizieren und
Dividieren beherrscht.

Der Taschenrechner soll seine Eingaben über ein Terminal-Interface ("Konsole") entgegennehmen und
die Ergebnisse auf die Konsole ausgeben ("drucken").

Benutzerinnen dürfen nur Zahlen (Operanden) oder Operatoren eingeben. Da nur ein 4-Spezies-Rechner gefordert
ist, sind alle Operationen binär.

Vereinfachend wird angenommen, dass der Taschenrechner nach der sogenannten umgekehrten polnischen Notation (UPN)
entgegennimmt. Auf einer Eingabezahle dürfen Operanden und Operatoren gemäß UPN Regeln durch Leerzeichen
getrennt eingegeben werden.

Wird ein Functions (eine Zahl) vom Rechner erkannt, wird dieser gespeichert ('push = x'). Zur Speicherung verwendet
der Rechner einen Stapelspeicher (Stack). Dieser Stack kann nicht leer sein. Er hat genau N Elemente. Wird ein 5.
Element eingegeben, geht das 'oberste' Element im Stack verloren. Zu Beginn haben alle N Elemente im Stapel den
Wert 0.

Wird ein Functions erkannt, versucht der Rechner, zwei Operanden vom Stack zu holen ('x, y = pop, pop'), und die
gegebene Operation damit auszuführen. Das Ergebnis der Operation wird wieder auf den Stack geschrieben ('push = x').

Am Ende jeder einzelnen Eingabe werden die obersten beiden Werte im Stapelspeicher angezeigt. Das Ergebnis der
bisher abgeschlossenen Berechnungen befindet sich immer in der am weitesten rechts angezeigten Position, die mit 'X ='
ausgewiesen wird.

Die vorletzte Position wird als 'Y=' ausgewiesen.

Folgende Operationen stehen zur Verfügung:

    +    Addiere Y und X.
    -    Subtrahiere X von Y.
    *    Multipliziere Y mit X.
    /    Dividiere Y durch X.
    .    Kopiere die letzte Eingabe und schiebe sie auf den Stack.
    X    Tausche die Stack-Positionen X und Y
    Clr  Lösche den Stapelspeicher (alles auf 0 setzen). Groß-/Kleinschreibung wird ignoriert.
"""


class Stack:

    def __init__(self, size=4):
        self.buffer = [0] * size

    def top(self):
        return self.buffer[-1]

    def pop(self):
        x = self.buffer[-1]
        self.buffer = self.buffer[:1] + self.buffer[:-1]
        return x

    def push(self, x):
        self.buffer = self.buffer[1:] + [x]

    def rotate(self):
        self.buffer = self.buffer[-1:] + self.buffer[:-1]

    def __str__(self):
        return f'Y = {self.buffer[-2]:.4f}, X = {self.buffer[-1]:.4f}'


class Memory:

    def __init__(self):
        self.number = 0

    def set(self, value):
        self.number = value

    def get(self):
        return self.number


class Functions:

    def __init__(self):
        self.stack = Stack()
        self.memory = Memory()
        self.zd_flag = False

    def dump(self):
        return f'STACK: {self.stack}' + (', FEHLER: Division durch Null.' if self.zd_flag else '')

    def enter(self, number):
        self.stack.push(number)

    def duplicate(self):
        self.stack.push(self.stack.top())

    def swap(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.push(x)
        self.stack.push(y)

    def rotate(self):
        self.stack.rotate()

    def add(self):
        self.stack.push(self.stack.pop() + self.stack.pop())

    def subtract(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.push(y - x)

    def multiply(self):
        self.stack.push(self.stack.pop() * self.stack.pop())

    def divide(self):
        x = self.stack.pop()
        y = self.stack.pop()
        try:
            z = y / x
        except ZeroDivisionError:
            self.stack.push(y)
            self.stack.push(x)
            self.zd_flag = True
        else:
            self.stack.push(z)

    def change_sign(self):
        self.stack.push(-self.stack.pop())

    def clear(self):
        self.stack = Stack()

    def reset(self):
        self.zd_flag = False

    def store(self):
        self.memory.set(self.stack.top())

    def recall(self):
        self.stack.push(self.memory.get())


def usage():
    return """Verfügbare Rechen- und Anzeigeoperationen:
    
    q   Rechenprogramm verlassen.
    +   Addiere X und Y.
    -   Subtrahiere X von Y.
    *   Multipliziere X und Y.
    /   Teile Y durch X.
    chs Vorzeichenwechsel bei X.
    .   Kopiere X zu Y.
    x   Vertausche X und Y.
    r   Rotiere den Rechenspeicher über X.
    res Fehlerspeicher löschen.
    clr Lösche den Rechenspeicher.
    m+  Kopiere X in den Festwertspeicher.
    m   Schreibe die Zahl aus dem Festwertspeicher ein.
    ?   Zeige diesen Hilfetext an.
    """


if __name__ == '__main__':
    func = Functions()
    action = {
        '+': func.add, '-': func.subtract, '*': func.multiply, '/': func.divide,
        '.': func.duplicate, 'x': func.swap, 'clr': func.clear, 'chs': func.change_sign,
        'm+': func.store, 'm': func.recall, 'r': func.rotate
    }
    is_terminated = False
    print('Hilfe mit "?".')
    while not is_terminated:
        print(func.dump())
        expression = input('> ').lower().split()
        for token in expression:
            if token == 'q':
                is_terminated = True
                break
            elif token == '?':
                print(usage())
            elif token == 'res':
                func.reset()
                break
            elif func.zd_flag:
                break
            elif token not in action:
                try:
                    func.enter(float(token))
                except ValueError:
                    print(f'FEHLER: Eingabe kann nicht verarbeitet werden: "{token}"')
                    break
            else:
                action[token]()
    print('Bye!')
