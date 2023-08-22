from python_helper import TestHelper
TestHelper.run(__file__, inspectGlobals=False)

# TestHelper.run(
#     __file__,
#     runOnly = [
#         'EmailStaticHelperTest.getCompleteEmailBodyList_whatMore',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_whenSentenceIsTooLargeBySemiColon',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_badSequence',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_comaSplitNonsense',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_specificCase_tooManyeSpaces',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_whenWhatMore',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_whenTooManyLinks',
#         'EmailStaticHelperTest.getCompiledEmailBodyList_whenTooClutered',
#         'EmailStaticHelperTest.cutAndAppendCuttedSentences'
#     ]
# )
