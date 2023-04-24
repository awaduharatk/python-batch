import sys
from sample.app import SampleApp
from _common.batch.batch_processor import BatchProcessor


def main(*args: str) -> None:
    """メイン処理

    ここではapp.pyを呼び出すのみ
    """
    print("sample.main.py main()")

    # 複数ある場合はカンマ区切りのKey:Valueで指定可能
    kwargs = {"prop_file_path": ""}
    processor = SampleApp(*args, **kwargs)
    processor.process_execution()


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*args)
