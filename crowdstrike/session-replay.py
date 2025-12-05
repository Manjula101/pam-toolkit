#!/usr/bin/env python3
"""
CrowdStrike Falcon RTR Session Replay
Enterprise Security Lab | Manjula Wickramasuriya
Endpoint Behavior Analytics
"""
import os
import sys

# Check demo mode first (no imports if demo)
demo_mode = "--demo" in sys.argv or not os.getenv('FALCON_CLIENT_ID')
if demo_mode:
    from falconpy import RealTimeResponse  # Import only if needed (never in CI)
    class FalconRTRReplay:
        def __init__(self, client_id=None, client_secret=None, demo_mode=False):
            self.demo_mode = demo_mode
            if demo_mode:
                print("[INFO] Running in DEMO mode - no real API calls\n")
                self.rtr = None
            else:
                client_id = client_id or os.getenv('FALCON_CLIENT_ID')
                client_secret = client_secret or os.getenv('FALCON_CLIENT_SECRET')
                if not client_id or not client_secret:
                    raise ValueError("Set FALCON_CLIENT_ID/SECRET or use --demo")
                self.rtr = RealTimeResponse(client_id=client_id, client_secret=client_secret)

        def replay_session(self, session_id):
            if self.demo_mode:
                self._demo_replay(session_id)
                return
            # Real mode (skipped in CI)
            print("[INFO] Real mode – would replay session", session_id)

        def _demo_replay(self, session_id):
            print("="*60)
            print("RTR SESSION REPLAY [DEMO MODE]")
            print("="*60)
            print(f"Session ID: {session_id}")
            print("Device ID: device-abc123-demo")
            print("User: security.analyst@example.com")
            print("Start Time: 2025-12-01T10:00:00Z")
            print("Status: completed")
            print("\nCOMMAND HISTORY:")
            print("-"*60)
            demo_commands = [
                {"time": "10:00:15", "cmd": "pwd", "output": "/home/user"},
                {"time": "10:00:23", "cmd": "ls -la", "output": "total 48\n..."},
                {"time": "10:01:05", "cmd": "cat suspicious_file.txt", "output": "Suspicious content..."}
            ]
            for idx, cmd in enumerate(demo_commands, 1):
                print(f"\n[{idx}] 2025-12-01T{cmd['time']}Z")
                print(f" Command: {cmd['cmd']}")
                print(f" Status: success")
                print(f" Output:\n {cmd['output']}")
            print("-"*60)

    def main():
        demo_mode = "--demo" in sys.argv or not os.getenv('FALCON_CLIENT_ID')
        replay = FalconRTRReplay(demo_mode=demo_mode)
        session_id = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "--demo" else "demo-session-123"
        replay.replay_session(session_id)

    if __name__ == "__main__":
        main()
else:
    print("Real mode – set credentials to run")
