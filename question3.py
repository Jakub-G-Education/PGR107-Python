class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.text = ""

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def append(self, line):
        self.text = self.text + f"\n{line}"

    def to_string(self):
        return (f"From: {self.get_sender()}\nTo: {self.get_recipient()}\n\nDear {self.get_recipient()}, {self.text} \n"
                f"\nKind regards,\n{self.get_sender()} ")


message = Message("Mary", "John")

message.append("The code is written in Python.")
message.append("The task is from the exam Question 3.")

print(message.to_string())
