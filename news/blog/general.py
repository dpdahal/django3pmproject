from .models import SettingModel, BlogCategory


def setting(request):
    data = {
        'companyData': SettingModel.objects.first(),
        'blogCategoryData': BlogCategory.objects.all()
    }
    return data
