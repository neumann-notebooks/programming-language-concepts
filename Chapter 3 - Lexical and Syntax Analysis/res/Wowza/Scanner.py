import re
class Scanner:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.line = ""
        self.eof = False
    def __peekChar(self):
        if not self.line:
            self.line = self.file.readline()
            self.eof = (len(self.line) == 0)
        return self.line[0] if not self.eof else ""
    def __getChar(self):
        c = self.__peekChar()
        self.line = self.line[1:]
        return c
    def lex(self):
        if self.eof:
            return None
        print("CHAR:",self.__getChar())
        if not self.__peekChar():
            print("EOF!!!")
