#!/bin/bash
# Generates an ASCII stegosaurus to tell you a fortune, quote, or other saying every 10 minutes.
# Dependencies: cowsay & fortune

x=0
while True do
        printf "\033c";  # Clear screen
        fortune | cowsay -f stegosaurus
        sleep 600;
done
