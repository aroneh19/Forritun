class Message:
    def __init__(self, msg_from, msg_to):
        self.msg_from = msg_from
        self.msg_to = msg_to
        self.text = ""
    
    def append(self, msg):
        self.text += msg + "\n"
    
    def __len__(self):
        return len(self.text.replace("\n", ""))
    
    def __gt__(self, other):
        return len(self) > len(other)

    def __str__(self):
        return f"From: {self.msg_from}\nTo: {self.msg_to}\n{self.text}"
