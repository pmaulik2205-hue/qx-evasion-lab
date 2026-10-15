"""R4-N4 Verifies with the public key taken from a certificate in ANOTHER repo (qx-pki-ssh/certs/chain.pem).
The algorithm (RSA-2048 leaf) is only known from the certificate."""
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

CERT_PATH = "/opt/qx/qx-pki-ssh/certs/chain.pem"


def verify_partner(data: bytes, signature: bytes) -> None:
    with open(CERT_PATH, "rb") as fh:
        leaf = x509.load_pem_x509_certificates(fh.read())[0]
    leaf.public_key().verify(signature, data, padding.PKCS1v15(), hashes.SHA256())
