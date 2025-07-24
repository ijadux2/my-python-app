# Diskusage CLI Tool

A simple, user-friendly Python command-line tool to check disk space usage on Linux systems. Designed for daily use, scriptability, and quick insights—tailored for Linux users and system administrators.

## Features

- Show total, used, and free space for any path on your system
- Clean, readable output for humans
- Works out of the box on all modern Linux distributions
- Easily scriptable in shell workflows
- Ready for reproducible packaging with [Nix](https://nixos.org/)

## Usage

```sh
# Check root disk usage
./diskusage.py

# Check a specific directory (e.g., /home)
./diskusage.py /home
```

Or after installation:

```sh
diskusage       # Global command after moving to /usr/local/bin or using pip/nix
```

## Installation

### 1. Clone or Download

```sh
git clone https://github.com/YOURUSERNAME/diskusage
cd diskusage
```

### 2. Run Directly

```sh
chmod +x diskusage.py
./diskusage.py
```

### 3. System-wide (Personal Use)

```sh
sudo mv diskusage.py /usr/local/bin/diskusage
# Then use `diskusage`
```

### 4. With Nix (Reproducible Build)

If you have [Nix](https://nixos.org/) installed:

```sh
nix-build
./result/bin/diskusage
```

## Nix Integration

Includes a `default.nix` for reproducible, dependency-managed builds.

- Run `nix-shell` for a fully prepared dev shell
- Run `nix-build` to create a binary

## Contributing

Pull requests are welcome! Please open issues if you have ideas or spot bugs.

## License

MIT License

## Author

Vaibhav (madara)

