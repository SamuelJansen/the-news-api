from python_helper import Constant as c
from python_helper import StringHelper


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
                        *SYMBOLS
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

    filteredEmailBodySentenceList = [
        emailBodySentence if not '[http' in emailBodySentence else ' '.join([
            ' '.join([
                p if not (p.startswith('s://') or p.startswith('://')) else c.BLANK
                for p in part.split(']')
            ])
            for part in emailBodySentence.split('[http')
        ])
        for emailBodySentence in notFilteredEmailBodySentenceList
    ]

    emailBodySentenceList = [
        StringHelper.join(emailBodySentence.strip().split(), character=c.SPACE)
        for filteredEmailBodySentence in filteredEmailBodySentenceList
        for emailBodySentence in filteredEmailBodySentence.split(c.NEW_LINE)
        if (
            StringHelper.isNotBlank(emailBodySentence.strip()) and
            not c.DOT == emailBodySentence.strip() and
            not c.COMA == emailBodySentence.strip() and
            not '[Link]' == emailBodySentence.strip()
        )
    ]

    recentensedList = []
    for sentence in emailBodySentenceList:
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

    for punctuation in c.PUNCTUATION:
        emailBodySentenceList = [
            sentence.replace(f'{3*c.SPACE}{punctuation}', punctuation).replace(f'{2*c.SPACE}{punctuation}', punctuation).replace(f'{c.SPACE}{punctuation}', punctuation)
            for sentence in emailBodySentenceList
        ]

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
        sentence
        for sentence in emailBodySentenceList
        if (
            not sentence.lower().startswith('(imagem') and
            not sentence.lower().startswith('(gif') and
            not sentence.lower().startswith('(foto') and
            not sentence.lower().startswith('(print')
        )
    ]

    preCompiledEmailBodyList = []
    for sentence in emailBodySentenceList:
        if StringHelper.isNotBlank(sentence):
            if sentence.isupper():
                preCompiledEmailBodyList = [*preCompiledEmailBodyList[:-1], sentence, preCompiledEmailBodyList[-1]]
            elif 3 > len(sentence):
                preCompiledEmailBodyList[-1] = f'{preCompiledEmailBodyList[-1]}{c.SPACE}{sentence}'
            elif 256 > len(sentence) and sentence not in preCompiledEmailBodyList:
                preCompiledEmailBodyList.append(sentence)
            else:
                for s in sentence.split(c.DOT):
                    strippedSencence = s.strip()
                    if StringHelper.isNotBlank(strippedSencence):
                        preCompiledEmailBodyList.append(f'{strippedSencence}{c.DOT}')

    return [
        sentence.replace('<=', '&le;').replace('>=', '&ge;').replace('<', '&lt;').replace('>', '&gt;')
        for sentence in preCompiledEmailBodyList
    ]


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
                        '<div role="play buttom" onClick="handlePlayClick()" class="audio-circle"><span id="spam-audio-circle" class="material-icons">play_circle</span></div', ###- <button onClick="handlePlayClick()">voice over</button><div class="circle">
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
