import requests
import json

graphql_url = "https://leetcode.com/graphql/"    

def fetch_problems_count():
    payload = json.dumps({
        "query": "\n    query userSessionProgress($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  matchedUser(username: $username) {\n    submitStats {\n      acSubmissionNum {\n        difficulty\n        count\n        submissions\n      }\n      totalSubmissionNum {\n        difficulty\n        count\n        submissions\n      }\n    }\n  }\n}\n    ",
        "variables": {
            "username": "TheAnshul"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=a6s056N8TPfSqj5oIXkR0kpG7Aurmk8IAoXcDo4RjG2qRpTo0HFRwvxQABrqzbh1'
    }
    response = requests.request("POST", graphql_url, headers=headers, data=payload).json()
    return response['data']['allQuestionsCount'][0]['count']

def fetch_all_problems():
    count = fetch_problems_count()
    payload = json.dumps({
        "query": "\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ",
        "variables": {
            "categorySlug": "",
            "skip": 0,
            "limit": count,
            "filters": {}
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=a6s056N8TPfSqj5oIXkR0kpG7Aurmk8IAoXcDo4RjG2qRpTo0HFRwvxQABrqzbh1'
    }
    response = requests.request("POST", graphql_url, headers=headers, data=payload).json()
    response = response['data']['problemsetQuestionList']['questions']
    with open("problems.json", "w") as outfile:
        json.dump(response, outfile)
