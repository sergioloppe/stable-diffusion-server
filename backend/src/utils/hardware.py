import platform
import subprocess


def detected_apple_silicon():
    try:
        if platform.processor() == "arm":
            return True
        # Check for Rosetta 2 translation on Intel Macs
        if platform.processor() == "i386":
            result = subprocess.run(["sysctl", "-n", "sysctl.proc_translated"], capture_output=True, text=True)
            return result.stdout.strip() == "1"
    except Exception as e:
        print(f"Error checking platform: {str(e)}")

    return False
