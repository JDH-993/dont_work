class WordsFinder:
    def __init__(self, *args):
        self.args = args
        self.stroka(args)

    def stroka(*args):
        stroch = []
        for i in args:
            for y in i:
                stroch.append(y)
        return stroch

    def get_all_words():
        print(0)
        for k in self.stroka.stroch:
            print(9)
            with open(self.stroch[k], encoding= 'utf-8') as file:
                for n in file:
                    n.lower()
                    for t in n:
                        print(t)



g = WordsFinder("uihuig", "jftykfury", "ghl")
g.get_all_words()