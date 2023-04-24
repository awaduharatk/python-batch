from typing import final
import logging
from _common.properties import Properties
from abc import ABCMeta, abstractmethod


class BatchProcessor(metaclass=ABCMeta):
    """
    ベースクラス
    各処理はこのクラスを継承して実装する
    """

    def __init__(self, **kwargs: str) -> None:
        """
        初期化
        共通部品などの初期化もここで行う

        Args:
            prop_file_path (str): _description_
        """
        if kwargs.get("prop_file_path") != "":
            self.prop = Properties(kwargs.get("prop_file_path"))

    @final
    def process_execution(self) -> None:
        """
        オーバライド禁止
        共通処理を実装する
        """
        logging.info("Process Start")

        try:
            self.process()
        except Exception as e:
            # 想定外のエラーをキャッチして解析情報を出力する
            logging.error("Error: %s", e)

        logging.info("Process End")

    @abstractmethod
    def process(self) -> None:
        """
        ここをオーバーライドして各処理の実装をする
        """
        pass
