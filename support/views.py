from django.http import HttpResponse

from support.models import Foundation


def support_foundation(request):
    if request.method == 'POST':
        user = request.user
        foundation_id = request.POST.get('foundation_id')
        counter = Foundation.objects.add_support(user, foundation_id)
        return HttpResponse(counter)
