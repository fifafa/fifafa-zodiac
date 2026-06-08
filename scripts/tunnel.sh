#!/bin/bash
# lalalin Cloudflare Tunnel wrapper
# Creates a quick tunnel to localhost:8790 and saves the public URL
# Falls back gracefully if tunnel dies

URL_FILE="/var/www/lalalin-tunnel-url.txt"
LOG_FILE="/var/log/lalalin-tunnel.log"
TUNNEL_PID_FILE="/var/run/lalalin-tunnel.pid"

cleanup() {
    echo "$(date): Tunnel shutting down" >> "$LOG_FILE"
    rm -f "$TUNNEL_PID_FILE"
    exit 0
}
trap cleanup SIGTERM SIGINT

echo "$$" > "$TUNNEL_PID_FILE"

while true; do
    echo "$(date): Starting Cloudflare Tunnel to localhost:8790..." >> "$LOG_FILE"
    
    cloudflared tunnel --url http://localhost:8790 --no-autoupdate 2>&1 | while IFS= read -r line; do
        echo "$line" >> "$LOG_FILE"
        
        # Extract the trycloudflare URL
        if echo "$line" | grep -q 'trycloudflare.com'; then
            TUNNEL_URL=$(echo "$line" | grep -oP 'https://[a-zA-Z0-9.-]+\.trycloudflare\.com')
            if [ -n "$TUNNEL_URL" ]; then
                echo "$TUNNEL_URL" > "$URL_FILE"
                echo "$(date): Tunnel URL: $TUNNEL_URL" >> "$LOG_FILE"
                echo "TUNNEL_READY:$TUNNEL_URL"
            fi
        fi
    done
    
    echo "$(date): Tunnel died, restarting in 10s..." >> "$LOG_FILE"
    sleep 10
done
