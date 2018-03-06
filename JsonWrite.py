import json

cards = {'CardSum': 0, 'Card': {
    "Ev": [], "Pe": [], "Lu": [], "Co": [], "Lo": []}}

cardsType = {'Event': 1, "Person": 2, "Logic": 3, "Lucky": 4, "Condition": 5}


class Card(object):
    def __init__(self, catype, caname, fileName, cost, inner):
        self.catype = catype
        self.caname = caname
        self.fileName = fileName
        self.cost = cost
        self.inner = inner

    def obj2cards(self):
        dic = dict.update(self.__dict__)
        catype = dic['catype']
        if catype == cardsType['Event']:
            Card.classifier(dic, 'Ev')
        elif catype == cardsType['Person']:
            Card.classifier(dic, 'Pe')
        elif catype == cardsType['Logic']:
            Card.classifier(dic, 'Lo')
        elif catype == cardsType['Lucky']:
            Card.classifier(dic, 'Lu')
        elif catype == cardsType['Condition']:
            Card.classifier(dic, 'Co')

    @staticmethod
    def classifier(dic, string):
        del dic['catype']
        global cards
        cards['Card'][string].append(dic)
        cards['CardSum'] += 1


def dict2obj(d):
    args = dict((key.encode('utf-8'), value) for key, value in d.items())
    instance = Card(**args)
    return instance


def input2jsonFile(f):
    cardNum = int(input("AppendCardNumber>>>"))
    while cardNum > 0:
        newCard = Card(-1, '0', '', -1, '')
        while True:  # 卡牌类型
            try:
                inp = int(input(str(cardsType) + ">>>"))
            except:
                inp = -1
            finally:
                if inp > 0 and inp < 6:
                    newCard.catype = inp
                    break
        while True:  # 卡牌名称，未规定长度
            inp = input("CardName>>>")
            if inp.isalpha():
                inp.strip()
                newCard.caname = inp
                break
        while True:  # 文件名称，未规定长度
            inp = input("FileName(End of this must be '.png')>>>")
            if inp.endswith('.png'):
                inp.strip()
                newCard.fileName = inp
                break
        while True:  # 属性花费，未规定最大值
            try:
                inp = int(input("Cost>>>"))
            except:
                inp = -1
            finally:
                if inp >= 0 and inp < 12:
                    newCard.cost = inp
                    break
        while True:  # 卡牌内容，未规定长度
            inp = input("Inner>>>")
            if len(inp) > 0 and len(inp) < 50:
                newCard.inner = inp
                break
        newCard.obj2cards()
        cardNum -= 1
        print("*" * 30)
    print(cards)
    json.dump(cards, f, indent=4)  # json序列化


def printfs(string):
    for ins in cards['Card'][string]:
        print(ins)


def load2Console(f):
    while True:
        inp = int(input('Operate(Sum:1;Card:2)>>>'))
        if inp == 1:
            print(cards['CardSum'])
            break
        elif inp == 2:
            inp = int(input(str(cardsType) + '>>>'))
            if inp == cardsType['Event']:
                printfs('Ev')
            elif inp == cardsType['Person']:
                printfs('Pe')
            elif inp == cardsType['Logic']:
                printfs('Lo')
            elif inp == cardsType['Lucky']:
                printfs('Lu')
            elif inp == cardsType['Condition']:
                printfs('Co')
            break


def FileLoad():
    try:
        f = open("Json.json", "r+")
    except:
        f = open("Json.json", "w")

    try:
        global cards
        cards = json.load(f)
    except:
        cards['CardSum'] = 0
        cards['Card'] = {
            "Ev": [], "Pe": [], "Lu": [], "Co": [], "Lo": []}
    return f


def choisWorR(f):
    inp = input("Read or Write(r,w)>>>")
    if inp == 'r':
        load2Console(f)
    elif inp == 'w':
        input2jsonFile(f)


if __name__ == "__main__":
    f = FileLoad()
    choisWorR(f)
    f.close()
