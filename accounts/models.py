from django.db import models
from base.models import BaseModole
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_active_account_email


class Profile(BaseModole):

    user = models.OneToOneField(User , on_delete=models.CASCADE, blank=True , null=True ,related_name='profile')
    email_verifcation = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.user.username



@receiver(post_save, sender = User)
def send_email_token(sender,instance, created, **kwargs):

    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(
                user= instance,
                email_token = email_token
            )
            
            email = instance.email
            first_name = instance.first_name
            send_active_account_email(email , email_token, first_name)

    except Exception as ex:
        print(ex)

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)


class profileDetails(BaseModole):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_detais_user' , blank=True, null=True) 
    First_name =models.CharField(max_length=100)
    Last_name =models.CharField(max_length=100)
    city_name = models.CharField(max_length=100 , blank=True , null=True , default=" ")
    sate_name = models.CharField( max_length=100)
    Addresses =models.CharField(max_length=100)
    pincode =models.IntegerField()
    profile_image = models.ImageField(upload_to='profile_picture',blank=True, null=True)

    def __str__(self):
        return f'{self.First_name} {self.Last_name} {self.udid}' 
