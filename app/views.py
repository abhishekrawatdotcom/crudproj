from django.shortcuts import render
import csv
# Create your views here.

from django.core.paginator import Paginator

from .forms import UserForm
from app.models import UserData
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
import io
from django.http import HttpResponse
import xlsxwriter
from django.db import models



def ShowPage(request):
    return render(request,'stuhome.html')


def add_book(request):
    if request.method == 'POST':
        group1 = request.POST.get("group1",'')
        group2 = request.POST.get("group2",'')
        group3 = request.POST.get("group3",'')
        group4 = request.POST.get("group4",'')
        group5 = request.POST.get("group5",'')
        group6 = request.POST.get("group6",'')
        group7 = request.POST.get("group7",'')
        group8 = request.POST.get("group8",'')
        group9 = request.POST.get("group9",'')
        group10 = request.POST.get("group10",'')
        Salutation = request.POST.get("Salutation",'')
        firstname = request.POST.get("firstname",'')
        middlename = request.POST.get("middlename",'')
        lastname = request.POST.get("lastname",'')
        primarynumber = request.POST.get("primarynumber",'')
        alternatenumber = request.POST.get("alternatenumber",'')
        PrimaryMail = request.POST.get("PrimaryMail",'')
        AlternateMail = request.POST.get("AlternateMail",'')
        location = request.POST.get("location",'')
        city = request.POST.get("city",'')
        state = request.POST.get("state",'')
        country = request.POST.get("country",'')
        pincode = request.POST.get("pincode",'')
        Designation = request.POST.get("Designation",'')
        PrimaryExpertise = request.POST.get("PrimaryExpertise",'')
        AlternateExpertise1 = request.POST.get("AlternateExpertise1",'')
        AlternateExpertise2 = request.POST.get("AlternateExpertise2",'')
        HighestEducation = request.POST.get("HighestEducation",'')
        gender = request.POST.get("gender",'')
        DOB = request.POST.get("DOB",'')
        MessageOpen = request.POST.get("MessageOpen",'')
        Responded = request.POST.get("Responded",'')
        LinkClicked = request.POST.get("LinkClicked",'')
        Source = request.POST.get("Source",'')
        OrgName = request.POST.get("OrgName",'')
        NatureOfBusiness = request.POST.get("NatureOfBusiness",'')
        OrgLocation = request.POST.get("OrgLocation",'')
        DoNotCall = request.POST.get("DoNotCall",'')
        DoNotMessage = request.POST.get("DoNotMessage",'')
        DoNotMail = request.POST.get("DoNotMail",'')
        DoNotWhatsapp = request.POST.get("DoNotWhatsapp",''),
        DoNotDisturb = request.POST.get("DoNotDisturb",'')
        Notes1 = request.POST.get("Notes1",'')
        Notes2 = request.POST.get("Notes2",'')
        Notes3 = request.POST.get("Notes3",'')
        Notes4 = request.POST.get("Notes4",'')
        Notes5 = request.POST.get("Notes5",'')
        Remark = request.POST.get("Remark",'')
        DocumentAttach = request.FILES.get("DocumentAttach",'')
        Called = request.POST.get("Called",'')
        Met = request.POST.get("Met",'')
        FullName = firstname + " " + middlename + " " + lastname
        OutOfStation = request.POST.get("OutOfStation",'')
        OutOfCountry = request.POST.get("OutOfCountry",'')
        GeneratedPinCode = request.POST.get("GeneratedPinCode",'')
        MarkForDeletion = request.POST.get("MarkForDeletion",'')
        ReasonForDeletion = request.POST.get("ReasonForDeletion",'')
        BigLink = request.POST.get("BigLink",'')
        Website = request.POST.get("Website",'')
        LinkedinLink = request.POST.get("LinkedinLink",'')
        nstagramLink = request.POST.get("nstagramLink",'')
        YoutubeLink = request.POST.get("YoutubeLink",'')
        FacebookLink = request.POST.get("FacebookLink",'')
        SocialMediaOther = request.POST.get("SocialMediaOther",'')
        EnterBy = request.POST.get("EnterBy",'')
        Changedate = request.POST.get("Changedate",'')
        Changetime = request.POST.get("Changetime",'')

        u = UserData(Group1=group1,Group2=group2,Group3=group3,Group4=group4,Group5=group5,Group6=group6,Group7=group7,Group8=group8,Group9=group9,Group10=group10,Salutation=Salutation,
                 First_Name=firstname,Middle_Name=middlename,Last_Name=lastname,Primary_Number=primarynumber,Alternate_Number=alternatenumber,Primary_Mail=PrimaryMail,Alternate_Mail=AlternateMail,Location=location,City=city,State=state,Country=country,Pincode=pincode,Designation=Designation,Primary_Expertise=PrimaryExpertise,Primary_Expertise1=AlternateExpertise1,Primary_Expertise2=AlternateExpertise2,Highest_Education=HighestEducation,Gender=gender,DOB=DOB,Message_Open=MessageOpen,
                 Responded=Responded,Linked_Clicked=LinkClicked,Source=Source,Org_Name=OrgName,Nature_Of_Business=NatureOfBusiness,Org_Name_Location=OrgLocation,Do_Not_Call=DoNotCall,Do_Not_Message=DoNotMessage,Do_Not_Mail=DoNotMail,Do_Not_Whatsapp=DoNotWhatsapp,Do_Not_Disturb=DoNotDisturb,Notes1=Notes1,Notes2=Notes2,Notes3=Notes3,Notes4=Notes4,Notes5=Notes5,Remarks=Remark,Document_Attach=DocumentAttach,Called=Called,Met=Met,Full_Name=FullName,Out_Of_Station=OutOfStation,Out_Of_Country=OutOfCountry,Generated_Pincode=GeneratedPinCode,Mark_For_Deletion=MarkForDeletion,Reason_For_Deletion=ReasonForDeletion,Blog_Link=BigLink,Website=Website,Linkedin_Link=LinkedinLink,Instagram_Link=nstagramLink,Youtube_Link=YoutubeLink,Facebook_Link=FacebookLink,Social_Media_Other=SocialMediaOther,Created_By=FullName,Entered_By=EnterBy,
                     Changed_Date=Changedate,Changed_Time=Changetime
                 )
        u.save()
        messages.success(request, 'you are successfully Registered')
    return redirect('/showuser')

