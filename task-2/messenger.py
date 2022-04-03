from datetime import datetime

data_base = {}
chats_base = []
chats = []

class User():
    def __init__(self, nickname: str, name: str, surname: str):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        # self.files_attached = set()
        # self.chats = []
        self.add_user()

    def add_user(self):
        new_user_info = {}
        new_user_info['nickname'] = self.nickname
        new_user_info['name'] = self.name
        new_user_info['surname'] = self.surname
        new_user_info['attached_files'] = set()
        new_user_info['chats'] = []
        data_base[self.nickname] = new_user_info

class Message():
    def __init__(self, sender: str, addressee: str, message: str):
        self.sender = sender
        self.addressee = addressee
        self.message = message
        self.add_message()

    def add_message(self):
        if self.sender not in data_base.keys():
            print(f'No user with such a nickname {self.sender}, add user')
        elif self.addressee not in data_base.keys():
            print(f'No user with such a nickname {self.addressee}, add user')
        else:
            chat = [self.sender, self.addressee]
            chat.sort()
            if chat not in chats_base:
                chats_base.append(chat)
                chats.append([])
                data_base[self.sender]['chats'].append([self.addressee])
                data_base[self.addressee]['chats'].append([self.sender])
            # else:
            #     print(f'The chat for these users already exists: {self.sender}, {self.addressee}')
            message_info = {}
            message_info['from'] = self.sender
            message_info['to'] = self.addressee
            message_info['text'] = self.message
            message_info['datetime'] = datetime.now()
            num_chat = chats_base.index(chat)
            chats[num_chat].append(message_info)

User('Mike123', 'Mike', 'Smith')
User('AnkA', 'Anna', 'Carter')
User('Dave1983', 'Dave', 'Smith')
print(data_base)


Message('Mike123', 'AnkA', 'Are you going to gim?')
Message('Mike123', 'Dave1983', 'How are you?')
Message('Dave1983', 'Mike123', 'Better, but I\'m not going to gim today')
print(data_base)
print(chats_base)
print(chats)
