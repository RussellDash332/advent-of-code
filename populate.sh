export Y=2025
cd /workspaces/advent-of-code/aoc-$Y
for i in $(seq -f '%02g' 1 12)
do mkdir -p Day-$i && touch Day-$i/$i.in && mkdir -p Day-$i/Python && touch Day-$i/Python/main.py
done