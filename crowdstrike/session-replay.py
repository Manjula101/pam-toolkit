def __init__(self, client_id=None, client_secret=None, demo_mode=False):
    """
    Initialize the RTR client.

    Args:
        client_id: Falcon API client ID
        client_secret: Falcon API client secret
        demo_mode: Run in demonstration mode without real API calls
    """
    self.demo_mode = demo_mode

    if demo_mode:
        print("[INFO] Running in DEMO mode - no real API calls will be made\n")
        self.rtr = None
    else:
        client_id = client_id or os.getenv('FALCON_CLIENT_ID')
        client_secret = client_secret or os.getenv('FALCON_CLIENT_SECRET')
        if not client_id or not client_secret:
            raise ValueError(
                "Missing credentials. Set FALCON_CLIENT_ID and "
                "FALCON_CLIENT_SECRET environment variables or pass "
                "them directly."
            )

        self.rtr = RealTimeResponse(
            client_id=client_id,
            client_secret=client_secret
        )

def replay_session(self, session_id):
    """
    Replay a specific RTR session showing all commands and outputs.

    Args:
        session_id: The RTR session ID to replay
    """
    if self.demo_mode:
        self._demo_replay(session_id)
        return

    try:
        print(f"[*] Fetching session details for: {session_id}")
        response = self.rtr.list_sessions(ids=session_id)

        if response['status_code'] != 200:
            print(
                "[ERROR] Failed to fetch session: "
                f"{response['body']['errors']}"
            )
            return

        sessions = response['body']['resources']
        if not sessions:
            print(f"[ERROR] Session {session_id} not found")
            return

        session = sessions[0]
        self._display_session_info(session)

        print("\n[*] Retrieving command history...")
        cmd_response = self.rtr.list_queued_sessions(
            session_id=session_id
        )

        if cmd_response['status_code'] == 200:
            self._display_commands(cmd_response['body']['resources'])
        else:
            print("[WARN] Could not retrieve command history")

    except Exception as e:
        print(f"[ERROR] Session replay failed: {str(e)}")

def _display_session_info(self, session):
    """Display session metadata."""
    print("\n" + "="*60)
    print("RTR SESSION REPLAY")
    print("="*60)
    print(f"Session ID: {session.get('id', 'N/A')}")
    print(f"Device ID: {session.get('device_id', 'N/A')}")
    print(f"User: {session.get('user_id', 'N/A')}")
    print(f"Start Time: {session.get('created_at', 'N/A')}")
    print(f" Status: {session.get('status', 'N/A')}")
    print("="*60)

def _display_commands(self, commands):
    """Display command execution history."""
    print("\nCOMMAND HISTORY:")
    print("-"*60)

    for idx, cmd in enumerate(commands, 1):
        timestamp = cmd.get('created_at', 'N/A')
        command = cmd.get('command', 'N/A')
        status = cmd.get('status', 'N/A')

        print(f"\n[{idx}] {timestamp}")
        print(f" Command: {command}")
        print(f" Status: {status}")

        if 'stdout' in cmd:
            print(f" Output:\n{cmd['stdout']}")
        if 'stderr' in cmd:
            print(f" Error:\n{cmd['stderr']}")

    print("-"*60)

def _demo_replay(self, session_id):
    """Simulate session replay in demo mode."""
    print("="*60)
    print("RTR SESSION REPLAY [DEMO MODE]")
    print("="*60)
    print(f"Session ID: {session_id}")
    print("Device ID: device-abc123-demo")
    print("User: security.analyst@example.com")
    print("Start Time: 2025-11-18T10:00:00Z")
    print("Status: completed")
    print("="*60)

    print("\nCOMMAND HISTORY:")
    print("-"*60)

    demo_commands = [
        {
            'time': '10:00:15',
            'cmd': 'pwd',
            'output': '/home/user'
        },
        {
            'time': '10:00:23',
            'cmd': 'ls -la',
            'output': 'total 48\n...'
        },
        {
            'time': '10:01:05',
            'cmd': 'cat suspicious_file.txt',
            'output': 'Suspicious content...'
        },
        {
            'time': '10:02:30',
            'cmd': 'ps aux | grep malware',
            'output': 'No processes found'
        }
    ]

    for idx, cmd in enumerate(demo_commands, 1):
        print(f"\n[{idx}] 2025-11-18T{cmd['time']}Z")
        print(f" Command: {cmd['cmd']}")
        print(" Status: success")
        print(f" Output:\n {cmd['output']}")

    print("-"*60)
    print("\n[INFO] This is a demonstration. Connect with real API credentials")
    print(" to replay actual RTR sessions from your Falcon environment.")
