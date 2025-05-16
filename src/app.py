from server import app
import feffery_utils_components as fuc
import feffery_antd_components as fac
from views import navigator
from dash.dependencies import Input, Output, State
from dash import html

# 全局url监听组件，仅仅起到监听的作用
app.layout = [
    fuc.FefferyLocation(id="global-url-location"),
    # 注入全局消息提示容器
    fac.Fragment(id="global-message-container"),
    # 注入全局通知信息容器
    fac.Fragment(id="global-notification-container"),
    # 注入js执行
    fuc.FefferyExecuteJs(id="global-execute-js-output"),
    # 应用根容器
    html.Div(id="root-container"),
]


@app.callback(
    Output("root-container", "children"),
    Input("global-url-location", "pathname"),
    prevent_initial_call=True,
)
def main_router(pathname):
    if pathname == "/":
        return navigator.render_content()
