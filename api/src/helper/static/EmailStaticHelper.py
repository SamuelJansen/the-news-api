from python_helper import Constant as c
from python_helper import StringHelper, ObjectHelper, log

from constant import NewsConstant


def customDebug(*args, **kwargs):
    log.prettyJson(customDebug, *args, logLevel=log.DEBUG, **kwargs)


def getCompiledEmailBodyList(plainTextEmail):
    isMarketing = False
    lastSentence = c.BLANK
    notFilteredEmailBodySentenceList = []
    for emailBodySentence in [
        emailBodySentenceUnity
        for emailBodySentenceUnity in [
            possibleEmailBodySentence.replace(f'\r', c.BLANK).strip()
            for possibleEmailBodySentence in plainTextEmail.split(f'{c.NEW_LINE}')
        ]
        if StringHelper.isNotBlank(emailBodySentenceUnity)
    ]:
        ###-customDebug('emailBodySentence', [emailBodySentence])
        sentenceEnd = emailBodySentence.split()[-1].strip()
        sentenceEndFilterd = StringHelper.join(
            [
                charactere
                for charactere in sentenceEnd
                if charactere in c.CHARACTERES
            ],
            character=c.BLANK
        )
        if (
            emailBodySentence.startswith('CLIQUE PARA COMPARTILHAR') or
            emailBodySentence.endswith('FL') or
            emailBodySentence.endswith('QUIZ THE NEWS') or
            emailBodySentence.endswith('QUIZ') or
            emailBodySentence.endswith('EDIÇÃO ESPECIAL DE SÁBADO') or
            emailBodySentence.endswith('PROGRAMA DE INDICAÇÃO') or
            emailBodySentence.endswith('GIVEAWAY DO DÊNIUS') or
            emailBodySentence.endswith('SUPER GIVEAWAY')
        ):
            isMarketing = True
        elif 4 < len(sentenceEndFilterd) and sentenceEnd[-1].isupper():
            if isMarketing:
                notFilteredEmailBodySentenceList.append(lastSentence)
            isMarketing = False
        if isMarketing:
            lastSentence = emailBodySentence
            if lastSentence in [
                'FL',
                'QUIZ THE NEWS',
                'QUIZ',
                'EDIÇÃO ESPECIAL DE SÁBADO',
                'PROGRAMA DE INDICAÇÃO',
                'GIVEAWAY DO DÊNIUS',
                'SUPER GIVEAWAY'
            ]:
                notFilteredEmailBodySentenceList.pop()
        else:
            if (
                (
                    4 < len(sentenceEnd) and
                    not sentenceEndFilterd[-1].isupper() and
                    not sentenceEndFilterd[-2].isupper() and
                    not sentenceEndFilterd[-3].isupper() and
                    not sentenceEndFilterd[-4].isupper() and
                    not sentenceEndFilterd[-5].isupper()
                ) if sentenceEnd[-1].isupper() else not isMarketing
            ):
                if 'PATROCINADO POR' in emailBodySentence:
                    isMarketing = True
                    if emailBodySentence.startswith('PATROCINADO POR'):
                        notFilteredEmailBodySentenceList.pop()
                else:
                    notFilteredEmailBodySentenceList.append(emailBodySentence)
            else:
                upperCaseWords = c.BLANK
                for charactere in reversed(emailBodySentence):
                    if charactere.isupper() or (charactere in [
                        c.SPACE,
                        *NewsConstant.SYMBOLS
                    ] and not c.BLANK == upperCaseWords):
                        upperCaseWords = f'{charactere}{upperCaseWords}'
                    elif c.BLANK == upperCaseWords:
                        upperCaseWords = c.BLANK
                    else:
                        break
                upperCaseWords = upperCaseWords.strip()
                sentence = emailBodySentence.replace(upperCaseWords, c.BLANK).strip()
                if (
                    upperCaseWords.startswith('PATROCINADO POR') or
                    upperCaseWords.startswith('CLIQUE PARA COMPARTILHAR') or
                    upperCaseWords.startswith('FL') or
                    upperCaseWords.startswith('QUIZ THE NEWS') or
                    upperCaseWords.startswith('QUIZ') or
                    upperCaseWords.startswith('EDIÇÃO ESPECIAL DE SÁBADO') or
                    upperCaseWords.startswith('PROGRAMA DE INDICAÇÃO') or
                    upperCaseWords.startswith('GIVEAWAY DO DÊNIUS') or
                    emailBodySentence.endswith('SUPER GIVEAWAY')
                ):
                    isMarketing = True
                    if StringHelper.isBlank(sentence):
                        rawMarketingSentence = notFilteredEmailBodySentenceList.pop()
                        splitedRawMarketingSentence = [
                            s.strip()
                            for s in rawMarketingSentence.split(f'{5*c.SPACE}')
                            if StringHelper.isNotBlank(s.strip())
                        ]
                        if 1 < len(splitedRawMarketingSentence):
                            for notMarketingSentence in splitedRawMarketingSentence[:-1]:
                                if StringHelper.isNotBlank(notMarketingSentence):
                                    notFilteredEmailBodySentenceList.append(notMarketingSentence)
                    else:
                        splitedRawMarketingSentence = [
                            s.strip()
                            for s in sentence.split(f'{5*c.SPACE}')
                            if StringHelper.isNotBlank(s.strip())
                        ]
                        if 1 < len(splitedRawMarketingSentence):
                            for notMarketingSentence in splitedRawMarketingSentence[:-1]:
                                if StringHelper.isNotBlank(notMarketingSentence):
                                    notFilteredEmailBodySentenceList.append(notMarketingSentence.strip())

                else:
                    if 4 < len(upperCaseWords) and not StringHelper.isBlank(sentence):
                        notFilteredEmailBodySentenceList.append(sentence.strip())
                        notFilteredEmailBodySentenceList.append(upperCaseWords.strip())
                    else:
                        notFilteredEmailBodySentenceList.append(emailBodySentence)

    ###-customDebug('notFilteredEmailBodySentenceList', notFilteredEmailBodySentenceList)

    filteredEmailBodySentenceList = [
        emailBodySentence if not '[http' in emailBodySentence else ' '.join([
            c.SPACE.join([
                p if not (p.startswith('s://') or p.startswith('://')) else c.BLANK
                for p in part.split(']')
            ])
            for part in emailBodySentence.split('[http')
        ])
        for emailBodySentence in notFilteredEmailBodySentenceList
    ]
    ###-customDebug('filteredEmailBodySentenceList', filteredEmailBodySentenceList)

    resplitedEmailBodySentenceList = []
    for sentence in filteredEmailBodySentenceList:
        strippedSentence = sentence.strip()
        if ObjectHelper.isNeitherNoneNorBlank(strippedSentence):
            if NewsConstant.SPACES_AFTER_EXTRA in strippedSentence:
                for s in strippedSentence.split(NewsConstant.SPACES_AFTER_EXTRA):
                    strippedSegment = s.strip()
                    if ObjectHelper.isNeitherNoneNorBlank(strippedSegment):
                        resplitedEmailBodySentenceList.append(s.strip())
            else:
                resplitedEmailBodySentenceList.append(strippedSentence)
    ###-customDebug('resplitedEmailBodySentenceList', resplitedEmailBodySentenceList)



    emailBodySentenceList = fixPunctuationIssues(resplitedEmailBodySentenceList)
    ###-customDebug('emailBodySentenceList', emailBodySentenceList)

    emailBodySentenceList = [
        removeDoubleOrMoreSpaces(emailBodySentence)
        for filteredEmailBodySentence in emailBodySentenceList
        for emailBodySentence in filteredEmailBodySentence.split(c.NEW_LINE)
        if (
            StringHelper.isNotBlank(emailBodySentence.strip()) and
            not c.DOT == emailBodySentence.strip() and
            not c.COMA == emailBodySentence.strip() and
            not '[Link]' == emailBodySentence.strip()
        )
    ]

    emailBodySentenceList = fixPunctuationIssues(emailBodySentenceList)

    emailBodySentenceList = [
        sentence\
            .replace(c.BACK_SLASH_DOUBLE_QUOTE, c.SINGLE_QUOTE)\
            .replace(c.DOUBLE_QUOTE, c.SINGLE_QUOTE)\
            .replace('&nbsp;', c.BLANK)\
            .replace('\U0001fa99', c.BLANK)\
            .replace(c.AND, f'{c.SPACE}and{c.SPACE}')
        for sentence in emailBodySentenceList
    ]


    emailBodySentenceList = [
        removeDoubleOrMoreSpaces(sentence)
        for sentence in emailBodySentenceList
        if (
            not sentence.lower().startswith('(imagem') and
            not sentence.lower().startswith('(ilustração') and
            not sentence.lower().startswith('(gif') and
            not sentence.lower().startswith('(foto') and
            not sentence.lower().startswith('(print') and
            not sentence.lower().startswith('(Imagem') and
            not sentence.lower().startswith('(Ilustração') and
            not sentence.lower().startswith('(Gif') and
            not sentence.lower().startswith('(Foto') and
            not sentence.lower().startswith('(Print') and
            not sentence.lower().startswith('(magem') and
            not sentence.lower().startswith('(lustração') and
            not sentence.lower().startswith('(if') and
            not sentence.lower().startswith('(oto') and
            not sentence.lower().startswith('(rint')
        )
    ]

    preCompiledEmailBodyList = []
    for sentence in emailBodySentenceList:
        if StringHelper.isNotBlank(sentence):
            if sentence.isupper():
                preCompiledEmailBodyList = [*preCompiledEmailBodyList[:-1], sentence, preCompiledEmailBodyList[-1]]
            elif 3 > len(sentence):
                preCompiledEmailBodyList[-1] = f'{preCompiledEmailBodyList[-1]}{c.SPACE}{sentence}'
            elif NewsConstant.MAX_SENTENCE_SIZE > len(sentence) and sentence not in preCompiledEmailBodyList:
                preCompiledEmailBodyList.append(sentence)
            else:
                for s in sentence.split(c.DOT):
                    strippedSentence = s.strip()
                    if NewsConstant.MAX_SENTENCE_SIZE <= len(strippedSentence):
                        log.warning(getCompiledEmailBodyList, f'Sentence is too large: {strippedSentence}')
                        cutAndAppendCuttedSentences(strippedSentence, NewsConstant.CUT_SENTENCE_CUT_LIST, preCompiledEmailBodyList)
                    elif ObjectHelper.isNeitherNoneNorBlank(strippedSentence):
                        preCompiledEmailBodyList.append(f'{strippedSentence}{c.DOT}')
    ###-customDebug('preCompiledEmailBodyList', preCompiledEmailBodyList)

    emailBodyWithSpecialCharacteresReplacedList = [
        sentence.replace('<=', '&le;').replace('>=', '&ge;').replace('<', '&lt;').replace('>', '&gt;')
        for sentence in preCompiledEmailBodyList
    ]

    emailBodySentenceList = fixPunctuationIssues([
        removeDoubleOrMoreSpaces(sentence)
        for sentence in emailBodyWithSpecialCharacteresReplacedList
    ])
    ###- customDebug('emailBodySentenceList', emailBodySentenceList)
    return emailBodySentenceList


