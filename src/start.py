from app import app
import webview


if __name__ == "__main__":
    webview.create_window(
        "OpenEcuX",
        app.server,
        confirm_close=True,
        width=600,
        height=200,
        focus=True,
        resizable=False,
        shadow=True,
    )
    webview.start()
