import datetime
from _common.batch.batch_processor import BatchProcessor


class SampleApp(BatchProcessor):
    """_summary_

    Args:
        BatchProcessor (_type_): _description_
    """

    def __init__(self, *args: str, **kwargs) -> None:
        """
        コンストラクタ
        """
        super().__init__(**kwargs)
        self.args = args

    def process(self) -> None:
        """
        sample処理
        """
        print("sample.app.py main()")
        print(f"args: {self.args}")
        print(self.get_nowDate())

    def get_nowDate(self) -> datetime.datetime:
        """
        現在日時を取得する

        Returns:
            datetime.datetime: 現在日時
        """
        return datetime.datetime.now()
