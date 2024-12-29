#!/bin/bash

# Enhanced safety: exit on errors, unset variables, and pipeline failures
set -euo pipefail

PUBLIC_KEY_PATH="$HOME/.ssh/id_rsa-aoj.pub.pem"

# Prompt the user for input
read -p "Enter userID: " userID
read -sp "Enter password: " password
echo

# Generate the YAML string
yaml_string="id: $userID
password: \"$password\""

# Generate a random symmetric key
symmetric_key=$(openssl rand -base64 32)

# Encrypt the YAML string using the symmetric key
echo "$yaml_string" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:"$symmetric_key" -out submit.auth.yaml.enc

# Encrypt the symmetric key using the RSA public key
echo "$symmetric_key" | openssl pkeyutl -encrypt -pubin -inkey "$PUBLIC_KEY_PATH" -out symmetric.key.enc

echo "Encryption complete! Files generated:"
echo "- Encrypted YAML: submit.auth.yaml.enc"
echo "- Encrypted Symmetric Key: symmetric.key.enc"
