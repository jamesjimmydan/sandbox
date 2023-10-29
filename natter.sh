phrases=("Hi Ainslie" "You are doing such a good job" "Keep up the good work" "Press those buttons baby")

for p in "${phrases[@]}"; do
    sleep 300
    say $p
done
