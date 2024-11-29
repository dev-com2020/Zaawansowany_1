from django.views import View

class MyView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

methods = [method for method in dir(MyView) if callable(getattr(MyView, method)) and not method.startswith("_")]
print(methods)
