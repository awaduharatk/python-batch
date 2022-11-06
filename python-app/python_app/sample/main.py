import sys
import sample.app as app


def main() -> None:
    """メイン処理

    ここではapp.pyを呼び出すのみ
    """
    app.main(sys.argv)
    print("sample.main.py main()")


if __name__ == "__main__":
    main()
    print("sample.main.py __main__")
