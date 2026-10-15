"""R4-01 RSA through an aliased module name."""
from cryptography.hazmat.primitives.asymmetric import rsa as _kp
from cryptography.hazmat.primitives import hashes as _h
from cryptography.hazmat.primitives.asymmetric import padding as _p

_key = _kp.generate_private_key(public_exponent=65537, key_size=2048)
_sig = _key.sign(b"order-77", _p.PKCS1v15(), _h.SHA256())
