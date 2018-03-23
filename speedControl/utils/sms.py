from django.conf import settings
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


class SMS():
    def __init__(self, to_number, text):
        self.api_key = settings.COOL_SMS_KEY
        self.api_secret = settings.COOL_SMS_SECRET_KEY

        self.params = dict()
        self.params['type'] = 'sms'
        self.params['to'] = to_number
        self.params['from'] = settings.LHY_NUMBER
        self.params['text'] = text

    def send_sms(self):
        cool = Message(self.api_key, self.api_secret)
        try:
            response = cool.send(self.params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)


if __name__ == '__main__':
    import random

    # 사용할때 이렇게 사용하면 됨.
    send_message = ['빠름 빠름 빠름', '쉬는 쉬간 입니다', '저는 아무것도 모르겠습니다']
    sms = SMS(to_number='01051420203', text=random.choice(send_message))

    sms.send_sms()
