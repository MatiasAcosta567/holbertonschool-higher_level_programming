#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -H "Content-Type: application/json" -X POST --data "$(cat "$2")" "$1"
