# Create your views here.
import base64
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .forms import VoterRegistrationForm, PartiesRegistrationForm
from .models import VoterRegistrationModel, PartiesRegistrationModel, VotingPollModel
from django.conf import settings
from admins.models import VotingTurnOn


def VoterRegistrations(request):
    if request.method == 'POST':
        form = VoterRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            loginid = form.cleaned_data.get('loginid')
            print("Login ID:",loginid)
            # form = VoterRegistrationForm()

            # return render(request, 'UserRegistrations.html', {'form': form})
            return render(request, 'GetUserPics.html', {'loginid': loginid})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = VoterRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = VoterRegistrationModel.objects.get(loginid=loginid, password=pswd)
            age = check.age
            print('Age is = ', age)
            if age > 18:
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'You cant vote')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    # VoterRegistrationModel.objects.all().delete()
    # VotingPollModel.objects.all().delete()
    return render(request, 'users/UserHomePage.html', {})


def VoterPage(request):
    vote = VotingTurnOn.objects.get(id=1)
    id = request.session['id']
    v_data = VoterRegistrationModel.objects.get(id=id)
    aadhar = v_data.aadhar
    if vote.status == 'active':
        data = PartiesRegistrationModel.objects.all()
        print('AM Good')
        return render(request, 'users/voterpage.html', {'data': data, 'vote': vote, 'aadhar': aadhar})
    elif vote.status == 'inactive':
        return render(request, 'users/voterpage.html', {'vote': vote})
    else:
        return render(request, 'users/voterpage.html', {'vote': vote})


def VoterVoting(request):
    if request.method == 'POST':
        aadhar = request.POST.get('aadhar')
        candidate_id = int(request.POST.get('vote'))
        candidate = PartiesRegistrationModel.objects.get(id=candidate_id)
        candidateName = candidate.name
        constituency = candidate.locality
        partyname = candidate.partyname
        vote = 1
        try:
            VotingPollModel.objects.create(aadhar=aadhar,candidate_id=candidate_id,candidateName=candidateName,constituency=constituency,partyname=partyname,vote=vote)
            return render(request, 'success.html', {'msg': 'you voted sucess'})
        except Exception as ex:
            print(ex)
            return render(request, 'success.html', {'msg': 'you voted Already'})
    return HttpResponse('votting Under work')


def save_image(request):
    imgstr = request.POST['mydata']
    voting_session_id = request.POST.get('voting_session')
    # user = request.user.username

    if request.POST:
        f = open(settings.MEDIA_ROOT + '/webcamimages/' + voting_session_id + '.jpg', 'wb')
        f.write(base64.b64decode(imgstr))
        f.close()

    messages.success(request, f'A picture of your face has been saved in the database!')
    return render(request, 'index.html', {'msg': 'success'})


def face_recog(webcam_photo, user_photo):
    import face_recognition
    picture_of_me = face_recognition.load_image_file(user_photo)
    my_face_encoding, unknown_face_encoding = [], []
    if face_recognition.face_encodings(picture_of_me):
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    else:
        return False
    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    unknown_picture = face_recognition.load_image_file(webcam_photo)
    if face_recognition.face_encodings(unknown_picture):
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    else:
        return False
    # Now we can see the two face encodings are of the same person with `compare_faces`!
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    return results[0]


def ValidatePicandOTP(request):
    if request.method=='POST':
        imgstr = request.POST['mydata']
        user_otp = int(request.POST.get('otp'))
        server_otp = request.session['server_otp']
        f = open(settings.MEDIA_ROOT + '/test/' + 'one' + '.jpg', 'wb')
        f.write(base64.b64decode(imgstr))
        f.close()
        if user_otp==server_otp:
            print('Valid Otp')
            loginid = request.session['loginid']
            can_vote = face_recog(settings.MEDIA_ROOT + '/webcamimages/' + loginid + '.jpg',
                                  settings.MEDIA_ROOT + '/test/' + 'one' + '.jpg')
            print('Voting user Status: ',can_vote)
            if can_vote:
                vote = VotingTurnOn.objects.get(id=1)
                id = request.session['id']
                v_data = VoterRegistrationModel.objects.get(id=id)
                aadhar = v_data.aadhar
                if vote.status == 'active':
                    data = PartiesRegistrationModel.objects.all()
                    return render(request, 'users/voterpage.html', {'data': data, 'vote': vote, 'aadhar': aadhar})
                elif vote.status == 'inactive':
                    return render(request, 'users/voterpage.html', {'vote': vote})
                else:
                    return render(request, 'users/voterpage.html', {'vote': vote})
            else:
                return render(request, 'success.html', {'msg': 'Facial Authentication Failed'})
        else:
            return render(request, 'success.html', {'msg': 'Invalid OTP'})

    else:
        import random
        fixed_digits = 6
        otp = random.randrange(111111, 999999, fixed_digits)
        print("Otp is:",otp)
        request.session['server_otp'] = otp
        return render(request, 'users/face_auth.html',{})