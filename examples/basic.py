"""Minimal example for TokenSwapCalc."""

from tokenswapcalc import tokenswapcalc


def main():
 runner = tokenswapcalc({"name": "TokenSwapCalc", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()