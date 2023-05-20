

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import User

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = request.POST
        
        # Extract user data from request
        username = data.get('username')
        password = data.get('password')
        mobile = data.get('mobile')
        name = data.get('name')
        address = data.get('address')
        email = data.get('email')
        
        # Validate user data
        if not (username.isalpha() and len(mobile) == 10 and is_valid_email(email)):
            return JsonResponse({'error': 'Invalid user data'})
        
        # Save user data to the database
        user = User(username=username, password=password, mobile=mobile, name=name, address=address, email=email)
        user.save()
        
        # Trigger email with password details
        send_email(email, password)
        
        return JsonResponse({'user_id': user.id})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.POST
        
        # Extract login credentials from request
        username = data.get('username')
        password = data.get('password')
        
        # Validate login credentials against the database
        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'status': 'success'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'failure'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def select_users(request):
    # Retrieve all users from the database
    users = User.objects.all().values()
    
    return JsonResponse(list(users), safe=False)

def is_valid_email(email):
    # Implement email validation logic here
    pass

def send_email(email, password):
    # Implement email sending logic here
    pass
