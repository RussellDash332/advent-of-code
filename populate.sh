export Y=2024
cd ~/advent-of-code/aoc-$Y
for i in $(seq -f '%02g' 1 25)
do mkdir -p Day-$i && touch Day-$i/$i.in && mkdir -p Day-$i/Python && touch Day-$i/Python/main.py
done