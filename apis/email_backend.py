import ssl
from django.core.mail.backends.smtp import EmailBackend as SmtpEmailBackend
import certifi

class CustomSSLEmailBackend(SmtpEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Create an SSL context that uses certifi or unverified context if cert verification fails
        try:
            context = ssl.create_default_context(cafile=certifi.where())
        except Exception:
            context = ssl._create_unverified_context()
        
        # Disable certificate hostname verification fallback if needed
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        self.ssl_context = context
