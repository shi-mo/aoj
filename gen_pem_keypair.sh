#!/bin/bash

# Enhanced safety: exit on errors, unset variables, and pipeline failures
set -euo pipefail

PRIVATE_KEY_NAME="id_rsa-aoj"
SSH_KEY_DIR="$HOME/.ssh"
PRIVATE_KEY_PATH="$SSH_KEY_DIR/$PRIVATE_KEY_NAME"
PUBLIC_KEY_PATH="$PRIVATE_KEY_PATH.pub.pem"

# Generate the RSA key pair
ssh-keygen -t rsa -m PEM -f "$PRIVATE_KEY_PATH" -N ""

# Convert the public key to PEM format
ssh-keygen -f "$PRIVATE_KEY_PATH.pub" -e -m PEM > "$PUBLIC_KEY_PATH"

echo "Keys generated:"
echo "- Private key: $PRIVATE_KEY_PATH"
echo "- Public key: $PUBLIC_KEY_PATH"
