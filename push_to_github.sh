#!/bin/bash
# Script to push HVR 6 docs to GitHub
# Usage: ./push_to_github.sh <GITHUB_TOKEN>

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <GITHUB_TOKEN>"
    echo "Get a token at: https://github.com/settings/tokens (needs 'repo' scope)"
    exit 1
fi

TOKEN="$1"
REPO="Badn3o/hvr6-docs"

echo "=== Creating repo $REPO ==="
curl -s -X POST \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/user/repos \
    -d '{"name":"hvr6-docs","description":"HVR 6 Complete Documentation - Fivetran HVR (High-Volume Replicator) v6.2 reference, manuals, technical docs","private":false,"has_issues":true,"has_wiki":false}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('html_url','') or d.get('message',''))"

echo ""
echo "=== Pushing to GitHub ==="
cd /root/hvr-docs
git remote set-url origin https://${TOKEN}@github.com/${REPO}.git
git push -u origin master

echo ""
echo "=== Done! ==="
echo "Repo available at: https://github.com/${REPO}"
