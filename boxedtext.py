"""
Author: Nathan Carter
Licence: GPL 3.0
"""

class Box:
    def __init__(self, width):
        self._width = width
        self._text = "#"*width + "########" # for the padding and border

    def add_text(self, text, center=False):
        if center:
            self._text += "\n"
            self._text += "##  "
            lpad = (self._width - len(text))//2
            rpad = self._width - lpad - len(text)
            self._text += " " * lpad + text + " " * rpad
            self._text += "  ##"
            
        else:
            lines = []
            words = text.split(" ")
            line = []
            for word in words:
                if len(" ".join(line)) + len(" " + word) <= self._width:
                    line.append(word)
                else:
                    lines.append(line)
                    line = [word]
                    
            # get the last line
            if len(line) != 0:
                lines.append(line)
                    
            for line in lines:
                self._text += "\n##  " + " ".join(line) + " " * (self._width - len(" ".join(line))) + "  ##"

    def add_list(self, items):
        for i in range(len(items)):
            lines = []
            words = items[i].split(" ")
            line = [f"{i + 1}."]
            indent = 0
            for word in words:
                if len(" ".join(line)) + len(" " + word) <= self._width - indent:
                    line.append(word)
                else:
                    lines.append(line)
                    line = [word]
                indent = 3
            # get the last line
            if len(line) != 0:
                lines.append(line)

            indent = 0
            for line in lines:
                self._text += "\n##  " + " " * indent + " ".join(line) + " " * (self._width - len(" ".join(line)) - indent) + "  ##"
                indent = 3
        

    def __str__(self):
        return self._text + "\n" + "#"*self._width + "########"

    def __repr__(self):
        return self._text + "\n" + "#"*self._width + "########"
