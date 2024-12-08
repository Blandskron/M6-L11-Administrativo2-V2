from django.contrib.auth.models import User

def create_test_user():
    username = 'testuser'
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username, 'testuser@example.com', 'testpassword')
        user.first_name = 'Test'
        user.last_name = 'User'
        user.save()
        print(f'User "{username}" created successfully.')
    else:
        print(f'User "{username}" already exists.')
