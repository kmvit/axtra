from .models import Page


def contact_information(request):
    info = Page.objects.get(is_home_page=True)
    if info:
        context = {
            'phone': info.phone,
            'mobile': info.mobile_phone,
            'email': info.email,
            'address': info.address,
            'instagram': info.instagram,
            'vk': info.vk,
        }
    else:
        context = {
            'phone': '',
            'mobile': '',
            'email': '',
            'address': '',
            'instagram': '',
            'vk': '',
        }
    return context
