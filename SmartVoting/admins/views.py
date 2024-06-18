from django.shortcuts import render, HttpResponse
from django.contrib import messages
from users.models import VoterRegistrationModel,PartiesRegistrationModel,VotingPollModel
from users.forms import PartiesRegistrationForm
from .models import VotingTurnOn
from django.db.models import Count,Avg,Sum
# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def RegisterUsersView(request):
    data = VoterRegistrationModel.objects.all()
    return render(request,'admins/viewregisterusers.html',{'data':data})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admins/viewregisterusers.html',{'data':data})

# Create your views here.
def PartiesRegisterActions(request):
    data = PartiesRegistrationModel.objects.all()
    if request.method == 'POST':
        form = PartiesRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.partysymbol = request.FILES['partysymbol']
            file_type = user_pr.partysymbol.url.split('.')[-1]
            file_type = file_type.lower()
            user_pr.save()
            messages.success(request, 'You have been successfully registered')
            form = PartiesRegistrationForm()

            return render(request, 'admins/PartiesRegistrations.html', {'form': form,'data': data})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = PartiesRegistrationForm()
    return render(request, 'admins/PartiesRegistrations.html', {'form': form,'data': data})



def DeleteParty(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        print("PID = ", id)
        PartiesRegistrationModel.objects.filter(id=id).delete()
        data = PartiesRegistrationModel.objects.all()
        form = PartiesRegistrationForm()
        return render(request, 'admins/PartiesRegistrations.html', {'form': form, 'data': data})


def AdminElectionsTurnOn(request):
    # VotingTurnOn.objects.create(status='active')
    data = VotingTurnOn.objects.get(id=1)
    return render(request, "admins/adminvoteturnon.html", {'data': data})


def VoteTurnOn(request):
    # VotingTurnOn.objects.create(status='active')
    VotingTurnOn.objects.filter(id=1).update(status='active')
    data = VotingTurnOn.objects.get(id=1)
    return render(request, "admins/adminvoteturnon.html", {'data': data})

def VoteTurnOff(request):
    VotingTurnOn.objects.filter(id=1).update(status='inactive')
    data = VotingTurnOn.objects.get(id=1)
    return render(request, "admins/adminvoteturnon.html", {'data': data})


def AdminElectionsResults(request):
    # p = VotingPollModel.objects.all().annotate(Count('VotingPollModel__partyname',distinct=True))
    count = VotingPollModel.objects.order_by().values('partyname').distinct()
    results = {}
    symb= {}
    for row in count:
        party = row['partyname']
        print('Party is:',party)
        d_data = VotingPollModel.objects.filter(partyname=party)
        symbols = PartiesRegistrationModel.objects.get(partyname=party)
        count  = 0
        for s in d_data:
            vo = s.vote
            count = count+vo
        results.update({party:count})
        symb.update({symbols.name:symbols.partysymbol})
    print(results)
    dataset = VotingPollModel.objects.values('candidateName').annotate(dcount=Sum('vote'))
    return render(request, "admins/results.html", {'data': results,'symb': symb,'chart_type': 'bar', 'dataset': dataset})