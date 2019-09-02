import uuid

from django.db.models import F

from UserApp.models import StrangeUser, UserAccount

USER_KEY = 'uid'


class UserAccessMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):

        email = request.session.get('user_email')
        if email:
            UserAccount.objects.filter(email=email).update(access_count = F('access_count')+1)
            request.user_account = UserAccount.objects.filter(email=email)[0]
        else:
            request.user_account = None


        sUser = self.get_sUser(request)
        request.sUser = sUser

        response = self.get_response(request)
        return response

    def get_sUser(self,request):
        try:
            uid = request.session[USER_KEY]
            sUser = StrangeUser.objects.filter(uid=uid)
            sUser.update(access_count=F('access_count') + 1)
            return sUser[0]
        except KeyError:
            uid = request.META.get('REMOTE_ADDR')
            request.session.set_expiry(60*60*24*10)
            request.session[USER_KEY] = uid
            sUser = StrangeUser.objects.filter(uid=uid)

            if len(sUser):
                sUser.update(access_count=F('access_count')+1)
            else:
                sUser=[]
                ssUser = StrangeUser()
                ssUser.uid = uid
                ssUser.access_count = 1
                ssUser.objects.save()
                sUser.append(ssUser)
            return sUser[0]




