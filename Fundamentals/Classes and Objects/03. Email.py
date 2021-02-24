class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while command != "Stop":
    email_info = command.split()
    sender_1 = email_info[0]
    receiver_1 = email_info[1]
    content_1 = email_info[2]
    email = Email(sender_1, receiver_1, content_1)
    emails.append(email)
    command = input()
send_emails = input().split(", ")
send_emails = [int(x) for x in send_emails]
[emails[x].send() for x in send_emails]
[print(x.get_info()) for x in emails]


