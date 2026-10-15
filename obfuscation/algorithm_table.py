"""R4-03 Algorithm picked from a lookup table at runtime (default = legacy RSA)."""
import os

from cryptography.hazmat.primitives.asymmetric import ec, rsa

KEY_FACTORIES = {
    "legacy": lambda: rsa.generate_private_key(public_exponent=65537, key_size=2048),
    "modern": lambda: ec.generate_private_key(ec.SECP256R1()),
}


def make_key():
    return KEY_FACTORIES[os.environ.get("QX_KEY_MODE", "legacy")]()
