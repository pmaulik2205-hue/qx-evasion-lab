"""R4-14 HOP 1 of 3: lowest-level primitive. Only this file names the algorithm."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


def _new_key():
    return ec.generate_private_key(ec.SECP256R1())


def raw_sign(data: bytes) -> bytes:
    return _new_key().sign(data, ec.ECDSA(hashes.SHA256()))
