import os

# The port the proxy will listen on (default is 443)
PORT = int(os.getenv("PORT", 443))

def parse_users(env_val):
    """
    Parse the USERS environment variable string into a dictionary.
    Expected format of USERS string: "username1=secret1,username2=secret2"
    Returns a dict: { "username1": "secret1", "username2": "secret2" }
    """
    users = {}
    if env_val:
        pairs = env_val.split(",")
        for p in pairs:
            if "=" in p:
                name, secret = p.split("=", 1)
                users[name.strip()] = secret.strip()
    return users

# Get users from the USERS environment variable or use a default user if not set
USERS = parse_users(os.getenv("USERS")) or {
    "tg": "00000000000000000000000000000001"
}

# Proxy operating modes
MODES = {
    # Classic mode - easy to detect
    "classic": os.getenv("MODE_CLASSIC", "False") == "True",

    # Secure mode - harder to detect, may be incompatible with very old clients
    "secure": os.getenv("MODE_SECURE", "False") == "True",

    # TLS mode - hardest to detect, may be incompatible with very old clients
    "tls": os.getenv("MODE_TLS", "True") == "True"
}

# The domain used in TLS mode, where bad clients are proxied
# Use a random existing domain; the proxy checks it on start
TLS_DOMAIN = os.getenv("TLS_DOMAIN", None)
# Example:
# TLS_DOMAIN = "www.google.com"

# Advertising tag obtained from @MTProxybot
AD_TAG = os.getenv("AD_TAG", None)
# Example:
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
