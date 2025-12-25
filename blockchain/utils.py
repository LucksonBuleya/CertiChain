import hashlib

def has_certificate(data: dict) -> str:
    # Creates a unique fingerprint for certificate data
    certificate_string = "".join(str(value) for value in data.values())
    return
hashlib.sha256(certificate_string.encode()).hexdigest()

#data order must never change