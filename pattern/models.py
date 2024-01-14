from django.db import models
from django.contrib.auth.models import User

# Pattern view ERD 
#  ____________________
# |Name of Pattern_____|    X  
# |Image(s)____________|    - 
# |Pattern notes_______|    X 
# |Published by User___| F  X
# |Date published _____|    X
# |Category of Pattern_|    x
# |Yarn Weight_________|    x
# |Gauge_______________|    -
# |Needle size_________|    X
# |Yardage_____________|    -
# |Suggested Wool______|    -
# |Pattern sizes_______|    -
# |Tags________________|    -

STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, ''), (1, 'Sweater'), (2, 'Cardigan'), (3, 'Skirt'), (4, 'Pants'), (5, 'Hat'), (6, 'Scarf'))
WEIGHT = ((0, 'Cobweb'), (1, 'Lace'), (2, 'Fingering'), (3, 'DK'), (4, 'Worsted'))
NEEDLE = ((0, '1mm'), (1, '2mm'), (2, '3mm'), (3, '4mm'))


class Pattern(models.Model):
    #Pattern title
    title = models.CharField(max_length=200, unique=True)
    #Slug for URL
    slug = models.SlugField(max_length=200, unique=True)
    #Pattern posted by
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    #Pattern notes
    content = models.TextField()
    #Post created on
    created_on = models.DateTimeField(auto_now_add=True)
    #Pattern first published
    first_published = models.DateField()
    #Pattern category
    category = models.IntegerField(choices=CATEGORY, default=0)
    #Yarn Weight
    weight = models.IntegerField(choices=WEIGHT, default=0)
    #Needle size
    needle = models.IntegerField(choices=NEEDLE, default=0)
