# rolling_project
This is phase one of my DevOps rolling project.

# Infra Automation Simulator

This phase in the project simulates virtual machine (VM) provisioning using Python and Bash.  
Users can define VM details, validate input, generate configuration files, and simulate service setup.

## Features

- Input validation using `pydantic`
- Configuration saved to `infra_automation/configs/instances.json`
- Simulated service setup via Bash script
- Logs saved to `infra_automation/logs/provisioning.log`

## How to Run

```bash
python infra_simulator.py

