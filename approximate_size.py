SUFFIXES = {
    1000: ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
    1024: ["KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"],
}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    """ Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string
    """
    if size < 0:
        raise ValueError("number must be non-negative")

    # declare variable + if/else
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        # value that returned by the sentence below is Boolean
        if size < multiple:
            return f"{round(size,1)} {suffix}"

    raise ValueError("number too large")


if __name__ == "__main__":
    print(approximate_size(1000000000000))
    print(approximate_size(1000000000000, False))
