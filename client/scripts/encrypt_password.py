import hashlib
import sys

if __name__ == "__main__":
    password = sys.argv[1]
    print hashlib.sha256(password).hexdigest()
