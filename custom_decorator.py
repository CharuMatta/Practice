import functools

user = {'username':'charu', 'access_level':'admin'}

def make_secure(access_level): 
    def custum_decorator(func): #creating custom decorator
        @functools.wraps(func) #This takes a function used in a decorator and adds the functionality of copying over the function name, docstring, arguments list
        def secure_func():
            if user['access_level'] == access_level:
                return func()
            else:
                return f"No permisson for user {user['username']}"
        return secure_func 
    return custum_decorator


@make_secure("guest")
def get_guest_pass():
    return "guest:abc"

@make_secure("admin")
def get_admin_pass():
    return "admin:123"

print(get_guest_pass())
print(get_admin_pass())

user = {'username':'charu', 'access_level':'guest'}

print(get_admin_pass())
print(get_guest_pass())