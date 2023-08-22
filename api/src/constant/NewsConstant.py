from python_helper import Constant
from enumeration.NewsStatus import NewsStatus


FILE_PREFIX_NAME = 'news'
FILE_EXTENSION = 'html'
DEFAULT_STATUS = NewsStatus.NONE
END_STATUS = NewsStatus.FINISHED

SPACES_AFTER_EXTRA = '          '
SYMBOLS = list({
    "@",
    '©',
    '®',
    '™',
    '℠',
    "#",
    "$",
    "%",
    "&",
    "=",
    "|",
    "_",
    "/",
    "*",
    "-",
    "+"
})
LONG_DASH = f'—'
SPACE_LONG_DASH_SPACE = f'{Constant.SPACE}—{Constant.SPACE}'
SPACE_DASH_SPACE = f'{Constant.SPACE}{Constant.DASH}{Constant.SPACE}'
THREE_DOTS = '…'
THREE_DOTS_TOKEN = '--THREE_DOTS--'
PUNCTUATION_LIST = [
    Constant.DOT,
    Constant.COMA,
    Constant.QUESTION_MARK,
    Constant.EXCLAMATION_MARK,
    Constant.SEMI_COLON,
    Constant.COLON,
    Constant.UNDERSCORE,
    THREE_DOTS,
    SPACE_DASH_SPACE,
    SPACE_LONG_DASH_SPACE
]
MAX_SENTENCE_SIZE = 256


WHAT_COMA = f'que{Constant.COMA}'
CUT_SENTENCE_CUT_LIST = [
    Constant.QUESTION_MARK,
    Constant.EXCLAMATION_MARK,
    Constant.COLON,
    Constant.SEMI_COLON,
    THREE_DOTS,
    LONG_DASH,
    Constant.DASH,
    Constant.COMA
]