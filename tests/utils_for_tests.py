import csv

class UtilsForTests():
    
    def loadTestCorpus(self, file):
        case = [];
        with open(file) as f:
            line = f.readline();
            case.append(eval(line));
        return case;