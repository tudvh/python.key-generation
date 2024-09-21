import secrets
import os

# Constants for directory and file name
DIR = "src/jwt-secret/generated-keys"
FILE_NAME = "secret_key.txt"


def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)


def generate_jwt_secret():
    """Generate a JWT secret."""
    return secrets.token_hex(32)


def save_secret_to_file(directory, file_name, secret):
    """Save the JWT secret to a file."""
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as f:
        f.write(secret + '\n')
    print(f"JWT Secret Key saved to: {file_path}")


def main():
    ensure_directory_exists(DIR)
    jwt_secret = generate_jwt_secret()
    save_secret_to_file(DIR, FILE_NAME, jwt_secret)
    print(f"JWT Secret Key: {jwt_secret}")


if __name__ == "__main__":
    main()
