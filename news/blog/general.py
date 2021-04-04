from .models import SettingModel


def setting(request):
    data = {
        'companyData': SettingModel.objects.first()
    }
    return data
