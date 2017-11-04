from django.http import HttpResponse
from support.models import Foundation
from django.http import HttpResponse

from support.models import Foundation


def support_foundation(request):
    if request.method == 'POST':
        foundation_id = request.POST.get('foundation_id')
        counter = Foundation.objects.add_support(foundation_id)

        return HttpResponse(counter)
