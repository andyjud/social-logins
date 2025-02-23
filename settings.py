from environ import Env
env = Env()
env.read_env()


INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('OAUTH_GOOGLE_CLIENT_ID'),
            'secret': env('OAUTH_GOOGLE_SECRET'),
        },
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
            'prompt': 'consent'
        },
    },
    'github': {
        'APP': {
            'client_id': env('OAUTH_GITHUB_CLIENT_ID'),
            'secret': env('OAUTH_GITHUB_SECRET'),
        },
        'AUTH_PARAMS': {
            'prompt': 'consent',  
        },
    },
    'twitter': {
        'APP': {
            'client_id': env('OAUTH_TWITTER_CLIENT_ID'),
            'secret': env('OAUTH_TWITTER_SECRET'),
        },
    },
    'facebook': {
        'APP': {
            'client_id': env('OAUTH_FACEBOOK_CLIENT_ID'),
            'secret': env('OAUTH_FACEBOOK_SECRET'),
        },
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate',
        },
    },
}


SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_ADAPTER = "a_users.adapters.CustomAccountAdapter"
SOCIALACCOUNT_ADAPTER = "a_users.adapters.SocialAccountAdapter"
