# My Personal Blog

My personal blog source code
I am using Django for this project.
In this project I am created Superuser,
Homepage for blogs, Post detail,post list,js validation,
sqlite3 use as a database.

Interecting with databse 

python3 manage.py shell

from myapp.models import Post

# Create a new post
post = Post(title='My First Post', content='This is the content of the post.')
post.save()

# Query all posts
all_posts = Post.objects.all()

# Query a specific post
specific_post = Post.objects.get(id=1)

# Update a post
specific_post.title = 'Updated Post Title'
specific_post.save()

# Delete a post
specific_post.delete()
