from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from cloudinary.models import CloudinaryField
from upload_validator import FileTypeValidator

# Pattern view ERD 
#  ____________________
# |Name of Pattern_____|    X  
# |Image_______________|    x
# |Pattern PDF_________|    X
# |Pattern notes_______|    X 
# |Published by User___| F  X
# |Date published _____|    X
# |Category of Pattern_|    x
# |Yarn Weight_________|    x
# |Needle size_________|    X


class Pattern(models.Model):
    CATEGORY = (
        (0, ''), 
        (1, 'Sweater'), 
        (2, 'Cardigan'), 
        (3, 'Skirt'), 
        (4, 'Pants'), 
        (5, 'Hat'), 
        (6, 'Scarf')
        )
    WEIGHT = (
        (0, 'Cobweb'), 
        (1, 'Lace'), 
        (2, 'Fingering'), 
        (3, 'DK'), 
        (4, 'Worsted')
        )
    NEEDLE = (
        (0, '1mm'), 
        (1, '2mm'), 
        (2, '3mm'), 
        (3, '4mm')
        )
    #Pattern title
    title = models.CharField(max_length=200, unique=True)
    #Pattern posted by
    author = models.ForeignKey(
    User, 
    on_delete=models.CASCADE, 
    )
    #Pattern notes
    content = models.TextField()
    #Post created on
    created_on = models.DateTimeField(auto_now=True)
    #Pattern category
    category = models.IntegerField(choices=CATEGORY, default=0)
    #Yarn Weight
    weight = models.IntegerField(choices=WEIGHT, default=0)
    #Needle size
    needle = models.IntegerField(choices=NEEDLE, default=0)
    # Image
    image = ImageField(upload_to='media/')
    # PDF
    pdf = models.FileField(upload_to='pdfs/', blank=True)
    # Link to Pattern
    link_pattern = models.CharField(blank=True)
        
