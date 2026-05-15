#!/bin/bash
# Move existing projects into the 'Monceipts' Master Structure

projects=("MonLayers" "Bullish-Chain" "Crypto-Raid-MEGA-Bot" "Strawman-Track-Down")

for repo in "${projects[@]}"
do
    echo "📦 Integrating $repo..."
    mkdir -p "app/integrated_services/$repo"
    # Logic to move source code while keeping the root clean
    # mv path/to/$repo/* app/integrated_services/$repo/
done

echo "✅ Integration complete. Update the root docker-compose to orchestrate new services."
