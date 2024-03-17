from django.db.models import Model, CharField, BooleanField, TextField, ForeignKey, CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Blog(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    titel = CharField(max_length=100)
    description = TextField()
    category = CharField(max_length=20, choices=(
        ('Python', 'Python'), 
        ('Data Alalysis', 'Data Alalysis'), 
        ('Data Science', 'Data Science'), 
        ('React', 'React'), 
        ('MERN', 'MERN')
    ))
    publish = BooleanField()



# <form method="POST" action="">
#     <div class="form-group">
#         {% csrf_token %}
#         {{form.as_p}}
#     </div>
# </form>