def Showdata(request):
    my_objects = UserData.objects.all()
    paginator = Paginator(my_objects,10)  # Display 25 objects per page
    page_number = request.GET.get('page')
    u = paginator.get_page(page_number)
    return render(request, 'showdata.html',{'u':u})

def editdata(request,id):
    udata = UserData.objects.get(id=id)
    return render(request,'Edituserdetail.html',{'udata':udata})


def Update_Book(request,id):
    print('1111111111111111111111')
    u = UserData.objects.get(id=id)
    u.Group1 = request.POST.get("group11")
    print('u.group1',u.Group1)
    u.Group2 = request.POST.get("group21",'')
    u.Group3 = request.POST.get("group31",'')
    u.Group4 = request.POST.get("group41",'')
    u.Group5 = request.POST.get("group51",'')
    u.Group6 = request.POST.get("group61",'')
    u.Group7 = request.POST.get("group71",'')
    u.Group8 = request.POST.get("group81",'')
    u.Group9 = request.POST.get("group91",'')
    u.Group10 = request.POST.get("group101",'')
    u.Salutation = request.POST.get("Salutation1",'')
    u.First_Name = request.POST.get("firstname1",'')
    u.Middle_Name = request.POST.get("middlename1",'')
    u.Last_Name = request.POST.get("lastname1",'')
    u.Primary_Number = request.POST.get("primarynumber1",'')
    u.Alternate_Number = request.POST.get("alternatenumber1",'')
    u.Primary_Mail = request.POST.get("PrimaryMail1",'')
    u.Alternate_Mail = request.POST.get("AlternateMail1",'')
    u.Location = request.POST.get("location1",'')
    u.City = request.POST.get("city1",'')
    u.State = request.POST.get("state1",'')
    u.Country = request.POST.get("country1",'')
    u.Pincode = request.POST.get("pincode1",'')
    u.Designation = request.POST.get("Designation1",'')
    u.Primary_Expertise = request.POST.get("PrimaryExpertise1",'')
    u.Primary_Expertise1 = request.POST.get("AlternateExpertise11",'')
    u.Primary_Expertise2 = request.POST.get("AlternateExpertise21",'')
    u.Highest_Education = request.POST.get("HighestEducation1",'')
    u.Gender = request.POST.get("gender1",'')
    u.DOB = request.POST.get("DOB1",'')
    u.Message_Open = request.POST.get("MessageOpen1",'')
    u.Responded = request.POST.get("Responded1",'')
    u.Linked_Clicked = request.POST.get("LinkClicked1",'')
    u.Source = request.POST.get("Source1",'')
    u.Org_Name = request.POST.get("OrgName1",'')
    u.Nature_Of_Business = request.POST.get("NatureOfBusiness1",'')
    u.Org_Name_Location = request.POST.get("OrgLocation1",'')
    u.Do_Not_Call = request.POST.get("DoNotCall1",'')
    u.Do_Not_Message = request.POST.get("DoNotMessage1",'')
    u.Do_Not_Mail = request.POST.get("DoNotMail1",'')
    u.Do_Not_Whatsapp = request.POST.get("DoNotWhatsapp1",'')
    u.Do_Not_Disturb = request.POST.get("DoNotDisturb1",'')
    u.Notes1 = request.POST.get("Notes11",'')
    u.Notes2 = request.POST.get("Notes21",'')
    u.Notes3 = request.POST.get("Notes31",'')
    u.Notes4 = request.POST.get("Notes41",'')
    u.Notes5 = request.POST.get("Notes51",'')
    u.Remarks = request.POST.get("Remark1",'')
    doc5 = request.FILES.get("DocumentAttach1")
    if doc5 == None:
        u.Document_Attach = u.Document_Attach
    else:
        u.Document_Attach = request.FILES.get("DocumentAttach1")
    u.Called = request.POST.get("Called1",'')
    u.Met = request.POST.get("Met1",'')
    u.Full_Name = request.POST.get("firstname1") + " " + request.POST.get("middlename1") + " " + request.POST.get("lastname1")
    u.Out_Of_Station = request.POST.get("OutOfStation1",'')
    u.Out_Of_Country = request.POST.get("OutOfCountry1",'')
    u.Generated_Pincode = request.POST.get("GeneratedPinCode1",'')
    u.Mark_For_Deletion = request.POST.get("MarkForDeletion1",'')
    u.Reason_For_Deletion = request.POST.get("ReasonForDeletion1",'')
    u.Blog_Link = request.POST.get("BigLink1",'')
    u.Website = request.POST.get("Website1",'')
    u.Linkedin_Link = request.POST.get("LinkedinLink1",'')
    u.Instagram_Link = request.POST.get("nstagramLink1",'')
    u.Youtube_Link = request.POST.get("YoutubeLink1")
    u.Facebook_Link = request.POST.get("FacebookLink1",'')
    u.Social_Media_Other = request.POST.get("SocialMediaOther1",'')
    u.Created_By = u.Created_By
    u.Entered_By = request.POST.get("EnterBy1",'')
    u.Changed_Date = request.POST.get("Changedate1",'')
    u.Changed_Time = request.POST.get("Changetime1",'')
    u.save()
    print('yess savingg')
    return redirect('/Showdata')




# def update_user(request, id):
#     user = get_object_or_404(UserData, pk=id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('/Showdata',)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'updatefields.html', {'form': form})

def export_data_to_excel(request):
    # Create a new workbook and add a worksheet
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Write the header row
    header_row = [field.name for field in UserData._meta.fields]
    for col_num, value in enumerate(header_row):
        worksheet.write(0, col_num, value)

    # Write the data rows
    queryset = UserData.objects.all()
    for row_num, obj in enumerate(queryset, start=1):
        row = []
        for field in UserData._meta.fields:
            value = getattr(obj, field.name)
            if isinstance(field, models.ImageField):
                # If the field is an image, convert it to a string representation
                if value:
                    value = str(value)
                else:
                    value = ''
            row.append(value)
        for col_num, value in enumerate(row):
            worksheet.write(row_num, col_num, value)

    # Close the workbook and export the data
    workbook.close()
    output.seek(0)

    response = HttpResponse(output.read(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    return response




