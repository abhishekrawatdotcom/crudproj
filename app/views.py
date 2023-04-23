from django.shortcuts import render

# Create your views here.




from app.models import UserData
from django.shortcuts import render, redirect
from django.contrib import messages




def ShowPage(request):
    return render(request,'stuhome.html')


def add_book(request):
    if request.method == 'POST':
        group1 = request.POST.get("group1")
        group2 = request.POST.get("group2")
        group3 = request.POST.get("group3")
        group4 = request.POST.get("group4")
        group5 = request.POST.get("group5")
        group6 = request.POST.get("group6")
        group7 = request.POST.get("group7")
        group8 = request.POST.get("group8")
        group9 = request.POST.get("group9")
        group10 = request.POST.get("group10")
        Salutation = request.POST.get("Salutation")
        firstname = request.POST.get("firstname")
        middlename = request.POST.get("middlename")
        lastname = request.POST.get("lastname")
        primarynumber = request.POST.get("primarynumber")
        alternatenumber = request.POST.get("alternatenumber")
        PrimaryMail = request.POST.get("PrimaryMail")
        AlternateMail = request.POST.get("AlternateMail")
        location = request.POST.get("location")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pincode = request.POST.get("pincode")
        Designation = request.POST.get("Designation")
        PrimaryExpertise = request.POST.get("PrimaryExpertise")
        AlternateExpertise1 = request.POST.get("AlternateExpertise1")
        AlternateExpertise2 = request.POST.get("AlternateExpertise2")
        HighestEducation = request.POST.get("HighestEducation")
        gender = request.POST.get("gender")
        DOB = request.POST.get("DOB")
        MessageOpen = request.POST.get("MessageOpen")
        Responded = request.POST.get("Responded")
        LinkClicked = request.POST.get("LinkClicked")
        Source = request.POST.get("Source")
        OrgName = request.POST.get("OrgName")
        NatureOfBusiness = request.POST.get("NatureOfBusiness")
        OrgLocation = request.POST.get("OrgLocation")
        DoNotCall = request.POST.get("DoNotCall")
        DoNotMessage = request.POST.get("DoNotMessage")
        DoNotMail = request.POST.get("DoNotMail")
        DoNotWhatsapp = request.POST.get("DoNotWhatsapp")
        DoNotDisturb = request.POST.get("DoNotDisturb")
        Notes1 = request.POST.get("Notes1")
        Notes2 = request.POST.get("Notes2")
        Notes3 = request.POST.get("Notes3")
        Notes4 = request.POST.get("Notes4")
        Notes5 = request.POST.get("Notes5")
        Remark = request.POST.get("Remark")
        DocumentAttach = request.FILES.get("DocumentAttach")
        Called = request.POST.get("Called")
        Met = request.POST.get("Met")
        FullName = firstname + " " + middlename + " " + lastname
        OutOfStation = request.POST.get("OutOfStation")
        OutOfCountry = request.POST.get("OutOfCountry")
        GeneratedPinCode = request.POST.get("GeneratedPinCode")
        MarkForDeletion = request.POST.get("MarkForDeletion")
        ReasonForDeletion = request.POST.get("ReasonForDeletion")
        BigLink = request.POST.get("BigLink")
        Website = request.POST.get("Website")
        LinkedinLink = request.POST.get("LinkedinLink")
        nstagramLink = request.POST.get("nstagramLink")
        YoutubeLink = request.POST.get("YoutubeLink")
        FacebookLink = request.POST.get("FacebookLink")
        SocialMediaOther = request.POST.get("SocialMediaOther")

        u = UserData(Group1=group1,Group2=group2,Group3=group3,Group4=group4,Group5=group5,Group6=group6,Group7=group7,Group8=group8,Group9=group9,Group10=group10,Salutation=Salutation,
                 First_Name=firstname,Middle_Name=middlename,Last_Name=lastname,Primary_Number=primarynumber,Alternate_Number=alternatenumber,Primary_Mail=PrimaryMail,Alternate_Mail=AlternateMail,Location=location,City=city,State=state,Country=country,Pincode=pincode,Designation=Designation,Primary_Expertise=PrimaryExpertise,Primary_Expertise1=AlternateExpertise1,Primary_Expertise2=AlternateExpertise2,Highest_Education=HighestEducation,Gender=gender,DOB=DOB,Message_Open=MessageOpen,
                 Responded=Responded,Linked_Clicked=LinkClicked,Source=Source,Org_Name=OrgName,Nature_Of_Business=NatureOfBusiness,Org_Name_Location=OrgLocation,Do_Not_Call=DoNotCall,Do_Not_Message=DoNotMessage,Do_Not_Mail=DoNotMail,Do_Not_Whatsapp=DoNotWhatsapp,Do_Not_Disturb=DoNotDisturb,Notes1=Notes1,Notes2=Notes2,Notes3=Notes3,Notes4=Notes4,Notes5=Notes5,Remarks=Remark,Document_Attach=DocumentAttach,Called=Called,Met=Met,Full_Name=FullName,Out_Of_Station=OutOfStation,Out_Of_Country=OutOfCountry,Generated_Pincode=GeneratedPinCode,Mark_For_Deletion=MarkForDeletion,Reason_For_Deletion=ReasonForDeletion,Blog_Link=BigLink,Website=Website,Linkedin_Link=LinkedinLink,Instagram_Link=nstagramLink,Youtube_Link=YoutubeLink,Facebook_Link=FacebookLink,Social_Media_Other=SocialMediaOther,Created_By=FullName
                 )
        u.save()
        messages.success(request, 'you are successfully Registered')
    return redirect('/showuser')

def Showdata(request):
    u = UserData.objects.all()
    return render(request, 'showdata.html',{'u':u})