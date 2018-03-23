import requests
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import status

User = get_user_model()


class APIFacebookBackend:
    CLIENT_ID = settings.FACEBOOK_APP_ID,
    CLIENT_SECRET_ID = settings.FACEBOOK_SECRET_CODE
    URL_ACCESS_TOKEN = 'https://graph.facebook.com/v2.12/oauth/access_token'
    URL_ME = 'https://graph.facebook.com/v2.12/me'

    def authenticate(self, request, access_token):
        def get_user_info(user_access_token):
            params_user = {
                'access_token': user_access_token,
                'fields': ','.join([
                    'id',
                    'name',
                    'picture.width(2500)',
                    'first_name',
                    'last_name',
                ]),
            }

            response = requests.get(self.URL_ME, params=params_user)

            if response.status_code == status.HTTP_200_OK:
                response_dict = response.json()
                return response_dict
            else:
                print('status code: ', response.status_code)
                print('\n\nresponse')
                print(response)

        try:
            user_info = get_user_info(access_token)
            facebook_id = user_info.get('id')
            facebook_name = user_info.get('name')
            facebook_picture_url = user_info['picture']['data']['url']
            facebook_first_name = user_info.get('first_name')
            facebook_last_name = user_info.get('last_name')

            try:
                user = User.objects.get(username=facebook_id)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=facebook_id,
                    nickname=facebook_name,
                    img_profile_url=facebook_picture_url,
                    first_name=facebook_first_name,
                    last_name=facebook_last_name,
                )

            return user
        except Exception as e:
            print('facebook authenticate error: ', e)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
