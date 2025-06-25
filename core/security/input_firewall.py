def is_safe_command(cmd: str) -> bool:
    blacklist = ["rm -rf", "shutdown", "format", "exec("]
    return all(danger not in cmd for danger in blacklist)
