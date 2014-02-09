from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

	def save_user(self, request, user, form, commit=True):
		user.phone = form.data.get('phone')
		super(AccountAdapter, self).save_user(request, user, form, commit)
