import datetime
import os


def main(args: list) -> None:
    # def main() -> None:
    print("sample.app.py main()")
    print("env stage:", get_env("stage"))
    print(get_nowDate())
    print(args)


def get_env(key: str) -> str:
    """指定されたKeyの環境変数を取得する

    Args:
        key (str): キー名

    Returns:
        str: バリュー値
    """
    return os.getenv(key, default="")


def get_nowDate() -> datetime.datetime:
    """現在日時を取得する

    Returns:
        datetime.datetime: 現在日時
    """
    return datetime.datetime.now()
