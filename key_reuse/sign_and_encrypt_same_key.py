"""R4-15 KEY MISUSE: the same RSA key (copied from qx-key-service) is used to sign AND to encrypt."""
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

KEY = serialization.load_pem_private_key(
    (Path(__file__).parent / "copied_rsa_signing_private.pem").read_bytes(), password=None)


def sign(data: bytes) -> bytes:
    return KEY.sign(data, padding.PKCS1v15(), hashes.SHA256())


def encrypt(data: bytes) -> bytes:
    return KEY.public_key().encrypt(
        data, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
