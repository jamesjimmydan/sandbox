phrases=("apple" "banana" "cherry" "date")

for p in "${phrases[@]}"; do
    sleep 5
    say $p
done