def buildHtml(textHtmlEmailList):
    parsedTextHtmlEmailList = []
    for textHtmlEmail in textHtmlEmailList:
        rawHtml = str(textHtmlEmail)
        rawHtml = rawHtml.replace(
            '</head>',
            '''<link rel="icon" type="image/x-icon" href="https://cdn.data-explore.com/favicon.ico"><link rel='stylesheet' href='https://fonts.googleapis.com/icon?family=Material+Icons'><link rel="stylesheet" href="{{staticUrl}}/util-style.css"/></head>'''
        )
        collectedBody = []
        for index, bodyPart in enumerate(rawHtml.split('<body')):
            if index > 0:
                splitHtml = bodyPart.split('>')
                parsedBodyPart = StringHelper.join(
                    [
                        splitHtml[0],
                        '<div role="play buttom" onClick="handlePlayClick()" class="audio-circle"><span id="spam-audio-circle" class="material-icons">play_circle</span></div',
                        *splitHtml[1:]
                    ],
                    character='>'
                )
            else:
                parsedBodyPart = bodyPart
            collectedBody.append(parsedBodyPart)
        html = StringHelper.join(collectedBody, character='<body')
        parsedTextHtmlEmailList.append(
            html.replace(
                '</body>',
                '<script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"></script><script src="{{staticUrl}}/utils.js"></script></body>'
            )
        )
    return parsedTextHtmlEmailList


