# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from __future__ import annotations

import re
import sys
from collections.abc import Mapping, Sequence
from datetime import date, datetime
from typing import Annotated, Any, Generic, Literal, TypeVar, Union, get_args

if sys.version_info >= (3, 14):  # https://peps.python.org/pep-0728/
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing_extensions import TypeIs

if sys.version_info >= (3, 12):
    from typing import TypeAliasType
else:
    from typing_extensions import TypeAliasType

if sys.version_info >= (3, 11):
    from typing import LiteralString
else:
    from typing_extensions import LiteralString

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


__all__ = [
    "AggregateOp_T",
    "Align_T",
    "AllSortString_T",
    "AutosizeType_T",
    "AxisOrient_T",
    "BinnedTimeUnit_T",
    "Blend_T",
    "BoxPlot_T",
    "ColorHex",
    "ColorName_T",
    "ColorScheme_T",
    "CompositeMark_T",
    "Cursor_T",
    "ErrorBand_T",
    "ErrorBarExtent_T",
    "ErrorBar_T",
    "FontWeight_T",
    "ImputeMethod_T",
    "Interpolate_T",
    "LayoutAlign_T",
    "LegendOrient_T",
    "Map",
    "MarkInvalidDataMode_T",
    "MarkType_T",
    "Mark_T",
    "MultiTimeUnit_T",
    "NonArgAggregateOp_T",
    "OneOrSeq",
    "Orient_T",
    "Orientation_T",
    "PaddingKwds",
    "PrimitiveValue_T",
    "ProjectionType_T",
    "RangeEnum_T",
    "ResolveMode_T",
    "RowColKwds",
    "ScaleInterpolateEnum_T",
    "ScaleType_T",
    "SelectionResolution_T",
    "SelectionType_T",
    "SingleDefUnitChannel_T",
    "SingleTimeUnit_T",
    "SortByChannel_T",
    "SortOrder_T",
    "StackOffset_T",
    "StandardType_T",
    "StepFor_T",
    "StrokeCap_T",
    "StrokeJoin_T",
    "Temporal",
    "TextBaseline_T",
    "TextDirection_T",
    "TimeInterval_T",
    "TitleAnchor_T",
    "TitleFrame_T",
    "TitleOrient_T",
    "TypeForShape_T",
    "Type_T",
    "Value",
    "VegaThemes",
    "WindowOnlyOp_T",
    "is_color_hex",
]


T = TypeVar("T")
OneOrSeq = TypeAliasType("OneOrSeq", Union[T, Sequence[T]], type_params=(T,))
"""
One of ``T`` specified type(s), or a `Sequence` of such.

Examples
--------
The parameters ``short``, ``long`` accept the same range of types::

    # ruff: noqa: UP006, UP007

    def func(
        short: OneOrSeq[str | bool | float],
        long: Union[str, bool, float, Sequence[Union[str, bool, float]],
    ): ...
"""


class Value(TypedDict, Generic[T]):
    """
    A `Generic`_ single item ``dict``.

    Parameters
    ----------
    value: T
        Wrapped value.

    .. _Generic:
        https://typing.readthedocs.io/en/latest/spec/generics.html#generics
    """

    value: T


ColorHex = Annotated[
    LiteralString,
    re.compile(r"#[0-9a-f]{2}[0-9a-f]{2}[0-9a-f]{2}([0-9a-f]{2})?", re.IGNORECASE),
]
"""
A `hexadecimal`_ color code.

Corresponds to the ``json-schema`` string format:

    {"format": "color-hex", "type": "string"}

Examples
--------
:

    "#f0f8ff"
    "#7fffd4"
    "#000000"
    "#0000FF"
    "#0000ff80"

.. _hexadecimal:
    https://www.w3schools.com/html/html_colors_hex.asp
"""


def is_color_hex(obj: Any) -> TypeIs[ColorHex]:
    """Return ``True`` if the object is a hexadecimal color code."""
    # NOTE: Extracts compiled pattern from metadata,
    # to avoid defining in multiple places.
    it = iter(get_args(ColorHex))
    next(it)
    pattern: re.Pattern[str] = next(it)
    return bool(pattern.fullmatch(obj))


class RowColKwds(TypedDict, Generic[T], total=False):
    """
    A `Generic`_ two-item ``dict``.

    Parameters
    ----------
    column: T
    row: T

    .. _Generic:
        https://typing.readthedocs.io/en/latest/spec/generics.html#generics
    """

    column: T
    row: T


