from dash import Dash, set_props
from common import get_logger
import feffery_antd_components as fac

logger = get_logger(__name__)

# dash实例
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=True,
    on_error=lambda err: (
        logger.exception(f"[exception]{err}"),
        set_props(
            "global-notification-container",
            {
                "children": fac.AntdNotification(
                    message="内部错误", description=str(err), type="error"
                )
            },
        ),
    ),
)
app.server.secret_key = "5hyBGnKyl4REUL08sFdus"

# flask实例
server = app.server
