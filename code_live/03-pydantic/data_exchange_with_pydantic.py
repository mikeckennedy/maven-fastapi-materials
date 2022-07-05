import json
from pathlib import Path

from package_models import PackageModel


def main():
    file = Path(__file__).parent / 'pydantic.json'
    with open(file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    package = PackageModel(**data)
    print(package)
    print()
    print(json.dumps(package.dict(), indent=4))

if __name__ == '__main__':
    main()
