import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Constants for directory paths
MULTI_LINE_DIR = "src/asymmetric-key-pair/generated-keys/multi-line-keys"
ONE_LINE_DIR = "src/asymmetric-key-pair/generated-keys/one-line-keys"


def generate_private_key():
    """Generate an RSA private key."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )


def save_key_to_file(file_path, key_data):
    """Save key data to a file."""
    with open(file_path, "wb") as f:
        f.write(key_data)


def convert_to_one_line(pem_data):
    """Convert PEM data to a single line format."""
    return pem_data.rstrip(b'\n').replace(b'\n', b'\\n') + b'\n'


def main():
    # Create directories if they don't exist
    os.makedirs(MULTI_LINE_DIR, exist_ok=True)
    os.makedirs(ONE_LINE_DIR, exist_ok=True)

    # Generate private key
    private_key = generate_private_key()

    # Export private key in PEM format
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Save private key in multi-line format
    save_key_to_file(os.path.join(
        MULTI_LINE_DIR, "private_key.pem"), pem_private_key)

    # Save private key in one-line format
    pem_private_key_one_line = convert_to_one_line(pem_private_key)
    save_key_to_file(os.path.join(
        ONE_LINE_DIR, "private_key.pem"), pem_private_key_one_line)

    # Export public key in PEM format
    pem_public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save public key in multi-line format
    save_key_to_file(os.path.join(
        MULTI_LINE_DIR, "public_key.pem"), pem_public_key)

    # Save public key in one-line format
    pem_public_key_one_line = convert_to_one_line(pem_public_key)
    save_key_to_file(os.path.join(
        ONE_LINE_DIR, "public_key.pem"), pem_public_key_one_line)


if __name__ == "__main__":
    main()
