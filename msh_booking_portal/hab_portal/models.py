import os
from django.db import models
from django.core.exceptions import ValidationError
from users.models import SiteUser
from .storage import OverwriteStorage
from django.contrib.auth.models import User
from datetime import datetime
from .storage import OverwriteStorage


HOSTELS = [
    ('lohit', 'Lohit'),
    ('brahmaputra', 'Brahmaputra'),
    ('siang', 'Siang'),
    ('manas', 'Manas'),
    ('disang', 'Disang'),
    ('kameng', 'Kameng'),
    ('umiam', 'Umiam'),
    ('barak', 'Barak'),
    ('kapili', 'Kapili'),
    ('dihing', 'Dihing'),
    ('subansiri', 'Subansiri'),
    ('dhansiri', 'Dhansiri'),
    ('msh', 'Married Scholar Hostel'),
]

STATUS = [
    ('Accepted','Accepted'),
    ('Pending','Pending'),
    ('Declined','Declined'),
]

def upload_file_name(instance, filename):
    return 'hab_portal/user_{0}.pdf'.format(instance.user.pk)


def validate_file_size(value):
    size = value.size

    if size <= 10*1024**2:
        return value
    else:
        raise ValidationError('The maximum file size is 10 MB.')


def validate_file_extension(value):
    if os.path.splitext(value.name)[-1] == '.pdf':
        return value
    else:
        raise ValidationError('Upload a PDF File.')


def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


def upload_file_name(instance, filename):
    return 'hab_portal/user_{0}.pdf'.format(instance.user.pk)


def validate_file_size(value):
    size = value.size

    if size <= 10*1024**2:
        return value
    else:
        raise ValidationError('The maximum file size is 10 MB.')


def validate_file_extension(value):
    if os.path.splitext(value.name)[-1] == '.pdf':
        return value
    else:
        raise ValidationError('Upload a PDF File.')


HAB_FIELDS = {'roll_number': 'roll_number',
              'hostel': 'hostel'}


class HABModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True)
    name = models.CharField('Name', max_length=256)
    email = models.EmailField('Email', max_length=500)
    department = models.CharField('Department', max_length=256)

    time_of_submission = models.DateTimeField(auto_now_add=True, null=True)

    roll_number = models.IntegerField('Roll No.')
    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS)

    date_of_arrival = models.DateField('Date of Arrival', default=get_current_date)

    fee_to_be_paid = models.IntegerField('Fee to be Paid', default=0)

    fee_paid = models.IntegerField('Fee Paid', null=True)
    date_of_payment = models.DateField('Date of Payment')
    fee_receipt = models.FileField('Fee Receipt', upload_to=upload_file_name, storage=OverwriteStorage(),
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.')

    approved = models.BooleanField(default=False)

    locked = models.BooleanField(default=False)
    status = models.CharField(max_length=256, choices=STATUS, default='Pending', null=True) 

    class Meta:
        ordering = ['hostel','-status','date_of_arrival']
        permissions = (
            ('can_view_lohit_hostel_data', 'can view lohit hostel data'),
            ('can_view_brahma_hostel_data', 'can view brahma hostel data'),
            ('can_view_siang_hostel_data', 'can view siang hostel data'),
            ('can_view_manas_hostel_data', 'can view manas hostel data'),
            ('can_view_disang_hostel_data', 'can view disang hostel data'),
            ('can_view_kameng_hostel_data', 'can view kameng hostel data'),
            ('can_view_umiam_hostel_data', 'can view umiam hostel data'),
            ('can_view_barak_hostel_data', 'can view barak hostel data'),
            ('can_view_kapili_hostel_data', 'can view kapili hostel data'),
            ('can_view_dihing_hostel_data', 'can view dihing hostel data'),
            ('can_view_suban_hostel_data', 'can view subansiri hostel data'),
            ('can_view_dhan_hostel_data', 'can view dhansiri hostel data'),
            ('can_view_msh_hostel_data', 'can view msh hostel data'),
        )

    def __str__(self):
        return self.user.user.first_name+" "+self.user.user.last_name


