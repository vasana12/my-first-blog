from polls.models import PollsBreakdown

def dao(request):
    print('dao 진입1')
    pollsBreakdown = PollsBreakdown.objects.create()
    print('dao 진입2')
    print('bywhat=',request.POST['ByWhat'])
    print('keywordA=',request.POST.getlist('keywordA'))
    pollsBreakdown.bywhat = request.POST['ByWhat']
    print(pollsBreakdown.bywhat)
    pollsBreakdown.nUrlA = request.POST.getlist('nUrl')[0]
    pollsBreakdown.nUrlB = request.POST.getlist('nUrl')[1] if (  len(request.POST.getlist('nUrl'))> 0 ) else pollsBreakdown.nUrlA
    pollsBreakdown.keywordA = request.POST.getlist('keywordA')  # keywordA 필드값 입력
    pollsBreakdown.keywordB = request.POST.getlist('keywordB') if (  len(  request.POST.getlist('keywordB')  ) > 0  ) else request.POST.getlist('keywordA')
    pollsBreakdown.channelA = request.POST.getlist('channelA')
    pollsBreakdown.channelB = request.POST.getlist('channelB') if (  len(  request.POST.getlist('channelB')  ) > 0  ) else request.POST.getlist('channelA')
    pollsBreakdown.periodA = request.POST.getlist('aday')  # period A
    pollsBreakdown.periodB = request.POST.getlist('bday') if (  len(  request.POST.getlist('bday')  ) > 0  ) else request.POST.getlist('aday')
    pollsBreakdown.save()

    return pollsBreakdown