class PaddingKwds(TypedDict, total=False):
    bottom: float
    left: float
    right: float
    top: float


Temporal: TypeAlias = Union[date, datetime]

VegaThemes: TypeAlias = Literal[
    "carbong10",
    "carbong100",
    "carbong90",
    "carbonwhite",
    "dark",
    "excel",
    "fivethirtyeight",
    "ggplot2",
    "googlecharts",
    "latimes",
    "powerbi",
    "quartz",
    "urbaninstitute",
    "vox",
]
Map: TypeAlias = Mapping[str, Any]
PrimitiveValue_T: TypeAlias = Union[str, bool, float, None]
AggregateOp_T: TypeAlias = Literal[
    "argmax",
    "argmin",
    "average",
    "count",
    "distinct",
    "max",
    "mean",
    "median",
    "min",
    "missing",
    "product",
    "q1",
    "q3",
    "ci0",
    "ci1",
    "stderr",
    "stdev",
    "stdevp",
    "sum",
    "valid",
    "values",
    "variance",
    "variancep",
    "exponential",
    "exponentialb",
]
Align_T: TypeAlias = Literal["left", "center", "right"]
AllSortString_T: TypeAlias = Literal[
    "ascending",
    "descending",
    "x",
    "y",
    "color",
    "fill",
    "stroke",
    "strokeWidth",
    "size",
    "shape",
    "fillOpacity",
    "strokeOpacity",
    "opacity",
    "text",
    "-x",
    "-y",
    "-color",
    "-fill",
    "-stroke",
    "-strokeWidth",
    "-size",
    "-shape",
    "-fillOpacity",
    "-strokeOpacity",
    "-opacity",
    "-text",
]
AutosizeType_T: TypeAlias = Literal["pad", "none", "fit", "fit-x", "fit-y"]
AxisOrient_T: TypeAlias = Literal["top", "bottom", "left", "right"]
BinnedTimeUnit_T: TypeAlias = Literal[
    "binnedyear",
    "binnedyearquarter",
    "binnedyearquartermonth",
    "binnedyearmonth",
    "binnedyearmonthdate",
    "binnedyearmonthdatehours",
    "binnedyearmonthdatehoursminutes",
    "binnedyearmonthdatehoursminutesseconds",
    "binnedyearweek",
    "binnedyearweekday",
    "binnedyearweekdayhours",
    "binnedyearweekdayhoursminutes",
    "binnedyearweekdayhoursminutesseconds",
    "binnedyeardayofyear",
    "binnedutcyear",
    "binnedutcyearquarter",
    "binnedutcyearquartermonth",
    "binnedutcyearmonth",
    "binnedutcyearmonthdate",
    "binnedutcyearmonthdatehours",
    "binnedutcyearmonthdatehoursminutes",
    "binnedutcyearmonthdatehoursminutesseconds",
    "binnedutcyearweek",
    "binnedutcyearweekday",
    "binnedutcyearweekdayhours",
    "binnedutcyearweekdayhoursminutes",
    "binnedutcyearweekdayhoursminutesseconds",
    "binnedutcyeardayofyear",
]
Blend_T: TypeAlias = Literal[
    None,
    "multiply",
    "screen",
    "overlay",
    "darken",
    "lighten",
    "color-dodge",
    "color-burn",
    "hard-light",
    "soft-light",
    "difference",
    "exclusion",
    "hue",
    "saturation",
    "color",
    "luminosity",
]
BoxPlot_T: TypeAlias = Literal["boxplot"]
ColorName_T: TypeAlias = Literal[
    "black",
    "silver",
    "gray",
    "white",
    "maroon",
    "red",
    "purple",
    "fuchsia",
    "green",
    "lime",
    "olive",
    "yellow",
    "navy",
    "blue",
    "teal",
    "aqua",
    "orange",
    "aliceblue",
    "antiquewhite",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "blanchedalmond",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkgrey",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkslategrey",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "greenyellow",
    "grey",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgray",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightslategrey",
    "lightsteelblue",
    "lightyellow",
    "limegreen",
    "linen",
    "magenta",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "oldlace",
    "olivedrab",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "skyblue",
    "slateblue",
    "slategray",
    "slategrey",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "whitesmoke",
    "yellowgreen",
    "rebeccapurple",
]
ColorScheme_T: TypeAlias = Literal[
    "accent",
    "category10",
    "category20",
    "category20b",
    "category20c",
    "dark2",
    "paired",
    "pastel1",
    "pastel2",
    "set1",
    "set2",
    "set3",
    "tableau10",
    "tableau20",
    "observable10",
    "blues",
    "tealblues",
    "teals",
    "greens",
    "browns",
    "greys",
    "purples",
    "warmgreys",
    "reds",
    "oranges",
    "turbo",
    "viridis",
    "inferno",
    "magma",
    "plasma",
    "cividis",
    "bluegreen",
    "bluegreen-3",
    "bluegreen-4",
    "bluegreen-5",
    "bluegreen-6",
    "bluegreen-7",
    "bluegreen-8",
    "bluegreen-9",
    "bluepurple",
    "bluepurple-3",
    "bluepurple-4",
    "bluepurple-5",
    "bluepurple-6",
    "bluepurple-7",
    "bluepurple-8",
    "bluepurple-9",
    "goldgreen",
    "goldgreen-3",
    "goldgreen-4",
    "goldgreen-5",
    "goldgreen-6",
    "goldgreen-7",
    "goldgreen-8",
    "goldgreen-9",
    "goldorange",
    "goldorange-3",
    "goldorange-4",
    "goldorange-5",
    "goldorange-6",
    "goldorange-7",
    "goldorange-8",
    "goldorange-9",
    "goldred",
    "goldred-3",
    "goldred-4",
    "goldred-5",
    "goldred-6",
    "goldred-7",
    "goldred-8",
    "goldred-9",
    "greenblue",
    "greenblue-3",
    "greenblue-4",
    "greenblue-5",
    "greenblue-6",
    "greenblue-7",
    "greenblue-8",
    "greenblue-9",
    "orangered",
    "orangered-3",
    "orangered-4",
    "orangered-5",
    "orangered-6",
    "orangered-7",
    "orangered-8",
    "orangered-9",
    "purplebluegreen",
    "purplebluegreen-3",
    "purplebluegreen-4",
    "purplebluegreen-5",
    "purplebluegreen-6",
    "purplebluegreen-7",
    "purplebluegreen-8",
    "purplebluegreen-9",
    "purpleblue",
    "purpleblue-3",
    "purpleblue-4",
    "purpleblue-5",
    "purpleblue-6",
    "purpleblue-7",
    "purpleblue-8",
    "purpleblue-9",
    "purplered",
    "purplered-3",
    "purplered-4",
    "purplered-5",
    "purplered-6",
    "purplered-7",
    "purplered-8",
    "purplered-9",
    "redpurple",
    "redpurple-3",
    "redpurple-4",
    "redpurple-5",
    "redpurple-6",
    "redpurple-7",
    "redpurple-8",
    "redpurple-9",
    "yellowgreenblue",
    "yellowgreenblue-3",
    "yellowgreenblue-4",
    "yellowgreenblue-5",
    "yellowgreenblue-6",
    "yellowgreenblue-7",
    "yellowgreenblue-8",
    "yellowgreenblue-9",
    "yellowgreen",
    "yellowgreen-3",
    "yellowgreen-4",
    "yellowgreen-5",
    "yellowgreen-6",
    "yellowgreen-7",
    "yellowgreen-8",
    "yellowgreen-9",
    "yelloworangebrown",
    "yelloworangebrown-3",
    "yelloworangebrown-4",
    "yelloworangebrown-5",
    "yelloworangebrown-6",
    "yelloworangebrown-7",
    "yelloworangebrown-8",
    "yelloworangebrown-9",
    "yelloworangered",
    "yelloworangered-3",
    "yelloworangered-4",
    "yelloworangered-5",
    "yelloworangered-6",
    "yelloworangered-7",
    "yelloworangered-8",
    "yelloworangered-9",
    "darkblue",
    "darkblue-3",
    "darkblue-4",
    "darkblue-5",
    "darkblue-6",
    "darkblue-7",
    "darkblue-8",
    "darkblue-9",
    "darkgold",
    "darkgold-3",
    "darkgold-4",
    "darkgold-5",
    "darkgold-6",
    "darkgold-7",
    "darkgold-8",
    "darkgold-9",
    "darkgreen",
    "darkgreen-3",
    "darkgreen-4",
    "darkgreen-5",
    "darkgreen-6",
    "darkgreen-7",
    "darkgreen-8",
    "darkgreen-9",
    "darkmulti",
    "darkmulti-3",
    "darkmulti-4",
    "darkmulti-5",
    "darkmulti-6",
    "darkmulti-7",
    "darkmulti-8",
    "darkmulti-9",
    "darkred",
    "darkred-3",
    "darkred-4",
    "darkred-5",
    "darkred-6",
    "darkred-7",
    "darkred-8",
    "darkred-9",
    "lightgreyred",
    "lightgreyred-3",
    "lightgreyred-4",
    "lightgreyred-5",
    "lightgreyred-6",
    "lightgreyred-7",
    "lightgreyred-8",
    "lightgreyred-9",
    "lightgreyteal",
    "lightgreyteal-3",
    "lightgreyteal-4",
    "lightgreyteal-5",
    "lightgreyteal-6",
    "lightgreyteal-7",
    "lightgreyteal-8",
    "lightgreyteal-9",
    "lightmulti",
    "lightmulti-3",
    "lightmulti-4",
    "lightmulti-5",
    "lightmulti-6",
    "lightmulti-7",
    "lightmulti-8",
    "lightmulti-9",
    "lightorange",
    "lightorange-3",
    "lightorange-4",
    "lightorange-5",
    "lightorange-6",
    "lightorange-7",
    "lightorange-8",
    "lightorange-9",
    "lighttealblue",
    "lighttealblue-3",
    "lighttealblue-4",
    "lighttealblue-5",
    "lighttealblue-6",
    "lighttealblue-7",
    "lighttealblue-8",
    "lighttealblue-9",
    "blueorange",
    "blueorange-3",
    "blueorange-4",
    "blueorange-5",
    "blueorange-6",
    "blueorange-7",
    "blueorange-8",
    "blueorange-9",
    "blueorange-10",
    "blueorange-11",
    "brownbluegreen",
    "brownbluegreen-3",
    "brownbluegreen-4",
    "brownbluegreen-5",
    "brownbluegreen-6",
    "brownbluegreen-7",
    "brownbluegreen-8",
    "brownbluegreen-9",
    "brownbluegreen-10",
    "brownbluegreen-11",
    "purplegreen",
    "purplegreen-3",
    "purplegreen-4",
    "purplegreen-5",
    "purplegreen-6",
    "purplegreen-7",
    "purplegreen-8",
    "purplegreen-9",
    "purplegreen-10",
    "purplegreen-11",
    "pinkyellowgreen",
    "pinkyellowgreen-3",
    "pinkyellowgreen-4",
    "pinkyellowgreen-5",
    "pinkyellowgreen-6",
    "pinkyellowgreen-7",
    "pinkyellowgreen-8",
    "pinkyellowgreen-9",
    "pinkyellowgreen-10",
    "pinkyellowgreen-11",
    "purpleorange",
    "purpleorange-3",
    "purpleorange-4",
    "purpleorange-5",
    "purpleorange-6",
    "purpleorange-7",
    "purpleorange-8",
    "purpleorange-9",
    "purpleorange-10",
    "purpleorange-11",
    "redblue",
    "redblue-3",
    "redblue-4",
    "redblue-5",
    "redblue-6",
    "redblue-7",
    "redblue-8",
    "redblue-9",
    "redblue-10",
    "redblue-11",
    "redgrey",
    "redgrey-3",
    "redgrey-4",
    "redgrey-5",
    "redgrey-6",
    "redgrey-7",
    "redgrey-8",
    "redgrey-9",
    "redgrey-10",
    "redgrey-11",
    "redyellowblue",
    "redyellowblue-3",
    "redyellowblue-4",
    "redyellowblue-5",
    "redyellowblue-6",
    "redyellowblue-7",
    "redyellowblue-8",
    "redyellowblue-9",
    "redyellowblue-10",
    "redyellowblue-11",
    "redyellowgreen",
    "redyellowgreen-3",
    "redyellowgreen-4",
    "redyellowgreen-5",
    "redyellowgreen-6",
    "redyellowgreen-7",
    "redyellowgreen-8",
    "redyellowgreen-9",
    "redyellowgreen-10",
    "redyellowgreen-11",
    "spectral",
    "spectral-3",
    "spectral-4",
    "spectral-5",
    "spectral-6",
    "spectral-7",
    "spectral-8",
    "spectral-9",
    "spectral-10",
    "spectral-11",
    "rainbow",
    "sinebow",
]
CompositeMark_T: TypeAlias = Literal["boxplot", "errorbar", "errorband"]
Cursor_T: TypeAlias = Literal[
    "auto",
    "default",
    "none",
    "context-menu",
    "help",
    "pointer",
    "progress",
    "wait",
    "cell",
    "crosshair",
    "text",
    "vertical-text",
    "alias",
    "copy",
    "move",
    "no-drop",
    "not-allowed",
    "e-resize",
    "n-resize",
    "ne-resize",
    "nw-resize",
    "s-resize",
    "se-resize",
    "sw-resize",
    "w-resize",
    "ew-resize",
    "ns-resize",
    "nesw-resize",
    "nwse-resize",
    "col-resize",
    "row-resize",
    "all-scroll",
    "zoom-in",
    "zoom-out",
    "grab",
    "grabbing",
]
ErrorBand_T: TypeAlias = Literal["errorband"]
ErrorBarExtent_T: TypeAlias = Literal["ci", "iqr", "stderr", "stdev"]
ErrorBar_T: TypeAlias = Literal["errorbar"]
FontWeight_T: TypeAlias = Literal[
    "normal", "bold", "lighter", "bolder", 100, 200, 300, 400, 500, 600, 700, 800, 900
]
ImputeMethod_T: TypeAlias = Literal["value", "median", "max", "min", "mean"]
Interpolate_T: TypeAlias = Literal[
    "basis",
    "basis-open",
    "basis-closed",
    "bundle",
    "cardinal",
    "cardinal-open",
    "cardinal-closed",
    "catmull-rom",
    "linear",
    "linear-closed",
    "monotone",
    "natural",
    "step",
    "step-before",
    "step-after",
]
LayoutAlign_T: TypeAlias = Literal["all", "each", "none"]
LegendOrient_T: TypeAlias = Literal[
    "none",
    "left",
    "right",
    "top",
    "bottom",
    "top-left",
    "top-right",
    "bottom-left",
    "bottom-right",
]
MarkInvalidDataMode_T: TypeAlias = Literal[
    "filter",
    "break-paths-filter-domains",
    "break-paths-show-domains",
    "break-paths-show-path-domains",
    "show",
]
MarkType_T: TypeAlias = Literal[
    "arc",
    "area",
    "image",
    "group",
    "line",
    "path",
    "rect",
    "rule",
    "shape",
    "symbol",
    "text",
    "trail",
]
Mark_T: TypeAlias = Literal[
    "arc",
    "area",
    "bar",
    "image",
    "line",
    "point",
    "rect",
    "rule",
    "text",
    "tick",
    "trail",
    "circle",
    "square",
    "geoshape",
]
MultiTimeUnit_T: TypeAlias = Literal[
    "yearquarter",
    "yearquartermonth",
    "yearmonth",
    "yearmonthdate",
    "yearmonthdatehours",
    "yearmonthdatehoursminutes",
    "yearmonthdatehoursminutesseconds",
    "yearweek",
    "yearweekday",
    "yearweekdayhours",
    "yearweekdayhoursminutes",
    "yearweekdayhoursminutesseconds",
    "yeardayofyear",
    "quartermonth",
    "monthdate",
    "monthdatehours",
    "monthdatehoursminutes",
    "monthdatehoursminutesseconds",
    "weekday",
    "weekdayhours",
    "weekdayhoursminutes",
    "weekdayhoursminutesseconds",
    "dayhours",
    "dayhoursminutes",
    "dayhoursminutesseconds",
    "hoursminutes",
    "hoursminutesseconds",
    "minutesseconds",
    "secondsmilliseconds",
    "utcyearquarter",
    "utcyearquartermonth",
    "utcyearmonth",
    "utcyearmonthdate",
    "utcyearmonthdatehours",
    "utcyearmonthdatehoursminutes",
    "utcyearmonthdatehoursminutesseconds",
    "utcyearweek",
    "utcyearweekday",
    "utcyearweekdayhours",
    "utcyearweekdayhoursminutes",
    "utcyearweekdayhoursminutesseconds",
    "utcyeardayofyear",
    "utcquartermonth",
    "utcmonthdate",
    "utcmonthdatehours",
    "utcmonthdatehoursminutes",
    "utcmonthdatehoursminutesseconds",
    "utcweekday",
    "utcweekdayhours",
    "utcweekdayhoursminutes",
    "utcweekdayhoursminutesseconds",
    "utcdayhours",
    "utcdayhoursminutes",
    "utcdayhoursminutesseconds",
    "utchoursminutes",
    "utchoursminutesseconds",
    "utcminutesseconds",
    "utcsecondsmilliseconds",
]
NonArgAggregateOp_T: TypeAlias = Literal[
    "average",
    "count",
    "distinct",
    "max",
    "mean",
    "median",
    "min",
    "missing",
    "product",
    "q1",
    "q3",
    "ci0",
    "ci1",
    "stderr",
    "stdev",
    "stdevp",
    "sum",
    "valid",
    "values",
    "variance",
    "variancep",
    "exponential",
    "exponentialb",
]
Orient_T: TypeAlias = Literal["left", "right", "top", "bottom"]
Orientation_T: TypeAlias = Literal["horizontal", "vertical"]
ProjectionType_T: TypeAlias = Literal[
    "albers",
    "albersUsa",
    "azimuthalEqualArea",
    "azimuthalEquidistant",
    "conicConformal",
    "conicEqualArea",
    "conicEquidistant",
    "equalEarth",
    "equirectangular",
    "gnomonic",
    "identity",
    "mercator",
    "naturalEarth1",
    "orthographic",
    "stereographic",
    "transverseMercator",
]
RangeEnum_T: TypeAlias = Literal[
    "width", "height", "symbol", "category", "ordinal", "ramp", "diverging", "heatmap"
]
ResolveMode_T: TypeAlias = Literal["independent", "shared"]
ScaleInterpolateEnum_T: TypeAlias = Literal[
    "rgb", "lab", "hcl", "hsl", "hsl-long", "hcl-long", "cubehelix", "cubehelix-long"
]
ScaleType_T: TypeAlias = Literal[
    "linear",
    "log",
    "pow",
    "sqrt",
    "symlog",
    "identity",
    "sequential",
    "time",
    "utc",
    "quantile",
    "quantize",
    "threshold",
    "bin-ordinal",
    "ordinal",
    "point",
    "band",
]
SelectionResolution_T: TypeAlias = Literal["global", "union", "intersect"]
SelectionType_T: TypeAlias = Literal["point", "interval"]
SingleDefUnitChannel_T: TypeAlias = Literal[
    "text",
    "shape",
    "x",
    "y",
    "xOffset",
    "yOffset",
    "x2",
    "y2",
    "longitude",
    "latitude",
    "longitude2",
    "latitude2",
    "theta",
    "theta2",
    "radius",
    "radius2",
    "color",
    "fill",
    "stroke",
    "opacity",
    "fillOpacity",
    "strokeOpacity",
    "strokeWidth",
    "strokeDash",
    "size",
    "angle",
    "key",
    "href",
    "url",
    "description",
]
SingleTimeUnit_T: TypeAlias = Literal[
    "year",
    "quarter",
    "month",
    "week",
    "day",
    "dayofyear",
    "date",
    "hours",
    "minutes",
    "seconds",
    "milliseconds",
    "utcyear",
    "utcquarter",
    "utcmonth",
    "utcweek",
    "utcday",
    "utcdayofyear",
    "utcdate",
    "utchours",
    "utcminutes",
    "utcseconds",
    "utcmilliseconds",
]
SortByChannel_T: TypeAlias = Literal[
    "x",
    "y",
    "color",
    "fill",
    "stroke",
    "strokeWidth",
    "size",
    "shape",
    "fillOpacity",
    "strokeOpacity",
    "opacity",
    "text",
]
SortOrder_T: TypeAlias = Literal["ascending", "descending"]
StackOffset_T: TypeAlias = Literal["zero", "center", "normalize"]
StandardType_T: TypeAlias = Literal["quantitative", "ordinal", "temporal", "nominal"]
StepFor_T: TypeAlias = Literal["position", "offset"]
StrokeCap_T: TypeAlias = Literal["butt", "round", "square"]
StrokeJoin_T: TypeAlias = Literal["miter", "round", "bevel"]
TextBaseline_T: TypeAlias = Literal[
    "alphabetic", "top", "middle", "bottom", "line-top", "line-bottom"
]
TextDirection_T: TypeAlias = Literal["ltr", "rtl"]
TimeInterval_T: TypeAlias = Literal[
    "millisecond", "second", "minute", "hour", "day", "week", "month", "year"
]
TitleAnchor_T: TypeAlias = Literal[None, "start", "middle", "end"]
TitleFrame_T: TypeAlias = Literal["bounds", "group"]
TitleOrient_T: TypeAlias = Literal["none", "left", "right", "top", "bottom"]
TypeForShape_T: TypeAlias = Literal["nominal", "ordinal", "geojson"]
Type_T: TypeAlias = Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"]
WindowOnlyOp_T: TypeAlias = Literal[
    "row_number",
    "rank",
    "dense_rank",
    "percent_rank",
    "cume_dist",
    "ntile",
    "lag",
    "lead",
    "first_value",
    "last_value",
    "nth_value",
]
