# Generated by Django 3.2.6 on 2023-04-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group1', models.CharField(blank=True, max_length=12, null=True)),
                ('Group2', models.CharField(blank=True, max_length=12, null=True)),
                ('Group3', models.CharField(blank=True, max_length=12, null=True)),
                ('Group4', models.CharField(blank=True, max_length=12, null=True)),
                ('Group5', models.CharField(blank=True, max_length=12, null=True)),
                ('Group6', models.CharField(blank=True, max_length=12, null=True)),
                ('Group7', models.CharField(blank=True, max_length=12, null=True)),
                ('Group8', models.CharField(blank=True, max_length=12, null=True)),
                ('Group9', models.CharField(blank=True, max_length=12, null=True)),
                ('Group10', models.CharField(blank=True, max_length=12, null=True)),
                ('Salutation', models.CharField(blank=True, max_length=4, null=True)),
                ('First_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Middle_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Primary_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Alternate_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Primary_Mail', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('Alternate_Mail', models.CharField(blank=True, max_length=80, null=True)),
                ('Location', models.CharField(blank=True, max_length=30, null=True)),
                ('City', models.CharField(blank=True, max_length=30, null=True)),
                ('State', models.CharField(blank=True, max_length=30, null=True)),
                ('Country', models.CharField(blank=True, max_length=30, null=True)),
                ('Pincode', models.CharField(blank=True, max_length=8, null=True)),
                ('Designation', models.CharField(blank=True, max_length=40, null=True)),
                ('Primary_Expertise', models.CharField(blank=True, max_length=30, null=True)),
                ('Primary_Expertise1', models.CharField(blank=True, max_length=30, null=True)),
                ('Primary_Expertise2', models.CharField(blank=True, max_length=30, null=True)),
                ('Highest_Education', models.CharField(blank=True, max_length=40, null=True)),
                ('Gender', models.CharField(blank=True, max_length=6, null=True)),
                ('DOB', models.CharField(blank=True, max_length=6, null=True)),
                ('Message_Open', models.CharField(blank=True, max_length=1, null=True)),
                ('Responded', models.CharField(blank=True, max_length=1, null=True)),
                ('Linked_Clicked', models.CharField(blank=True, max_length=1, null=True)),
                ('Source', models.CharField(blank=True, max_length=30, null=True)),
                ('Org_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Nature_Of_Business', models.CharField(blank=True, max_length=120, null=True)),
                ('Org_Name_Location', models.CharField(blank=True, max_length=20, null=True)),
                ('Do_Not_Call', models.CharField(blank=True, max_length=1, null=True)),
                ('Do_Not_Message', models.CharField(blank=True, max_length=1, null=True)),
                ('Do_Not_Mail', models.CharField(blank=True, max_length=1, null=True)),
                ('Do_Not_Whatsapp', models.CharField(blank=True, max_length=1, null=True)),
                ('Do_Not_Disturb', models.CharField(blank=True, max_length=1, null=True)),
                ('Notes1', models.CharField(blank=True, max_length=120, null=True)),
                ('Notes2', models.CharField(blank=True, max_length=120, null=True)),
                ('Notes3', models.CharField(blank=True, max_length=120, null=True)),
                ('Notes4', models.CharField(blank=True, max_length=120, null=True)),
                ('Notes5', models.CharField(blank=True, max_length=120, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('Document_Attach', models.ImageField(blank=True, null=True, upload_to='DocumentAttach')),
                ('Called', models.CharField(blank=True, max_length=1, null=True)),
                ('Met', models.CharField(blank=True, max_length=1, null=True)),
                ('Full_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Out_Of_Station', models.CharField(blank=True, max_length=1, null=True)),
                ('Out_Of_Country', models.CharField(blank=True, max_length=1, null=True)),
                ('Generated_Pincode', models.CharField(blank=True, max_length=8, null=True)),
                ('Mark_For_Deletion', models.CharField(blank=True, max_length=1, null=True)),
                ('Reason_For_Deletion', models.CharField(blank=True, max_length=30, null=True)),
                ('Blog_Link', models.CharField(blank=True, max_length=100, null=True)),
                ('Website', models.CharField(blank=True, max_length=100, null=True)),
                ('Linkedin_Link', models.CharField(blank=True, max_length=100, null=True)),
                ('Instagram_Link', models.CharField(blank=True, max_length=100, null=True)),
                ('Youtube_Link', models.CharField(blank=True, max_length=100, null=True)),
                ('Facebook_Link', models.CharField(blank=True, max_length=100, null=True)),
                ('Social_Media_Other', models.CharField(blank=True, max_length=100, null=True)),
                ('Created_By', models.CharField(blank=True, max_length=30, null=True)),
                ('Changed_By', models.CharField(blank=True, max_length=30, null=True)),
                ('created_Date', models.DateField(auto_now_add=True, null=True)),
                ('created_Time', models.DateTimeField(auto_now_add=True, null=True)),
                ('Changed_Date', models.DateField(auto_now=True, null=True)),
                ('Changed_Time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]