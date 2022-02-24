from dashboard.models import Lead

def menu_links(request):
    links = Lead.objects.all()
    return dict(links=links)