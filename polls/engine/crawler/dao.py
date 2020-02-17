from polls.models import PollsBreakdown

def breakdown_dao(request):
    print('dao 진입1')
    pollsBreakdown = PollsBreakdown.objects.create()
    print('bywhat=',request.POST['ByWhat'])
    print('keywordA=',request.POST.getlist('keywordA'))
    pollsBreakdown.bywhat = request.POST['ByWhat']
    pollsBreakdown.usr_id = request.POST['username']
    pollsBreakdown.usr_key = request.POST['usr_key']
    print(pollsBreakdown.usr_key)
    pollsBreakdown.nUrlA = request.POST['nUrlA']
    pollsBreakdown.nUrlB = request.POST['nUrlB']
    pollsBreakdown.keywordA = request.POST.getlist('keywordA')  # keywordA 필드값 입력
    pollsBreakdown.keywordB = request.POST.getlist('keywordB') if (  len(  request.POST.getlist('keywordB')  ) > 0  ) else request.POST.getlist('keywordA')
    pollsBreakdown.channelA = request.POST.getlist('channelA')
    pollsBreakdown.channelB = request.POST.getlist('channelB') if (  len(  request.POST.getlist('channelB')  ) > 0  ) else request.POST.getlist('channelA')
    pollsBreakdown.periodA = request.POST.getlist('aday')  # period A
    pollsBreakdown.periodB = request.POST.getlist('bday') if (  len(  request.POST.getlist('bday')  ) > 0  ) else request.POST.getlist('aday')
    pollsBreakdown.saved_path = "polls/source/image/wordcloud/"+str(pollsBreakdown.id)+".png"
    pollsBreakdown.saved_name = "polls/source/image/wordcloud/"+str(pollsBreakdown.id)+".png"
    pollsBreakdown.save()

    return pollsBreakdown

def login_dao(request):
    print("회원정보가져오기")