def fixPunctuationIssues(sentenceList):
    sentenceListWithDotSpaceAdded = [
        c.BLANK.join([
            f'{segment}{c.DOT_SPACE if shouldAddADotSpace(sentence, segment) else c.SPACE}'
            for segment in sentence.split(2*c.SPACE)
        ])
        for sentence in sentenceList
    ]

    filteredSentenceList = []
    for sentence in sentenceListWithDotSpaceAdded:
        filteredSentence = sentence.replace(f'{4*c.DOT}', f'{NewsConstant.THREE_DOTS_TOKEN}{c.SPACE}')
        filteredSentence = filteredSentence.replace(f'{3*c.DOT}', NewsConstant.THREE_DOTS_TOKEN)
        for punctuation in NewsConstant.PUNCTUATION_LIST:
            filteredSentence = filteredSentence.replace(f'{punctuation}{c.DOT}', f'{punctuation}{c.SPACE}')
            filteredSentence = filteredSentence.replace(f'{c.DOT}{punctuation}', f'{punctuation}{c.SPACE}')
            filteredSentence = filteredSentence.replace(f'{c.SPACE}{punctuation}', f'{punctuation}{c.SPACE}')
        filteredSentence = filteredSentence.replace(NewsConstant.THREE_DOTS_TOKEN, f'{NewsConstant.THREE_DOTS}')
        filteredSentence = filteredSentence.replace(f'{3*NewsConstant.THREE_DOTS}', f'{NewsConstant.THREE_DOTS}{c.SPACE}')
        filteredSentence = filteredSentence.replace(f'{2*NewsConstant.THREE_DOTS}', f'{NewsConstant.THREE_DOTS}{c.SPACE}')
        filteredSentenceList.append(filteredSentence.strip())

    recentensedList = []
    for sentence in filteredSentenceList:
        if sentence.startswith(c.DOT_SPACE) or sentence.startswith(c.COMA_SPACE):
            if sentence.startswith(c.DOT_SPACE):
                recentensedList[-1] = f'{recentensedList[-1]}{c.DOT}'
            else:
                recentensedList[-1] = f'{recentensedList[-1]}{c.COMA}'
            recentensedList.append(sentence[2:].strip())
        else:
            recentensedList.append(sentence.strip())

    emailBodySentenceList = []
    for sentence in recentensedList:
        if sentence.startswith(c.DOT) or sentence.startswith(c.COMA):
            if sentence.startswith(c.DOT):
                emailBodySentenceList[-1] = f'{emailBodySentenceList[-1]}{c.DOT}'
            else:
                emailBodySentenceList[-1] = f'{emailBodySentenceList[-1]}{c.COMA}'
            emailBodySentenceList.append(sentence[1:].strip())
        else:
            emailBodySentenceList.append(sentence.strip())

    for punctuation in NewsConstant.PUNCTUATION_LIST:
        emailBodySentenceList = [
            sentence.replace(f'{3*c.SPACE}{punctuation}', punctuation).replace(f'{2*c.SPACE}{punctuation}', punctuation).replace(f'{c.SPACE}{punctuation}', punctuation)
            for sentence in emailBodySentenceList
        ]

    return [
        removeDoubleOrMoreSpaces(sentence)
        for sentence in emailBodySentenceList
    ]


