from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from donor.models import Donor, BloodDonate
from patient.models import Patient
from blood.models import Stock, BloodRequest
import random

class Command(BaseCommand):
    help = 'Seeds the database with 100 Donors, 50 Patients, 500 Blood Donations, Random Blood Requests'

    def handle(self, *args, **kwargs):
        blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
        diseases = ['None', 'Diabetes', 'Hypertension', 'Asthma']

        # Ensure groups exist
        donor_group, _ = Group.objects.get_or_create(name='DONOR')
        patient_group, _ = Group.objects.get_or_create(name='PATIENT')

        # Create Stocks if empty
        if Stock.objects.count() == 0:
            for bg in blood_groups:
                Stock.objects.create(bloodgroup=bg, unit=0)

        self.stdout.write("Creating 100 Donors...")
        donors = []
        for i in range(100):
            user = User.objects.create_user(
                username=f'donor_{i}',
                password='password123',
                first_name=f'Donor{i}',
                last_name='Test'
            )
            donor_group.user_set.add(user)
            donor = Donor.objects.create(
                user=user,
                bloodgroup=random.choice(blood_groups),
                address=f'City {random.randint(1, 20)}',
                mobile=f'9876543{random.randint(100, 999)}',
                profile_pic='profile_pic/Donor/1.jpg'
            )
            donors.append(donor)

        self.stdout.write("Creating 50 Patients...")
        patients = []
        for i in range(50):
            user = User.objects.create_user(
                username=f'patient_{i}',
                password='password123',
                first_name=f'Patient{i}',
                last_name='Test'
            )
            patient_group.user_set.add(user)
            patient = Patient.objects.create(
                user=user,
                bloodgroup=random.choice(blood_groups),
                address=f'City {random.randint(1, 20)}',
                mobile=f'9876543{random.randint(100, 999)}',
                disease=random.choice(diseases),
                age=random.randint(18, 70),
                profile_pic='profile_pic/Patient/1.jpg'
            )
            patients.append(patient)

        self.stdout.write("Creating 500 Blood Donations...")
        for i in range(500):
            donor = random.choice(donors)
            status = random.choice(['Pending', 'Approved', 'Rejected'])
            donation = BloodDonate.objects.create(
                donor=donor,
                disease=random.choice(diseases),
                age=random.randint(18, 60),
                bloodgroup=donor.bloodgroup,
                unit=random.randint(1, 2),
                status=status
            )
            if status == 'Approved':
                stock = Stock.objects.get(bloodgroup=donor.bloodgroup)
                stock.unit += donation.unit
                stock.save()

        self.stdout.write("Creating Random Blood Requests...")
        for i in range(200):
            patient = random.choice(patients)
            status = random.choice(['Pending', 'Approved', 'Rejected'])
            req = BloodRequest.objects.create(
                patient=patient,
                patient_name=patient.user.first_name,
                patient_age=patient.age,
                reason='Surgery',
                bloodgroup=patient.bloodgroup,
                unit=random.randint(1, 3),
                status=status
            )
            if status == 'Approved':
                stock = Stock.objects.get(bloodgroup=patient.bloodgroup)
                if stock.unit >= req.unit:
                    stock.unit -= req.unit
                    stock.save()
                else:
                    req.status = 'Rejected'
                    req.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
