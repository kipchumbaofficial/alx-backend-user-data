#!/usr/bin/env python3
""" filter_datum:
        Returns: Log message obfuscated
"""
import re


def filter_datum(fields: str, redaction: str,
                 message: str, separator: str):
    pattern = r'(' + '|'.join(map(re.escape, fields)) + r')=[^' + re.escape(separator) + r']+'
    return re.sub(pattern, lambda m: m.group(0).split('=')[0] + '=' + redaction, message)