def removeDoubleOrMoreSpaces(sentence):
    return StringHelper.join(
        [
            word.strip()
            for word in sentence.strip().split()
            if ObjectHelper.isNeitherNoneNorBlank(word)
        ],
        character=c.SPACE
    )


def cutAndAppendCuttedSentences(sentence, tokenList, emailBodyList):
    # print(f'{sentence=}')
    # print(f'{tokenList=}')
    # print(0 < len(tokenList) and tokenList[0] in sentence)
    if 0 >= len(tokenList):
        stripedSentence = sentence.strip()
        emailBodyList.append(
            f'''{stripedSentence}{getPunctuationSufix(stripedSentence, tokenList, stripedSentence)}'''
        )
    elif 0 < len(tokenList) and tokenList[0] in sentence:
        evaluatedSplitedSentenceList = sentence.split(tokenList[0])
        if 1 < len(evaluatedSplitedSentenceList):
            if ObjectHelper.equals(c.COMA, tokenList[0]):
                splitedSentenceList = [
                    StringHelper.join(
                        evaluatedSplitedSentenceList[:-1],
                        character = tokenList[0]
                    ),
                    evaluatedSplitedSentenceList[-1]
                ]
            else:
                splitedSentenceList = [*evaluatedSplitedSentenceList]
            # print(f'{splitedSentenceList=}')
            for segment in splitedSentenceList:
                strippedSegment = segment.strip()
                # print(f'{strippedSegment=}')
                if NewsConstant.MAX_SENTENCE_SIZE <= len(strippedSegment):
                    cutAndAppendCuttedSentences(strippedSegment, tokenList[1:], emailBodyList)
                elif ObjectHelper.isNeitherNoneNorBlank(strippedSegment):
                    emailBodyList.append(
                        f'''{strippedSegment}{getPunctuationSufix(splitedSentenceList[-1], tokenList[0], segment)}'''
                    )
        else:
            cutAndAppendCuttedSentences(sentence, tokenList[1:], emailBodyList)
    elif f'que{c.COMA}' in sentence and 1 < len(sentence.split(NewsConstant.WHAT_COMA)):
        splitedSentenceList = sentence.split(NewsConstant.WHAT_COMA)
        for segment in splitedSentenceList:
            strippedSegment = segment.strip()
            if ObjectHelper.isNeitherNoneNorBlank(strippedSegment):
                emailBodyList.append(f'''{strippedSegment}{(f"{c.SPACE}{'que'}{c.COLON}" if splitedSentenceList[-1] is not segment else c.BLANK)}''')
    else:
        cutAndAppendCuttedSentences(sentence, tokenList[1:], emailBodyList)


