#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to log informational messages
log() {
    echo "[INFO] $1"
}

# Function to print error message and exit with failure
error_exit() {
    echo "[ERROR] $1" >&2
    exit 1
}

# Check if nginx is already installed using dpkg (Debian-based systems)
if dpkg -s nginx >/dev/null 2>&1; then
    log "Nginx is already installed."
else
    log "Nginx is not installed. Installing..."

    # Update the package list
    sudo apt-get update || error_exit "Failed to update package list."

    # Install nginx, fail with error message if it doesn't succeed
    sudo apt-get install -y nginx || error_exit "Failed to install nginx."

    log "Nginx installation completed successfully."
fi

