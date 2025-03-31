#!/bin/bash

# Function to log informational messages
log() {
  echo "[INFO] $1"
}

# Function to print error message and exit
error_exit() {
  echo "[ERROR] $1" >&2
  exit 1
}

# The path to find the vm's jsons in the structure.
CONFIG_FILE="../configs/instances.json"

[ ! -f "$CONFIG_FILE" ] && error_exit "Configuration file not found at $CONFIG_FILE"

# Using grep to find the names of the vms for the logging printing.
VM_LIST=$(grep -o '"name": *"[^"]*"' "$CONFIG_FILE" | cut -d '"' -f4)

[ -z "$VM_LIST" ] && error_exit "No VM instances found in $CONFIG_FILE"

log "Starting Nginx installation simulation on all VMs..."

# For every vm the user added we will install 'nginx'
for vm in $VM_LIST; do
  log "Starting simulation on $vm..."

  echo "Simulating: Updating package list on $vm..."
  sleep 1
  echo "Simulating: Installing Nginx on $vm..."
  sleep 1
  log "Nginx installation simulation completed successfully on $vm."

  echo "-------------------------------------------"
done

log "Provisioning process finished for all VMs."

