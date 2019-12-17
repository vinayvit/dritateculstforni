from django.contrib import admin
from .models import Post
from .models import Result
from .models import Answer
from .models import Admit
from .models import Admission
from .models import Important

admin.site.register(Post)
admin.site.register(Admit)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Admission)
admin.site.register(Important)