# TASK - Polymorphism Practice 3
#
# Create 3 classes: WhatsApp, Instagram, Twitter
# Each class has one method: send_message()
#   - WhatsApp  -> prints "Sending message via WhatsApp"
#   - Instagram -> prints "Sending message via Instagram"
#   - Twitter   -> prints "Sending message via Twitter"
#
# Create a list with one object of each class.
# Loop through the list and call send_message() on each.

class WhatsApp():
    def send_msg(self):
        print(f"msg on whatsapp")
class Insta():
    def send_msg(self):
        print(f"msg via insta")
class Twitter():
    def send_msg(self):
        print(f"Send msg via Twitter")

msg = [WhatsApp(),Insta(),Twitter()]

for m in msg:
    m.send_msg()
    