from authentication.models import Account

def menu_links(request):
    links = Account.objects.all()
    return dict(links=links)