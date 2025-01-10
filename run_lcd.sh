#!/bin/bash

clean(){
	echo -e "\nCleaning...\n"
	python3 clear.py
	sleep 0.5
	pkill -f main.py
	pkill -f lcd.py
	pkill -f clear.py
	echo "Goodbye!"
}

echo "Welcome to PiTunes!"

trap clean EXIT

python3 main.py &
python3 lcd.py &

wait

