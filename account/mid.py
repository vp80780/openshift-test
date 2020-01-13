class Role:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):

        request.role = []
        if request.user.is_authenticated:
            group = request.user.groups.all()
            if group:
                request.role = list(group.values_list('name', flat=True))

    def process_exception(self, request, exception):
        pass
