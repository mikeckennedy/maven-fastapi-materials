import json

from models.packages import PackageModel


def load_data() -> dict:
    with open('./pydantic.json', 'r', encoding='utf-8') as fin:
        return json.load(fin)


def main():
    jdata = load_data()
    model = PackageModel(**jdata)
    print(json.dumps(model.dict(), indent=4))


if __name__ == '__main__':
    main()