def shouldAddADotSpace(sentence, segment):
    splitedSentence = sentence.split('  ')
    strippedSegment = segment.strip()
    return (
        ObjectHelper.isNeitherNoneNorBlank(strippedSegment)
    ) and (
        not strippedSegment.isupper()
    ) and (
        (
            splitedSentence.index(segment) == len(splitedSentence)-1
        ) or (
            (
                1 < len(segment.split()[-1].strip())
            ) and (
                splitedSentence.index(segment) < len(splitedSentence)-1
            ) and (
                ObjectHelper.isNeitherNoneNorBlank(splitedSentence[splitedSentence.index(segment)+1].strip())
            ) and (
                splitedSentence[splitedSentence.index(segment)+1].strip()[0].isupper()
            )
        )
    ) and (
        strippedSegment[-1] not in NewsConstant.PUNCTUATION_LIST
    ) and (
        (
            strippedSegment[-1] in c.CHARACTERES
        ) or (
            strippedSegment[-1] in c.NUMBERS
        )
    )


def getPunctuationSufix(sentence, token, segment):
    return (
        f"{token}"
        if sentence is not segment and (
            (
                token not in [
                    NewsConstant.LONG_DASH,
                    NewsConstant.SPACE_LONG_DASH_SPACE,
                    c.DASH,
                    NewsConstant.SPACE_DASH_SPACE
                ]
            )
        ) else c.BLANK
    )
