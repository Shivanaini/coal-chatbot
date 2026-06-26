#!/bin/bash
set -e

aws cloudformation validate-template \
  --template-body file://infra/cloudformation/network.yaml

echo "Template validation successful"