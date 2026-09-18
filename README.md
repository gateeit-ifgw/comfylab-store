# ComfyLAB Store

Official repository for modular instruments, blocks, clusters, and blueprints for [ComfyLAB](https://github.com/gateeit-ifgw/ComfyLAB).

## Official Store Signing Key
All official packages in this repository are cryptographically signed using Ed25519.
- **Official Public Key:** `3a61083b4c2ebce87fa7c250b3e64712a457315920952ce920dd8bd88509a022`

## Directory Structure
- `instruments/`: Vendor-specific instrument drivers and UI blocks.
- `blocks/`: General domain-specific processing blocks.
- `clusters/`: Reusable compound cluster graphs.
- `blueprints/`: Complete automated test-and-measurement blueprints.

## Contributing a New Instrument
1. Create a directory: `instruments/<vendor>/<model>/`
2. Add `manifest.json`, `driver.py`, and `blocks.py`.
3. Open a Pull Request!
