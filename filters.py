from enum import Enum
import config


class Filter(Enum):
    MOST_RECENT = config.filter_recent
    RELEVANCE = config.filter_relevance
    LOWEST_PRICE = config.filter_lowest

