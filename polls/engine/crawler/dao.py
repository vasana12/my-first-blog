from polls.models import Breakdown

def dao(request):
    breakdown = Breakdown.objects.create()
    print('dao 진입')
    breakdown.ByWhat = request.POST['ByWhat']
    print(breakdown.ByWhat)
    breakdown.nUrlA = request.POST.getlist('nUrl')[0]
    breakdown.nUrlB = request.POST.getlist('nUrl')[1] if (  len(request.POST.getlist('nUrl'))> 0 ) else breakdown.nUrlA
    breakdown.keywordA = request.POST.getlist('keywordA')  # keywordA 필드값 입력
    breakdown.keywordB = request.POST.getlist('keywordB') if (  len(  request.POST.getlist('keywordB')  ) > 0  ) else request.POST.getlist('keywordA')
    breakdown.channelA = request.POST.getlist('channelA')
    breakdown.channelB = request.POST.getlist('channelB') if (  len(  request.POST.getlist('channelB')  ) > 0  ) else request.POST.getlist('channelA')
    breakdown.periodA = request.POST.getlist('aday')  # period A
    breakdown.periodB = request.POST.getlist('bday') if (  len(  request.POST.getlist('bday')  ) > 0  ) else request.POST.getlist('aday')
    breakdown.save()
    return breakdown