from app.models.analytic import BattingMetric, BattingQuery
from app.services.analytics.batting_analytics import get_batting_ranking
from app.services.analytics.query_service import answer_batting_query
from app.models.match import Innings

# Use an actual parsed innings here
innings = [
      {
        "batting_team": "BELIEVERS",
        "bowling_team": "Red Wings",
        "overs": "20.0",
        "runs": 149,
        "wickets": 6,
        "innings_number": 1,
        "innings_type": "regular",
        "super_over_number": None,
        "batting": [
          {
            "player_name": "TiRtha2051",
            "batting_position": 1,
            "dismissal": "c",
            "dismissal_details": "Tagore b Sai",
            "runs": 1,
            "balls_faced": 3,
            "minutes": 4,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 33.33
          },
          {
            "player_name": "Ramesh Babu",
            "batting_position": 2,
            "dismissal": "c",
            "dismissal_details": "SRI b Harry Shergill",
            "runs": 2,
            "balls_faced": 5,
            "minutes": 14,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 40
          },
          {
            "player_name": "Suraj Pal",
            "batting_position": 3,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 57,
            "balls_faced": 50,
            "minutes": 77,
            "fours": 7,
            "sixes": 1,
            "strike_rate": 114
          },
          {
            "player_name": "Mani Polasu",
            "batting_position": 4,
            "dismissal": "c",
            "dismissal_details": "†JD b Harry Shergill",
            "runs": 0,
            "balls_faced": 1,
            "minutes": 1,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          },
          {
            "player_name": "Bhargav",
            "batting_position": 5,
            "dismissal": "b",
            "dismissal_details": "Harry Shergill",
            "runs": 10,
            "balls_faced": 9,
            "minutes": 7,
            "fours": 1,
            "sixes": 1,
            "strike_rate": 111.11
          },
          {
            "player_name": "Purushotham Reddy",
            "batting_position": 6,
            "dismissal": "run out",
            "dismissal_details": "Deepak Mishra / † JD",
            "runs": 13,
            "balls_faced": 20,
            "minutes": 24,
            "fours": 1,
            "sixes": 0,
            "strike_rate": 65
          },
          {
            "player_name": "Vamsee Chaganti",
            "batting_position": 7,
            "dismissal": "b",
            "dismissal_details": "Tagore",
            "runs": 22,
            "balls_faced": 21,
            "minutes": 21,
            "fours": 3,
            "sixes": 0,
            "strike_rate": 104.76
          },
          {
            "player_name": "Avinash Nagubadi",
            "batting_position": 8,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 19,
            "balls_faced": 11,
            "minutes": 9,
            "fours": 1,
            "sixes": 2,
            "strike_rate": 172.73
          }
        ],
        "bowling": [
          {
            "player_name": "Sai",
            "overs": "4",
            "maidens": 1,
            "runs_conceded": 21,
            "wickets": 1,
            "dot_balls": 14,
            "fours_conceded": 3,
            "sixes_conceded": 0,
            "wides": 2,
            "no_balls": 0,
            "economy": 5.25
          },
          {
            "player_name": "Harry Shergill",
            "overs": "4",
            "maidens": 0,
            "runs_conceded": 21,
            "wickets": 3,
            "dot_balls": 16,
            "fours_conceded": 2,
            "sixes_conceded": 1,
            "wides": 1,
            "no_balls": 0,
            "economy": 5.25
          },
          {
            "player_name": "SRI",
            "overs": "4",
            "maidens": 0,
            "runs_conceded": 44,
            "wickets": 0,
            "dot_balls": 13,
            "fours_conceded": 6,
            "sixes_conceded": 2,
            "wides": 4,
            "no_balls": 0,
            "economy": 11
          },
          {
            "player_name": "Shebbu 27",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 25,
            "wickets": 0,
            "dot_balls": 5,
            "fours_conceded": 2,
            "sixes_conceded": 0,
            "wides": 4,
            "no_balls": 0,
            "economy": 8.33
          },
          {
            "player_name": "Tagore",
            "overs": "4",
            "maidens": 0,
            "runs_conceded": 24,
            "wickets": 1,
            "dot_balls": 9,
            "fours_conceded": 1,
            "sixes_conceded": 1,
            "wides": 0,
            "no_balls": 0,
            "economy": 6
          },
          {
            "player_name": "Sandeep Reddy",
            "overs": "1",
            "maidens": 0,
            "runs_conceded": 6,
            "wickets": 0,
            "dot_balls": 1,
            "fours_conceded": 0,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 6
          }
        ],
        "fall_of_wickets": [
          {
            "score": 4,
            "wicket_number": 1,
            "player_name": "TiRtha2051",
            "over": "0.4"
          },
          {
            "score": 11,
            "wicket_number": 2,
            "player_name": "Ramesh Babu",
            "over": "3.1"
          },
          {
            "score": 11,
            "wicket_number": 3,
            "player_name": "Mani Polasu",
            "over": "3.2"
          },
          {
            "score": 29,
            "wicket_number": 4,
            "player_name": "Bhargav",
            "over": "5.4"
          },
          {
            "score": 67,
            "wicket_number": 5,
            "player_name": "Purushotham Reddy",
            "over": "11.4"
          },
          {
            "score": 110,
            "wicket_number": 6,
            "player_name": "Vamsee Chaganti",
            "over": "17.1"
          }
        ]
      },
      {
        "batting_team": "Red Wings",
        "bowling_team": "BELIEVERS",
        "overs": "19.0",
        "runs": 149,
        "wickets": 9,
        "innings_number": 1,
        "innings_type": "regular",
        "super_over_number": None,
        "batting": [
          {
            "player_name": "Abhi",
            "batting_position": 1,
            "dismissal": "c",
            "dismissal_details": "RJ Makkena b Avinash Nagubadi",
            "runs": 0,
            "balls_faced": 2,
            "minutes": 1,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          },
          {
            "player_name": "Deepak Mishra",
            "batting_position": 2,
            "dismissal": "c",
            "dismissal_details": "Purushotham Reddy b RITHVIK PULUGURTHA",
            "runs": 0,
            "balls_faced": 1,
            "minutes": 6,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          },
          {
            "player_name": "Amarnath Mishra",
            "batting_position": 3,
            "dismissal": "c",
            "dismissal_details": "Purushotham Reddy b Siva Kareti",
            "runs": 13,
            "balls_faced": 13,
            "minutes": 16,
            "fours": 3,
            "sixes": 0,
            "strike_rate": 100
          },
          {
            "player_name": "JD",
            "batting_position": 4,
            "dismissal": "c",
            "dismissal_details": "RITHVIK PULUGURTHA b Vamsi 3535",
            "runs": 24,
            "balls_faced": 19,
            "minutes": 33,
            "fours": 3,
            "sixes": 2,
            "strike_rate": 126.32
          },
          {
            "player_name": "Sandeep Reddy",
            "batting_position": 5,
            "dismissal": "c",
            "dismissal_details": "†Suraj Pal b Bhargav",
            "runs": 44,
            "balls_faced": 22,
            "minutes": 37,
            "fours": 7,
            "sixes": 0,
            "strike_rate": 200
          },
          {
            "player_name": "Rahul Abraham N",
            "batting_position": 6,
            "dismissal": "c",
            "dismissal_details": "TiRtha2051 b Purushotham Reddy",
            "runs": 22,
            "balls_faced": 25,
            "minutes": 37,
            "fours": 1,
            "sixes": 1,
            "strike_rate": 88
          },
          {
            "player_name": "Rakesh",
            "batting_position": 7,
            "dismissal": "c",
            "dismissal_details": "†Suraj Pal b Purushotham Reddy",
            "runs": 6,
            "balls_faced": 9,
            "minutes": 10,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 66.67
          },
          {
            "player_name": "Harry Shergill",
            "batting_position": 8,
            "dismissal": "run out",
            "dismissal_details": "RITHVIK PULUGURTHA",
            "runs": 19,
            "balls_faced": 18,
            "minutes": 21,
            "fours": 2,
            "sixes": 0,
            "strike_rate": 105.56
          },
          {
            "player_name": "Tagore",
            "batting_position": 9,
            "dismissal": "run out",
            "dismissal_details": "Bhargav",
            "runs": 5,
            "balls_faced": 5,
            "minutes": 9,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 100
          },
          {
            "player_name": "Sai",
            "batting_position": 10,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 0,
            "balls_faced": 0,
            "minutes": 1,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          },
          {
            "player_name": "Shebbu 27",
            "batting_position": 11,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 0,
            "balls_faced": 0,
            "minutes": 0,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          }
        ],
        "bowling": [
          {
            "player_name": "Avinash Nagubadi",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 13,
            "wickets": 1,
            "dot_balls": 12,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 3,
            "no_balls": 0,
            "economy": 4.33
          },
          {
            "player_name": "RITHVIK PULUGURTHA",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 21,
            "wickets": 1,
            "dot_balls": 11,
            "fours_conceded": 3,
            "sixes_conceded": 1,
            "wides": 0,
            "no_balls": 0,
            "economy": 7
          },
          {
            "player_name": "Siva Kareti",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 30,
            "wickets": 1,
            "dot_balls": 5,
            "fours_conceded": 6,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 15
          },
          {
            "player_name": "Vamsee Chaganti",
            "overs": "1",
            "maidens": 0,
            "runs_conceded": 9,
            "wickets": 0,
            "dot_balls": 3,
            "fours_conceded": 0,
            "sixes_conceded": 1,
            "wides": 0,
            "no_balls": 0,
            "economy": 9
          },
          {
            "player_name": "RJ Makkena",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 18,
            "wickets": 0,
            "dot_balls": 4,
            "fours_conceded": 1,
            "sixes_conceded": 1,
            "wides": 0,
            "no_balls": 0,
            "economy": 9
          },
          {
            "player_name": "Vamsi 3535",
            "overs": "1",
            "maidens": 0,
            "runs_conceded": 10,
            "wickets": 1,
            "dot_balls": 2,
            "fours_conceded": 2,
            "sixes_conceded": 0,
            "wides": 0,
            "no_balls": 0,
            "economy": 10
          },
          {
            "player_name": "Bhargav",
            "overs": "4",
            "maidens": 0,
            "runs_conceded": 20,
            "wickets": 1,
            "dot_balls": 9,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 5
          },
          {
            "player_name": "Purushotham Reddy",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 18,
            "wickets": 2,
            "dot_balls": 8,
            "fours_conceded": 2,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 6
          }
        ],
        "fall_of_wickets": [
          {
            "score": 0,
            "wicket_number": 1,
            "player_name": "Abhi",
            "over": "0.2"
          },
          {
            "score": 5,
            "wicket_number": 2,
            "player_name": "Deepak Mishra",
            "over": "1.1"
          },
          {
            "score": 29,
            "wicket_number": 3,
            "player_name": "Amarnath Mishra",
            "over": "3.4"
          },
          {
            "score": 84,
            "wicket_number": 4,
            "player_name": "JD",
            "over": "8.3"
          },
          {
            "score": 99,
            "wicket_number": 5,
            "player_name": "Sandeep Reddy",
            "over": "11.1"
          },
          {
            "score": 117,
            "wicket_number": 6,
            "player_name": "Rakesh",
            "over": "14.1"
          },
          {
            "score": 134,
            "wicket_number": 7,
            "player_name": "Rahul Abraham N",
            "over": "16.4"
          },
          {
            "score": 149,
            "wicket_number": 8,
            "player_name": "Tagore",
            "over": "18.5"
          },
          {
            "score": 149,
            "wicket_number": 9,
            "player_name": "Harry Shergill",
            "over": "19"
          }
        ]
      },
      {
        "batting_team": "Red Wings",
        "bowling_team": "BELIEVERS",
        "overs": "1.0",
        "runs": 11,
        "wickets": 0,
        "innings_number": 2,
        "innings_type": "super_over",
        "super_over_number": 1,
        "batting": [
          {
            "player_name": "Jd",
            "batting_position": 1,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 9,
            "balls_faced": 5,
            "minutes": 0,
            "fours": 1,
            "sixes": 0,
            "strike_rate": 180
          },
          {
            "player_name": "Abhi",
            "batting_position": 2,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 2,
            "balls_faced": 1,
            "minutes": 0,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 200
          }
        ],
        "bowling": [
          {
            "player_name": "Rithvik Pulugurtha",
            "overs": "1.0",
            "maidens": 0,
            "runs_conceded": 11,
            "wickets": 0,
            "dot_balls": 0,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 0,
            "no_balls": 0,
            "economy": 11
          }
        ],
        "fall_of_wickets": []
      },
      {
        "batting_team": "BELIEVERS",
        "bowling_team": "Red Wings",
        "overs": "1.0",
        "runs": 7,
        "wickets": 0,
        "innings_number": 2,
        "innings_type": "super_over",
        "super_over_number": 1,
        "batting": [
          {
            "player_name": "Avinash Nagubadi",
            "batting_position": 1,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 5,
            "balls_faced": 3,
            "minutes": 0,
            "fours": 1,
            "sixes": 0,
            "strike_rate": 166.67
          },
          {
            "player_name": "Bhargav",
            "batting_position": 2,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 2,
            "balls_faced": 3,
            "minutes": 0,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 66.67
          }
        ],
        "bowling": [
          {
            "player_name": "Sai",
            "overs": "1.0",
            "maidens": 0,
            "runs_conceded": 7,
            "wickets": 0,
            "dot_balls": 0,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 0,
            "no_balls": 0,
            "economy": 7
          }
        ],
        "fall_of_wickets": []
      }
    ]

innings = [
    Innings(**inning)
    for inning in innings
]

# query = BattingQuery(
#     metric=BattingMetric.FOURS,
#     rank=1,
#     innings_scope="super_over"
# )
question = "most runs with out fours and sixers"

result = answer_batting_query(innings, "Red Wings", question)

for player in result:
    print(player.player_name, player.value)