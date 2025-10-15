#!/usr/bin/env python3
import subprocess
import sys
import pathlib
import shutil

def run_command(cmd, cwd):
    print(f"\n[+] Running: {' '.join(cmd)} in {cwd}")
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def main():
    # Check if fakeroot is installed
    if not shutil.which("fakeroot"):
        print("[!] Error: 'fakeroot' is not installed or not in PATH")
        response = input("[?] Would you like to install it now? (y/n): ").strip().lower()
        
        if response in ['y', 'yes']:
            print("[+] Installing fakeroot...")
            try:
                subprocess.run(["sudo", "apt-get", "install", "-y", "fakeroot"], check=True)
                print("[+] fakeroot installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"[!] Failed to install fakeroot with exit code {e.returncode}")
                print("[!] Please install it manually: sudo apt-get install fakeroot")
                sys.exit(1)
            except FileNotFoundError:
                print("[!] 'apt-get' not found. Please install fakeroot manually for your distribution.")
                sys.exit(1)
        else:
            print("[!] Cannot proceed without fakeroot. Exiting.")
            sys.exit(1)
    
    package_dir = pathlib.Path(__file__).resolve().parent

    output_file = package_dir / (package_dir.name + ".deb")

    print(f"[+] Building package: {output_file.name}")

    run_command(
        ["fakeroot", "dpkg-deb", "--build", str(package_dir), str(output_file)],
        cwd=package_dir.parent
    )

    print(f"\nDone. Package created at: {output_file}")

if __name__ == "__main__":
    main()
