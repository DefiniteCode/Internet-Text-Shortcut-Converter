import tkinter
from tkinter import *


class ShortcutConverter():
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x350')
        self.root.title('Shortcut Converter')

        # dictionary containing some abbreviations and their meaning
        self.word_dict = {'lol': 'laugh out loud',
                     'wtf': 'what the fuck',
                     'smh': 'shaking my head',
                     'brb': 'Be right back',
                     'btw': 'By the way',
                     'g2g': 'Got to go',
                     'gtg': 'Got to go',
                     'wtg': 'we thank God',
                     'wta': 'we thank Allah',
                     'hmu': 'hit me up',
                     'hmb': 'hit me back',
                     'b4': 'before',
                     'ion': 'I don\'t',
                     'dint': 'didn\'t',
                     'idc': 'I don\'t care ',
                     'idk': 'I don\'t know',
                     'ikr': 'I know Right',
                     'ily': 'I love you',
                     'luv': 'love',
                     'lmao': 'Laughing my A** off',
                     'nvm': 'Never mind',
                     'omw': 'On my way',
                     'rofl': 'Rolling on the floor laughing',
                     'tbh': 'To be honest',
                     'tgif': 'Thank God it\'s friday',
                     'taif': 'Thank Allah it\'s friday',
                     'wbu': ' what about you',
                     'wby': 'what about you',
                     'walaba': 'what about',
                     'yolo': 'You only live once',
                     'pm': 'private message',
                     'dm': 'direct message',
                     'fb': 'facebook',
                     'ig': 'Instagram',
                     'nbd': 'No big deal',
                     'af': 'As F**k',
                     'jk': 'Just kidding',
                     'Obv': 'Obviously',
                     'pls': 'please',
                     'rn': 'right now',
                     'ty': 'Thank You',
                     'tnx': 'Thanks',
                     '10x': 'thanks',
                     'bae': 'baby',
                     'bff': 'Best friends forever',
                     'bf': 'boyfriend',
                     'gf': 'girlfriend',
                     'omg': 'Oh my God',
                     'lmk': 'let me know',
                     'knw': 'know',
                     'jic': 'just in case',
                     'mcm': 'man crush monday',
                     'mc': 'man crush',
                     'wcm': 'woman crush wednesday',
                     'wc': 'woman crush',
                     'BB': 'bye bye',
                     'Gm': 'Good Morning',
                     'Gn': 'Good Night',
                     'gud': 'good',
                     'cn': 'can',
                     'cnt': 'can\'t',
                     'nt': 'not',
                     'sup': 'what\'s up',
                     'zup': 'what\'s up',
                     'xup': 'what\'s up',
                     'sap': 'what\'s up',
                     'zap': 'what\'s up',
                     'xap': 'what\'s up',
                     'kk': 'okay',
                     'naa': 'no',
                     'hom': 'home',
                     'sch': 'school',
                     'skul': 'school',
                     'n': 'and',
                     'jx': 'just',
                     'x': 'is',
                     'd': 'the',
                     'dis': 'this',
                     'dat': 'that',
                     'fini': 'fish',
                     'u': 'you',
                     'cos': 'because',
                     'coz': 'because',
                     'tym': 'time',
                     'sam': 'some',
                     'samwan': 'someone',
                     'gimme': 'give me',
                     'lappy': 'laptop',
                     'rem': 'remember',
                     'rec': 'recognize',
                     'tins': 'things',
                     'oda': 'other',
                     'wah': 'what',
                     'fon': 'phone',
                     'onli': 'only',
                     'lyk': 'like',
                     'moni': 'money',
                     'bt': 'but',
                     'bliv': 'believe',
                     'ihr': 'i hear',
                     'kam': 'come',
                     'ur': 'your',
                     'den': 'then',
                     'Tg': 'Thank God',
                     'Ta': 'Thank Allah',
                     'diff': 'different',
                     'tho': 'though',
                     'dw': 'Don\'t worry',
                     'wen': 'when',
                     'pc': 'personal computer',
                     'them': 'them',
                     'sef': 'self',
                     'saf': 'self',
                     'widaut': 'without',
                     'dd': 'did',
                     'wud': 'would',
                     'll': 'will',
                     'wil': 'will',
                     'av': 'have',
                     'hav': 'some',
                     'ukr': 'You know right',
                     'nyc': 'nice',
                     'luk': 'look',
                     'wat': 'what',
                     'hu': 'who',
                     'hus': 'whose',
                     'hw': 'how',
                     'c': 'see',
                     'frgt': 'forgot',
                     '4get': 'forget',
                     'y': 'why',
                     'wasop': 'What\'s up',
                     'wasup': 'what\'s up',
                     '2day': 'today',
                     '2moro': 'tomorrow',
                     'moro': 'tomorrow',
                     'samwer': 'somewhere',
                     'samtin': 'something',
                     'sambori': 'somebody',
                     'samway': 'some way',
                     'samtins': 'somethings',
                     'axd': 'asked',
                     'buh': 'but',
                     'abt': 'about',
                     'ax': 'ask',
                     'fr': 'for',
                     'sm': 'some',
                     'p': 'problem',
                     'tot': 'thought',
                     'mre': 'more',
                     'reli': 'really',
                     'yestee': 'yesterday',
                     'yestanite': 'yesternight',
                     'nite': 'night',
                     'wit': 'with',
                     'tru': 'through',

                     }

        # functions
        def clear():
            self.statement.delete(0, END)
            self.result.delete('1.0', END)

        def convert():
            user_input = self.statement.get()
            user_lower =  user_input.lower()
            data = user_lower.split()

            for key, value in self.word_dict.items():
                if key in data:
                    data[data.index(key)] = value

            self.result.insert(END, data)


        # heading
        Label(self.root, text='Shortcut Converter', font=('raleway', 20, 'bold'), fg='indigo').place(x=20, y=10)

        # entry to receive input from user

        Label(self.root, text='please enter the statement, word or abbreviation', font=('raleway', 9, 'bold'), fg='indigo').place(x=5, y=60)
        Label(self.root, text='in the space provided below', font=('raleway', 9, 'bold'), fg='indigo').place(x=60, y=80)

        self.statement = Entry(self.root, width=45)
        self.statement.place(x=13, y=110)

        # Convert Button
        Button(self.root, text='Convert', width=12, command= convert, font=('raleway', 9, 'bold'), fg='indigo').place(x=50, y=140)

        # clear Button
        Button(self.root, text='Clear', width=12, command=clear, font=('raleway', 9, 'bold'), fg='indigo').place(x=150, y=140)

        # results area
        Label(self.root, text='RESULT', font=('railway', 10, 'bold'), fg='indigo').place(x=120, y=170)
        self.result = Text(self.root, width=31, height=9,font=('railway', 12, 'bold'))
        self.result.place(x=8, y=195)






root = Tk()
obj = ShortcutConverter(root)
root.mainloop()
