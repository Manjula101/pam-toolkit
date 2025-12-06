#!/usr/bin/env python3
"""
CrowdStrike Falcon RTR Session Replay – Demo Safe
Enterprise Security Lab | Manjula Wickramasuriya
"""


import os
import sys


class FalconRTRReplay:
    """Demo-safe RTR session replay."""

    def __init__(self, demo_mode=True):
        self.demo_mode = demo_mode
        if demo_mode:
            print("[INFO] Running in DEMO mode - no real API calls\n")

    def replay_session(self, session_id="demo-123"):
        """Replay session in demo mode."""
        if not self.demo_mode:
            print("Real mode not supported in demo")
            return

        print("=" * 60)
        print("RTR SESSION REPLAY [DEMO MODE]")
        print("=" * 60)
        print(f"Session ID: {session_id}")
        print("Device ID: device-abc123-demo")
        print("User: security.analyst@example.com")
        print("Start Time: 2025-12-01T10:00:00Z")
        print("Status: completed")
        print("\nCOMMAND HISTORY:")
        print("-" * 60)

 demo_commands = [
    {"time": "10:00:15", "cmd": "pwd", "output": "/home/user"},
    {"time": "10:00:23", "cmd": "ls -la", "output": "total 48"},
    {"time": "10:01:05", "cmd": "cat file.txt", "output": "Sensitive data"}
]

        for idx, cmd in enumerate(demo_commands, 1):
            time_stamp = f"2025-12-01T{cmd['time']}Z"
            print(f"\n[{idx}] {time_stamp}")
            print(f" Command: {cmd['cmd']}")
            print(" Status: success")
            print(f" Output:\n {cmd['output']}")

        print("-" * 60)


if __name__ == "__main__":
    demo = "--demo" in sys.argv or not os.getenv("FALCON_CLIENT_ID")
    replay = FalconRTRReplay(demo_mode=demo)
    if len(sys.argv) > 1 and sys.argv[1] != "--demo":
        session = sys.argv[1]
    else:
        session = "demo-123"
    replay.replay_session(session)
