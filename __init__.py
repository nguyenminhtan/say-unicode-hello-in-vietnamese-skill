from mycroft import MycroftSkill, intent_file_handler


class SayUnicodeHelloInVietnamese(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vietnamese.in.hello.unicode.say.intent')
    def handle_vietnamese_in_hello_unicode_say(self, message):
        self.speak_dialog('vietnamese.in.hello.unicode.say')


def create_skill():
    return SayUnicodeHelloInVietnamese()

