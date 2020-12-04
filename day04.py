from pathlib import Path
from dataclasses import dataclass
from typing import Any
import re

hcl_pattern = re.compile(r"^#[0-9a-f]{6}$")
pid_pattern = re.compile(r"^\d{9}$")


@dataclass
class Passport:
    byr: int  # (Birt Year)
    iyr: int  # (Issue Year)
    eyr: int  # (Expiration Year)
    hgt: str  # (Height)
    hcl: str  # (Hair Color)
    ecl: str  # (Eye Color)
    pid: str  # (Passport ID)
    cid: Any = 0  # (Country ID)

    def __post_init__(self):
        self.byr = int(self.byr)
        self.iyr = int(self.iyr)
        self.eyr = int(self.eyr)

    def validate_fields(self):
        is_byr = 1920 <= self.byr <= 2002
        is_iyr = 2010 <= self.iyr <= 2020
        is_eyr = 2020 <= self.eyr <= 2030
        if "in" in self.hgt:
            c_hgt = int(self.hgt.split("in")[0])
            is_hgt = 59 <= c_hgt <= 76
        elif "cm" in self.hgt:
            c_hgt = int(self.hgt.split("cm")[0])
            is_hgt = 150 <= c_hgt <= 193
        else:
            is_hgt = False
        is_hcl = bool(hcl_pattern.match(self.hcl))
        is_ecl = self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        is_pid = bool(pid_pattern.match(self.pid))
        if not all([is_byr, is_iyr, is_eyr, is_hgt, is_hcl, is_ecl, is_pid]):
            raise ValueError


def check_passports(strict_rules=False):
    with open(Path(__file__).parent / "data" / "day04.txt", "r") as f:
        valid_passports = []
        invalid_passports = 0

        fields = {}
        for line in f.read().splitlines():
            if not line:
                try:
                    p = Passport(**fields)
                    if strict_rules:
                        p.validate_fields()
                    valid_passports.append(p)
                    fields = {}
                    continue
                except TypeError:
                    invalid_passports += 1
                    fields = {}
                    continue
                except ValueError:
                    invalid_passports += 1
                    fields = {}
                    continue
            key_values = line.split(" ")
            fields.update(dict(kv.split(":") for kv in key_values))
    try:
        p = Passport(**fields)
        if strict_rules:
            p.validate_fields()
        valid_passports.append(p)
    except TypeError:
        invalid_passports += 1
    except ValueError:
        invalid_passports += 1
    return (len(valid_passports), invalid_passports)


print("First part")
valid_passports, invalid_passports = check_passports()
print(f"Number of valid passports: {valid_passports}.")
print(f"Number of invalid passports: {invalid_passports}.")
print("======")
print("Second part")
valid_passports, invalid_passports = check_passports(strict_rules=True)
print(f"Number of valid passports: {valid_passports}.")
print(f"Number of invalid passports: {invalid_passports}.")
