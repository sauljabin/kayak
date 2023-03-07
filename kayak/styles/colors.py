from textual.design import ColorSystem

PRIMARY = "#ff5f00"
SECONDARY = "#0087ff"
DESIGN = {
    "dark": ColorSystem(
        primary=PRIMARY,
        secondary=SECONDARY,
        dark=True,
    ),
    "light": ColorSystem(
        primary=PRIMARY,
        secondary=SECONDARY,
        dark=False,
    ),
}
