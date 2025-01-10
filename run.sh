#!/bin/bash

clean(){
    pkill -f main.py
    pkill -f display.py
    echo "Goodbye!"
}

echo "Welcome to PiTunes!"

python3 main.py &
python3 display.py &

while true; do
    if [ -f /tmp/exit_signal ]; then
        echo "Cleaning..."
        clean
        rm /tmp/exit_signal
        break
    fi
    sleep 1
done

wait
