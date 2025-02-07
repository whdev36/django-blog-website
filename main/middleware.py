from django.http import HttpResponseForbidden

class RestrictAdminMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		self.allowed_ips = ['127.0.0.1', '222.80.222.222', '90.60.200.140']  # set your ip addres

	def __call__(self, request):
		ip = request.META.get('HTTP_X_FORWARDED_FOR')
		if ip:
			ip = ip.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')

		print(ip)

		if request.path.startswith('/admin') and ip not in self.allowed_ips:
			return HttpResponseForbidden('Access to the admin panel is prohibited!')

		return self.get_response(request)
