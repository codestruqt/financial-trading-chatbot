import json
from datetime import datetime, timedelta
import random

# Define sample dialogue components
user_queries = [
    "What's the current sentiment on tech stocks today?",
    "Should I consider buying TSLA at these levels?",
    "What are today's trading volume leaders?",
    "Can you provide a technical analysis for SPY?",
    "What's the outlook on crude oil futures given the current global supply?"
]

bot_responses = [
    "Tech stocks are showing strong bullish signals this morning, primarily driven by positive earnings reports from major players like AAPL and MSFT.",
    "TSLA is currently trading at a high valuation. It might be better to wait for a consolidation phase before making a move.",
    "Today, AAPL, NVDA, and AMD are among the top in trading volume, indicating heightened market activity and potential volatility.",
    "SPY is nearing its overbought threshold based on the RSI and moving average indicators, which might suggest a short-term correction.",
    "Crude oil futures are under pressure due to rising inventories and slowing global demand. It might be wise to adopt a cautious approach in energy trades."
]

# Generate logs with timestamps
def generate_logs(num_logs=5):
    logs = []
    start_time = datetime.now() - timedelta(hours=1)
    for i in range(num_logs):
        timestamp_user = (start_time + timedelta(minutes=i*5)).strftime("%Y-%m-%d %H:%M:%S")
        timestamp_bot = (start_time + timedelta(minutes=i*5, seconds=5)).strftime("%Y-%m-%d %H:%M:%S")
        log = {
            "conversation": [
                {"timestamp": timestamp_user, "speaker": "User", "message": user_queries[i % len(user_queries)]},
                {"timestamp": timestamp_bot, "speaker": "Bot", "message": bot_responses[i % len(bot_responses)]}
            ]
        }
        logs.append(log)
    return logs

# Generate and save the logs
logs = generate_logs(num_logs=5)
with open("trading_chatbot_logs.json", "w") as f:
    json.dump(logs, f, indent=4)

print("Generated logs have been saved to trading_chatbot_logs.json")
