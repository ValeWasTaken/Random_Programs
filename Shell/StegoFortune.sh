#!/bin/bash
# Generates an ASCII stegosaurus to tell you a fortune, quote, or other saying every 10 minutes for 12 hours.
# Dependencies: Cowsay & fortune

x=0
while [ x>21540 ]; do
        printf "\033c"; # Clear screen
        fortune | cowsay -f stegosaurus
        sleep 600;
        let x+=600;
done
