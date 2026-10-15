"""R4-07 Unreachable RSA code (guarded by a constant False flag)."""
from cryptography.hazmat.primitives.asymmetric import rsa

ENABLE_LEGACY = False


def maybe_legacy_key():
    if ENABLE_LEGACY:
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return None
