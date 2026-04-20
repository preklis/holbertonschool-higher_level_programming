#!/bin/bash
# Displays the body of a 200 status code response from a URL
curl -s "$1" | cat
