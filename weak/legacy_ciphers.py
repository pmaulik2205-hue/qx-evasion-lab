"""R4-12 Weak / deprecated crypto: RSA-1024, SHA-1 signature, MD5, 3DES, AES-ECB, hardcoded AES key + static IV."""
import hashlib

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.decrepit.ciphers.algorithms import TripleDES

HARDCODED_AES_KEY = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
STATIC_IV = b"\x00" * 16


def weak_rsa_sha1(data: bytes) -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    return key.sign(data, padding.PKCS1v15(), hashes.SHA1())


def md5_fingerprint(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def aes_ecb(data: bytes) -> bytes:
    enc = Cipher(algorithms.AES(HARDCODED_AES_KEY), modes.ECB()).encryptor()
    return enc.update(data) + enc.finalize()


def aes_cbc_static_iv(data: bytes) -> bytes:
    enc = Cipher(algorithms.AES(HARDCODED_AES_KEY), modes.CBC(STATIC_IV)).encryptor()
    return enc.update(data) + enc.finalize()


def triple_des(data: bytes) -> bytes:
    enc = Cipher(TripleDES(HARDCODED_AES_KEY + HARDCODED_AES_KEY[:8]), modes.ECB()).encryptor()
    return enc.update(data) + enc.finalize()
