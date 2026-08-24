from app.models.analytic import BattingMetric, BattingQuery
from app.services.analytics.batting_analytics import get_batting_ranking
from app.models.match import Innings

# Use an actual parsed innings here
innings = [
      {
        "batting_team": "MYTRI Heros",
        "bowling_team": "Red Wings",
        "overs": "18.5",
        "runs": 148,
        "wickets": 10,
        "batting": [
          {
            "player_name": "Harsha Molakalapalli",
            "batting_position": 1,
            "dismissal": "b",
            "dismissal_details": "Rakesh",
            "runs": 1,
            "balls_faced": 2,
            "minutes": 6,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 50
          },
          {
            "player_name": "Gnani Krishna",
            "batting_position": 2,
            "dismissal": "lbw",
            "dismissal_details": "b Tagore",
            "runs": 8,
            "balls_faced": 6,
            "minutes": 10,
            "fours": 2,
            "sixes": 0,
            "strike_rate": 133.33
          },
          {
            "player_name": "Dileep Kumar Gosala",
            "batting_position": 3,
            "dismissal": "run out",
            "dismissal_details": "Abhi / Tagore",
            "runs": 5,
            "balls_faced": 9,
            "minutes": 10,
            "fours": 1,
            "sixes": 0,
            "strike_rate": 55.56
          },
          {
            "player_name": "Deepak",
            "batting_position": 4,
            "dismissal": "b",
            "dismissal_details": "Abhi",
            "runs": 39,
            "balls_faced": 30,
            "minutes": 29,
            "fours": 6,
            "sixes": 1,
            "strike_rate": 130
          },
          {
            "player_name": "Vardhan M",
            "batting_position": 5,
            "dismissal": "b",
            "dismissal_details": "Sai",
            "runs": 63,
            "balls_faced": 33,
            "minutes": 65,
            "fours": 7,
            "sixes": 3,
            "strike_rate": 190.91
          },
          {
            "player_name": "Anil",
            "batting_position": 6,
            "dismissal": "c",
            "dismissal_details": "†Naveen Kumar b Sudheer Reddy",
            "runs": 18,
            "balls_faced": 19,
            "minutes": 18,
            "fours": 4,
            "sixes": 0,
            "strike_rate": 94.74
          },
          {
            "player_name": "Rajesh P",
            "batting_position": 7,
            "dismissal": "lbw",
            "dismissal_details": "b Ravi",
            "runs": 3,
            "balls_faced": 5,
            "minutes": 9,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 60
          },
          {
            "player_name": "Nagaraj palacharla",
            "batting_position": 8,
            "dismissal": "c",
            "dismissal_details": "Abhi b Sai",
            "runs": 1,
            "balls_faced": 3,
            "minutes": 3,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 33.33
          },
          {
            "player_name": "Venkat",
            "batting_position": 9,
            "dismissal": "b",
            "dismissal_details": "Sai",
            "runs": 0,
            "balls_faced": 1,
            "minutes": 1,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          },
          {
            "player_name": "Surya Nalluri",
            "batting_position": 10,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 3,
            "balls_faced": 2,
            "minutes": 7,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 150
          },
          {
            "player_name": "Ch Gopi",
            "batting_position": 11,
            "dismissal": "b",
            "dismissal_details": "Sai",
            "runs": 0,
            "balls_faced": 4,
            "minutes": 2,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 0
          }
        ],
        "bowling": [
          {
            "player_name": "Tagore",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 26,
            "wickets": 1,
            "dot_balls": 10,
            "fours_conceded": 4,
            "sixes_conceded": 1,
            "wides": 0,
            "no_balls": 0,
            "economy": 8.67
          },
          {
            "player_name": "Rakesh",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 11,
            "wickets": 1,
            "dot_balls": 8,
            "fours_conceded": 2,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 5.5
          },
          {
            "player_name": "Sai",
            "overs": "3.5",
            "maidens": 0,
            "runs_conceded": 11,
            "wickets": 4,
            "dot_balls": 16,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 0,
            "no_balls": 0,
            "economy": 2.87
          },
          {
            "player_name": "Kasi Vishwanth Reddy",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 24,
            "wickets": 0,
            "dot_balls": 3,
            "fours_conceded": 3,
            "sixes_conceded": 1,
            "wides": 1,
            "no_balls": 0,
            "economy": 12
          },
          {
            "player_name": "Ravi",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 22,
            "wickets": 1,
            "dot_balls": 4,
            "fours_conceded": 4,
            "sixes_conceded": 0,
            "wides": 0,
            "no_balls": 0,
            "economy": 11
          },
          {
            "player_name": "Abhi",
            "overs": "1",
            "maidens": 0,
            "runs_conceded": 17,
            "wickets": 1,
            "dot_balls": 2,
            "fours_conceded": 1,
            "sixes_conceded": 2,
            "wides": 0,
            "no_balls": 0,
            "economy": 17
          },
          {
            "player_name": "JD",
            "overs": "3",
            "maidens": 1,
            "runs_conceded": 16,
            "wickets": 0,
            "dot_balls": 12,
            "fours_conceded": 2,
            "sixes_conceded": 0,
            "wides": 2,
            "no_balls": 1,
            "economy": 5.33
          },
          {
            "player_name": "Sudheer Reddy",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 20,
            "wickets": 1,
            "dot_balls": 3,
            "fours_conceded": 3,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 10
          }
        ],
        "fall_of_wickets": [
          {
            "score": 10,
            "wicket_number": 1,
            "player_name": "Harsha Molakalapalli",
            "over": "1.1"
          },
          {
            "score": 14,
            "wicket_number": 2,
            "player_name": "Gnani Krishna",
            "over": "2.1"
          },
          {
            "score": 22,
            "wicket_number": 3,
            "player_name": "Dileep Kumar Gosala",
            "over": "4.1"
          },
          {
            "score": 76,
            "wicket_number": 4,
            "player_name": "Deepak",
            "over": "9.3"
          },
          {
            "score": 109,
            "wicket_number": 5,
            "player_name": "Anil",
            "over": "13.3"
          },
          {
            "score": 136,
            "wicket_number": 6,
            "player_name": "Rajesh P",
            "over": "15.5"
          },
          {
            "score": 139,
            "wicket_number": 7,
            "player_name": "Nagaraj palacharla",
            "over": "16.4"
          },
          {
            "score": 139,
            "wicket_number": 8,
            "player_name": "Venkat",
            "over": "16.5"
          },
          {
            "score": 148,
            "wicket_number": 9,
            "player_name": "Vardhan M",
            "over": "18.1"
          },
          {
            "score": 148,
            "wicket_number": 10,
            "player_name": "Ch Gopi",
            "over": "18.5"
          }
        ]
      },
      {
        "batting_team": "Red Wings",
        "bowling_team": "MYTRI Heros",
        "overs": "17.3",
        "runs": 149,
        "wickets": 5,
        "batting": [
          {
            "player_name": "Naveen Kumar",
            "batting_position": 1,
            "dismissal": "c",
            "dismissal_details": "Anil b Gnani Krishna",
            "runs": 31,
            "balls_faced": 15,
            "minutes": 22,
            "fours": 4,
            "sixes": 1,
            "strike_rate": 206.67
          },
          {
            "player_name": "Ravi",
            "batting_position": 2,
            "dismissal": "c",
            "dismissal_details": "Anil b Ch Gopi",
            "runs": 7,
            "balls_faced": 10,
            "minutes": 13,
            "fours": 1,
            "sixes": 0,
            "strike_rate": 70
          },
          {
            "player_name": "Rakesh",
            "batting_position": 3,
            "dismissal": "b",
            "dismissal_details": "Gnani Krishna",
            "runs": 48,
            "balls_faced": 44,
            "minutes": 48,
            "fours": 6,
            "sixes": 0,
            "strike_rate": 109.09
          },
          {
            "player_name": "JD",
            "batting_position": 4,
            "dismissal": "c",
            "dismissal_details": "Anil b Ch Gopi",
            "runs": 23,
            "balls_faced": 14,
            "minutes": 23,
            "fours": 3,
            "sixes": 1,
            "strike_rate": 164.29
          },
          {
            "player_name": "Rahul Abraham N",
            "batting_position": 5,
            "dismissal": "run out",
            "dismissal_details": "† Nagaraj palacharla",
            "runs": 1,
            "balls_faced": 1,
            "minutes": 4,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 100
          },
          {
            "player_name": "Tagore",
            "batting_position": 6,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 9,
            "balls_faced": 11,
            "minutes": 21,
            "fours": 0,
            "sixes": 0,
            "strike_rate": 81.82
          },
          {
            "player_name": "Abhi",
            "batting_position": 7,
            "dismissal": "not out",
            "dismissal_details": None,
            "runs": 17,
            "balls_faced": 11,
            "minutes": 10,
            "fours": 2,
            "sixes": 1,
            "strike_rate": 154.55
          }
        ],
        "bowling": [
          {
            "player_name": "Ch Gopi",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 27,
            "wickets": 2,
            "dot_balls": 8,
            "fours_conceded": 5,
            "sixes_conceded": 0,
            "wides": 1,
            "no_balls": 0,
            "economy": 9
          },
          {
            "player_name": "Anil",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 22,
            "wickets": 0,
            "dot_balls": 8,
            "fours_conceded": 1,
            "sixes_conceded": 1,
            "wides": 0,
            "no_balls": 0,
            "economy": 7.33
          },
          {
            "player_name": "Gnani Krishna",
            "overs": "4",
            "maidens": 0,
            "runs_conceded": 47,
            "wickets": 2,
            "dot_balls": 9,
            "fours_conceded": 6,
            "sixes_conceded": 2,
            "wides": 1,
            "no_balls": 1,
            "economy": 11.75
          },
          {
            "player_name": "Surya Nalluri",
            "overs": "2",
            "maidens": 0,
            "runs_conceded": 19,
            "wickets": 0,
            "dot_balls": 4,
            "fours_conceded": 3,
            "sixes_conceded": 0,
            "wides": 2,
            "no_balls": 0,
            "economy": 9.5
          },
          {
            "player_name": "Deepak",
            "overs": "3",
            "maidens": 0,
            "runs_conceded": 16,
            "wickets": 0,
            "dot_balls": 5,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 0,
            "no_balls": 0,
            "economy": 5.33
          },
          {
            "player_name": "Rajesh P",
            "overs": "2.3",
            "maidens": 0,
            "runs_conceded": 16,
            "wickets": 0,
            "dot_balls": 4,
            "fours_conceded": 1,
            "sixes_conceded": 0,
            "wides": 2,
            "no_balls": 0,
            "economy": 6.4
          }
        ],
        "fall_of_wickets": [
          {
            "score": 35,
            "wicket_number": 1,
            "player_name": "Ravi",
            "over": "3.3"
          },
          {
            "score": 60,
            "wicket_number": 2,
            "player_name": "Naveen Kumar",
            "over": "5.4"
          },
          {
            "score": 102,
            "wicket_number": 3,
            "player_name": "JD",
            "over": "11.3"
          },
          {
            "score": 105,
            "wicket_number": 4,
            "player_name": "Rahul Abraham N",
            "over": "12.1"
          },
          {
            "score": 126,
            "wicket_number": 5,
            "player_name": "Rakesh",
            "over": "15"
          }
        ]
      }
    ]

innings = [
    Innings(**inning)
    for inning in innings
]

query = BattingQuery(
    metric=BattingMetric.SIXES,
    rank=1
)

result = get_batting_ranking(innings[1], query)

for player in result:
    print(player.player_name, player.sixes)