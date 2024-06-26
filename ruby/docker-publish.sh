#!/bin/bash
set -e

GIT_COMMIT="$(git rev-parse --short=10 HEAD)"

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 515978473749.dkr.ecr.us-east-1.amazonaws.com
docker build --platform linux/amd64 --tag 515978473749.dkr.ecr.us-east-1.amazonaws.com/procfy:latest --tag 515978473749.dkr.ecr.us-east-1.amazonaws.com/procfy:$GIT_COMMIT -f Dockerfile.production .
docker push 515978473749.dkr.ecr.us-east-1.amazonaws.com/procfy:latest
docker push 515978473749.dkr.ecr.us-east-1.amazonaws.com/procfy:$GIT_COMMIT