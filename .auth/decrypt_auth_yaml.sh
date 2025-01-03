#!/bin/bash

# Enhanced safety: exit on errors, unset variables, and pipeline failures
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ENCRYPTED_YAML_FILE="$SCRIPT_DIR/submit.auth.yaml.enc"
ENCRYPTED_SYMMETRIC_KEY_FILE="$SCRIPT_DIR/symmetric.key.enc"

PRIVATE_KEY_PATH="$HOME/.ssh/id_rsa-aoj"

# Decrypt the symmetric key using the private RSA key
symmetric_key=$(openssl pkeyutl -decrypt -inkey "$PRIVATE_KEY_PATH" -in "$ENCRYPTED_SYMMETRIC_KEY_FILE")

# Decrypt the YAML file using the symmetric key
openssl enc -d -aes-256-cbc -salt -pbkdf2 -pass pass:"$symmetric_key" -in "$ENCRYPTED_YAML_FILE"
