#!/bin/sh

black . --check --diff && isort . --check-only --diff