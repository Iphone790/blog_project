# How to make dropdown choice field:
# ----------------------------------
# STATUS_CHOICES=(('for python values', 'End user display value'))
# STATUS_CHOICES=(('draft', 'Draft'),('published', 'Published'))
# status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

# slug_field:
# seo
# to build proper urls

# slug= models.SlugField(max_length=256, unique_for_date='publish')

# author=models.ForeignKey(User, related_name='blog_posts')
# the value of author must be one of User in default auth application

# You can give example of your blog application you developed use foreign key for many to one relation.

# class Post(models.Model):
#     author=models.ForeignKey(User, related_name='blog_post')


DateTimeField(default=timezpne.now)





