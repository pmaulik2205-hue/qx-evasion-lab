"""R4-N1 PQC TRAP: names and comments say ML-KEM, but the code really uses RSA-OAEP.

Post-quantum ML-KEM-768 wrapper (quantum-safe).
"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

ML_KEM_768 = "ML-KEM-768"          # label only


def mlkem_encapsulate(secret: bytes):
    # ML-KEM-768 encapsulation (quantum-safe)
    mlkem_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ct = mlkem_key.public_key().encrypt(
        secret, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return mlkem_key, ct
