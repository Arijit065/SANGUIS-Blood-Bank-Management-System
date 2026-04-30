from django.db import models
from patient import models as pmodels
from donor import models as dmodels
from django.contrib.auth.models import User
class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    request_by_patient=models.ForeignKey(pmodels.Patient,null=True,on_delete=models.CASCADE)
    request_by_donor=models.ForeignKey(dmodels.Donor,null=True,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=30)
    patient_age=models.PositiveIntegerField()
    reason=models.CharField(max_length=500)
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=20,default="Pending")
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.bloodgroup


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=50, default="Alert") # "Alert", "Approval", "Warning", etc.
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"

class BloodDonationAppointment(models.Model):
    donor = models.ForeignKey(dmodels.Donor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50) # e.g. "10:00 AM - 11:00 AM"
    status = models.CharField(max_length=20, default="Scheduled") # "Scheduled", "Completed", "Cancelled"
    
    def __str__(self):
        return f"{self.donor.user.first_name} on {self.date} at {self.time_slot}"