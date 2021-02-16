__version__ = "0.1.16"

from .wildewidgets import (
    AltairChart,
    BarChart, 
    BasicMenu,
    DoughnutChart,
    Histogram,
    HorizontalBarChart, 
    HorizontalHistogram,
    HorizontalStackedBarChart,
    LightMenu,
    PieChart,
    StackedBarChart, 
    WildewidgetDispatch,
)

try:
    from .wildewidgets import (
        DataTable,
        DataTableFilter,
    )
except ImportError:
    pass