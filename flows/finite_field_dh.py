"""R4-N3 Classic finite-field Diffie-Hellman (2048-bit group)."""
from cryptography.hazmat.primitives.asymmetric import dh

PARAMS = dh.generate_parameters(generator=2, key_size=2048)


def agree() -> bytes:
    a = PARAMS.generate_private_key()
    b = PARAMS.generate_private_key()
    return a.exchange(b.public_key())
