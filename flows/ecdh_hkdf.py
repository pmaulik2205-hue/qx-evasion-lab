"""R4-N2 Key agreement flow: ECDH P-256 shared secret -> HKDF -> AES-256-GCM key."""
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def session_encrypt(plaintext: bytes) -> bytes:
    alice = ec.generate_private_key(ec.SECP256R1())
    bob = ec.generate_private_key(ec.SECP256R1())
    shared = alice.exchange(ec.ECDH(), bob.public_key())
    key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"qx-session").derive(shared)
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)
