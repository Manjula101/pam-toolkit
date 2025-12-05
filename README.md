# PAM Toolkit – Open-Source Privileged Access Automation
[![Stargazers](https://img.shields.io/github/stars/Manjula101/pam-toolkit?style=social)](https://github.com/Manjula101/pam-toolkit/stargazers)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Manjula101.pam-toolkit)](https://github.com/Manjula101/pam-toolkit)
[![CI](https://github.com/Manjula101/pam-toolkit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Manjula101/pam-toolkit/actions/workflows/ci.yml)
> **Zero-standing-privilege automation suite** – 5 enterprise-grade tools merged into official repos

![PAM Toolkit Overview](https://raw.githubusercontent.com/Manjula101/pam-toolkit/main/assets/demo-overview.gif)

### Live Contributions (Merged into Official Repos)

| Vendor        | Feature                              | PR / Status |
|---------------|--------------------------------------|-------------|
| CrowdStrike   | Noisy hosts detection                | [#1391](https://github.com/CrowdStrike/falconpy/pull/1391) |
| CrowdStrike   | RTR Session Replay (demo mode)       | [#1394](https://github.com/CrowdStrike/falconpy/pull/1394) |
| FortiOS       | Auto-block malicious IPs             | [#406](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/pull/406) |
| Teleport      | Full JIT + approval workflow         | [#61727](https://github.com/gravitational/teleport/pull/61727) |
| OPA           | Root-deny policy with JIT approval   | [#8073](https://github.com/open-policy-agent/opa/pull/8073) |

### Quick Start

```bash
git clone https://github.com/Manjula101/pam-toolkit.git
cd pam-toolkit
# Pick any tool and run – all are demo-safe
python crowdstrike/session-replay.py --demo
