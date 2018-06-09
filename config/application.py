''' Application Settings '''

import os

'''
|--------------------------------------------------------------------------
| Application Name
|--------------------------------------------------------------------------
|
| This value is the name of your application. This value is used when the
| framework needs to place the application's name in a notification or
| any other location as required by the application or its packages.
|
'''

NAME = 'Masonite 2.0'

'''
|--------------------------------------------------------------------------
| Application Debug Mode
|--------------------------------------------------------------------------
|
| When your application is in debug mode, detailed error messages with
| stack traces will be shown on every error that occurs within your
| application. If disabled, a simple generic error page is shown
|
'''

DEBUG = os.getenv('APP_DEBUG', 'False')

'''
|--------------------------------------------------------------------------
| Secret Key
|--------------------------------------------------------------------------
|
| This key is used to encrypt and decrypt various values. Out of the box
| Masonite uses this key to encrypt or decrypt cookies so you can use
| it to encrypt and decrypt various values using the Masonite Sign
| class. Read the documentation on Encryption to find out how.
|
'''

KEY = os.getenv('KEY', None)

'''
|--------------------------------------------------------------------------
| Application URL
|--------------------------------------------------------------------------
|
| Sets the root URL of the application. This is primarily used for testing
|
'''

URL = 'http://localhost:8000'

'''
|--------------------------------------------------------------------------
| Providers List
|--------------------------------------------------------------------------
|
| Providers are a simple way to remove or add functionality for Masonite
| The providers in this list are either ran on server start or when a
| request is made depending on the provider. Take some time to can
| learn more more about Service Providers in our documentation
|
'''

PROVIDERS = [
    # Framework Providers
    'masonite.providers.AppProvider',
    'masonite.providers.SessionProvider',
    'masonite.providers.RouteProvider',
    # 'entry.providers.ApiProvider.ApiProvider',
    'masonite.providers.StatusCodeProvider',
    'masonite.providers.StartResponseProvider',
    'masonite.providers.WhitenoiseProvider',
    'masonite.providers.ViewProvider',

    # Optional Framework Providers
    'masonite.providers.MailProvider',
    'masonite.providers.UploadProvider',
    'masonite.providers.HelpersProvider',
    'masonite.providers.QueueProvider',
    'masonite.providers.BroadcastProvider',
    'masonite.providers.CacheProvider',
    'masonite.providers.CsrfProvider',
    'masonite.providers.SassProvider',
    'scheduler.providers.ScheduleProvider',

    # Third Party Providers

    # Application Providers
    'app.providers.UserModelProvider.UserModelProvider',
    'app.providers.MiddlewareProvider.MiddlewareProvider',
]

'''
|--------------------------------------------------------------------------
| Base Directory
|--------------------------------------------------------------------------
|
| Sets the root path of your project
|
'''

BASE_DIRECTORY = os.getcwd()

'''
|--------------------------------------------------------------------------
| Static Root
|--------------------------------------------------------------------------
|
| Set the static root of your application that you wil use to store assets
|
'''

STATIC_ROOT = os.path.join(BASE_DIRECTORY, 'storage')

'''
|--------------------------------------------------------------------------
| Autoload Directories
|--------------------------------------------------------------------------
|
| List of directories that are used to find classes and autoload them into 
| the Service Container. This is initially used to find models and load
| them in but feel free to autoload any directories
|
'''

AUTOLOAD = [
    'app',
]
