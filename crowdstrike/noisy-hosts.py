#!/usr/bin/env python3
"""
Top 10 Noisy Hosts – CrowdStrike Falcon
Enterprise Security Lab | Manjula Wickramasuriya
Endpoint Behavior Analytics
"""


def top_noisy_hosts(days=7, limit=10):
    """Print demo noisy hosts."""
    print(f"[DEMO] Top {limit} Noisy Hosts (last {days} days):")
    print("HOST123456.example.com")
    print("2025-11-30T08:00:00Z 1247 logins")
    print("HOST789012.example.com")
    print("2025-11-30T07:30:00Z 987 logins")
    print("... (requires Falcon API key for real data)")


if __name__ == "__main__":
    top_noisy_hosts()
