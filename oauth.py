from FetchAnswers import AnswersFetcher

question_list = [
    24459652,
    34423047,
    60333636,
    24385122,
    23100254,
    46052366,
    53911719,
    58567916,
    30612820,
    22022036,
    41156195,
    40700971,
    36866494,
    26997744,
    26844780,
    28112915,
    31909770
]

fetcher = AnswersFetcher('air_fighter@163.com', 'airfighter049076')
for question_id in question_list:
    fetcher.fetch_to_single_file(question_id, './result/')
