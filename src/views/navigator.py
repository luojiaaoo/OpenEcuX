import feffery_antd_components as fac


def render_content():
    return fac.AntdSpace(
        [
            fac.AntdTabs(
                items=[
                    {
                        "key": f"硬件",
                        "label": f"硬件",
                        "children": fac.AntdCard(),
                    },
                ],
                size="small",
            ),
        ],
        direction="vertical",
        style={"width": "100%"},
    )
