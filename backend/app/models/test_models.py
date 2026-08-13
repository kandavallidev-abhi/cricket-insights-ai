from datetime import datetime, timezone

from .match import Match, MatchPlayer, Innings, BattingPerformance, BowlingPerformance, FallOfWicket

players = [
    MatchPlayer(
        player_name= "Abhi",
        is_captain= True
    ),
    MatchPlayer(
        player_name= "Naveen Kumar",
        is_wicketkeeper= True
    )
]

batting_performance = BattingPerformance(
    player_name= "Sandeep Mulpuri",
    batting_position= 3,
    dismissal= "caught",
    dismissal_details="c Hashmat b WASEEM YOUSUF",
    runs=59,
    balls_faced=53,
    minutes=79,
    fours=5,
    sixes=1,
    strike_rate=111.32
)

rakesh_bowling = BowlingPerformance(
    player_name="Rakesh",
    overs="1",
    maidens=0,
    runs_conceded=3,
    wickets=3,
    dot_balls=3,
    fours_conceded=0,
    sixes_conceded=0,
    wides=0,
    no_balls=0,
    economy=3.00,
)

fall_of_wickets = [
    FallOfWicket(
        score=15,
        wicket_number=1,
        player_name="JD",
        over="1.4",
    ),
    FallOfWicket(
        score=16,
        wicket_number=2,
        player_name="Abhi",
        over="2",
    ),
    FallOfWicket(
        score=19,
        wicket_number=3,
        player_name="Naveen Kumar",
        over="2.3",
    ),
    FallOfWicket(
        score=19,
        wicket_number=4,
        player_name="SRI",
        over="2.5",
    ),
    FallOfWicket(
        score=36,
        wicket_number=5,
        player_name="Rakesh",
        over="5.2",
    ),
    FallOfWicket(
        score=47,
        wicket_number=6,
        player_name="Rahul Abraham N",
        over="8.4",
    ),
    FallOfWicket(
        score=95,
        wicket_number=7,
        player_name="Sudheer Reddy",
        over="15.4",
    ),
    FallOfWicket(
        score=127,
        wicket_number=8,
        player_name="Sai",
        over="19.1",
    ),
    FallOfWicket(
        score=132,
        wicket_number=9,
        player_name="Sandeep Mulpuri",
        over="20",
    ),
]

innings = Innings(
    batting_team= "Red Wings",
    bowling_team= "The Trailblazers",
    overs="20.0",
    runs=132,
    wickets=9,
    batting= [batting_performance],
    bowling= [rakesh_bowling],
    fall_of_wickets=fall_of_wickets
)
match = Match(
    tournament_name="SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS",
    stage="Silver Final",
    match_date=datetime(
        2026,
        8,
        2,
        9,
        24,
        tzinfo=timezone.utc,
    ),
    ground="SS Cricket Ground",
    team_name="Red Wings",
    opponent_name="The Trailblazers",
    toss_winner="Red Wings",
    toss_decision="bat",
    batting_first="Red Wings",
    match_overs=20,
    team_runs=132,
    team_wickets=9,
    opponent_runs=100,
    opponent_wickets=10,
    result="Red Wings won by 32 runs",
    captain="Abhi",
    wicketkeeper="Naveen Kumar",
    players= players,
    innings= [innings]
)

print(match)

# ====== print all four pages ====
# ========== PAGE 1 ==========
# 0 '\xa0'
# 1 'SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS'
# 2 '(Silver Final)'
# 3 '8/4/26, 3:55 AM cricheroes.com 1 of 4'
# 4 'Match Details'
# 5 'Match Red Wings vs'
# 6 'The Trailblazers'
# 7 'Ground S2 Sports Infinity Cricket Arena,'
# 8 'Hyderabad (Telangana)'
# 9 'Date 2026-08-02, 09:24 AM UTC'
# 10 'Match Result'
# 11 'Toss Red Wings opt to bat'
# 12 'Total Red Wings 132/9 (20.0 Ov)'
# 13 'The Trailblazers 100/10 (20.0 Ov)'
# 14 'Result Red Wings won by 32 runs'
# 15 'Best Performances - Batsmen'
# 16 'Players Name R B 4s 6s SR'
# 17 'Sandeep Mulpuri 59 53 5 1 111.32'
# 18 'Sk 54 55 3 2 98.18'
# 19 'Sai 24 16 3 1 150.00'
# 20 'Best Performances - Bowlers'
# 21 'Players Name O M R W Eco'
# 22 'Rakesh 1.0 0 3 3 3.00'
# 23 'Aamir Raina 4.0 0 15 3 3.75'
# 24 'Sai 4.0 0 17 3 4.25'
# 25 'Match Officials'
# 26 'No Name Role Signature'
# 27 '1 Shawariq Scorer'
# 28 '2 Abhi (Red Wings) Captain'
# 29 '3 Amit Sharma (The Trailblazers) Captain'

# ========== PAGE 2 ==========
# 0 '\xa0'
# 1 'SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS'
# 2 '(Silver Final)'
# 3 '8/4/26, 3:55 AM cricheroes.com 2 of 4'
# 4 'Playing Squad'
# 5 'Red Wings'
# 6 ' The Trailblazers'
# 7 '1'
# 8 ' Abhi ( C )'
# 9 ' Amit Sharma ( C )'
# 10 '2'
# 11 ' Naveen Kumar ( WK )'
# 12 ' Waseem Yousuf'
# 13 '3'
# 14 ' Ravi'
# 15 ' Aamir Raina'
# 16 '4'
# 17 ' Sandeep Mulpuri'
# 18 ' Aman Vashist'
# 19 '5'
# 20 ' Tagore'
# 21 ' Hashmat'
# 22 '6'
# 23 ' Jd'
# 24 ' G Vijay Kumar'
# 25 '7'
# 26 ' Sai'
# 27 ' Shadab Khan'
# 28 '8'
# 29 ' Vinod Reddy'
# 30 ' Sk'
# 31 '9'
# 32 ' Rakesh'
# 33 ' Abhishek Nahire'
# 34 '10'
# 35 ' Sri'
# 36 ' Rakesh Saini'
# 37 '11'
# 38 ' Sudheer Reddy'
# 39 ' Aravind Kumar'
# 40 '12'
# 41 ' Rahul Abraham N'
# 42 ' Prasanna R Gachinmani'

# ========== PAGE 3 ==========
# 0 '\xa0'
# 1 'SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS'
# 2 '(Silver Final)'
# 3 '8/4/26, 3:55 AM cricheroes.com 3 of 4'
# 4 'Red Wings 132/9 (20.0 Ov) (1st Innings) Abhi (Red Wings)'
# 5 'No Batsman Status R B M 4s 6s SR'
# 6 '1 Abhi (c) (RHB) lbw b Aamir Raina 2 4 10 0 0 50.00'
# 7 '2 JD (RHB) b Aamir Raina 11 8 8 2 0 137.50'
# 8 '3 Sandeep Mulpuri (RHB) c Hashmat b WASEEM YOUSUF 59 53 79 5 1 111.32'
# 9 '4 Naveen Kumar (wk) (RHB) b Rakesh Saini 0 1 4 0 0 0.00'
# 10 '5 SRI (RHB) b Rakesh Saini 0 2 1 0 0 0.00'
# 11 '6 Rakesh (RHB) c Shadab Khan b Aamir Raina 1 6 10 0 0 16.67'
# 12 '7 Rahul Abraham N (RHB) c amit sharma b G vijay kumar 1 11 12 0 0 9.09'
# 13 '8 Sudheer Reddy (RHB) c Rakesh Saini b Prasanna R Gachinmani18 18 26 1 0 100.00'
# 14 '9 Sai (RHB) c †SK b WASEEM YOUSUF 24 16 12 3 1 150.00'
# 15 '10 Ravi (RHB) not out 2 2 2 0 0 100.00'
# 16 'Extras: (nb 1, b 3, lb 4, wd 6) 14'
# 17 'Total: Overs 20.0, Wickets 9 132 (CRR: 6.60)'
# 18 'To Bat: Vinod Reddy, Tagore'
# 19 'Fall of Wickets'
# 20 '15-1 (JD, 1.4 ov), 16-2 (Abhi, 2 ov), 19-3 (Naveen Kumar, 2.3 ov), 19-4 (SRI, 2.5 ov), 36-5 (Rakesh, 5.2 ov), 47-6 (Rahul Abraham N, 8.4 ov), 95-7 (Sudheer Reddy,'
# 21 '15.4 ov), 127-8 (Sai, 19.1 ov), 132-9 (Sandeep Mulpuri, 20 ov)'
# 22 'No Bowler O M R W 0s 4s 6s WD NB Eco'
# 23 '1 G vijay kumar 3 0 23 1 6 3 0 0 0 7.67'
# 24 '2 Rakesh Saini 4 1 25 2 17 4 0 2 1 6.25'
# 25 '3 Aamir Raina 4 0 15 3 13 1 0 0 0 3.75'
# 26 '4 amit sharma (c) 3 0 22 0 9 2 1 2 0 7.33'
# 27 '5 Prasanna R Gachinmani 4 0 27 1 4 1 0 1 0 6.75'
# 28 '6 Abhishek Nahire 1 0 8 0 3 0 1 0 0 8.00'
# 29 '7 WASEEM YOUSUF 1 0 5 2 2 0 0 0 0 5.00'

# ========== PAGE 4 ==========
# 0 '\xa0'
# 1 'SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS'
# 2 '(Silver Final)'
# 3 '8/4/26, 3:55 AM cricheroes.com 4 of 4'
# 4 'The Trailblazers 100/10 (20.0 Ov) (1st Innings) Amit Sharma (The Trailblazers)'
# 5 'No Batsman Status R B M 4s 6s SR'
# 6 '1 Shadab Khan (RHB) c Abhi b SRI 7 15 30 0 0 46.67'
# 7 '2 WASEEM YOUSUF (RHB) c Sudheer Reddy b Tagore 3 7 7 0 0 42.86'
# 8 '3 SK (LHB) c Rahul Abraham N b Rakesh 54 55 86 3 2 98.18'
# 9 '4 Aman Vashist (RHB) b Sai 0 3 6 0 0 0.00'
# 10 '5 Aravind Kumar (RHB) lbw b Sai 0 1 1 0 0 0.00'
# 11 '6 Aamir Raina (RHB) c SRI b Vinod Reddy 1 3 3 0 0 33.33'
# 12 '7 Hashmat (RHB) b Sai 0 1 1 0 0 0.00'
# 13 '8 Prasanna R Gachinmani (RHB) b Sudheer Reddy 18 22 31 2 0 81.82'
# 14 '9 G vijay kumar (LHB) c Rahul Abraham N b Rakesh 5 11 15 0 0 45.45'
# 15 '10 Abhishek Nahire (RHB) not out 1 1 3 0 0 100.00'
# 16 '11 Rakesh Saini (RHB) st †Naveen Kumar b Rakesh 0 1 1 0 0 0.00'
# 17 'Extras: (wd 9, lb 2) 11'
# 18 'Total: Overs 20.0, Wickets 10 100 (CRR: 5.00)'
# 19 'To Bat: Amit Sharma (c)'
# 20 'Fall of Wickets'
# 21 '5-1 (WASEEM YOUSUF, 2.2 ov), 29-2 (Shadab Khan, 7.4 ov), 34-3 (Aman Vashist, 8.5 ov), 34-4 (Aravind Kumar, 9 ov), 37-5 (Aamir Raina, 10 ov), 38-6 (Hashmat,'
# 22 '10.2 ov), 88-7 (Prasanna R Gachinmani, 16.4 ov), 99-8 (SK, 19.3 ov), 100-9 (G vijay kumar, 19.5 ov), 100-10 (Rakesh Saini, 20 ov)'
# 23 'No Bowler O M R W 0s 4s 6s WD NB Eco'
# 24 '1 Tagore 4 0 15 1 14 0 1 0 0 3.75'
# 25 '2 SRI 4 0 14 1 11 0 0 0 0 3.50'
# 26 '3 Sai 4 0 17 3 14 2 0 1 0 4.25'
# 27 '4 Vinod Reddy 2 0 20 1 4 2 1 1 0 10.00'
# 28 '5 Ravi 3 0 14 0 7 1 0 0 0 4.67'
# 29 '6 Sudheer Reddy 2 0 15 1 5 1 0 3 0 7.50'
# 30 '7 Rakesh 1 0 3 3 3 0 0 0 0 3.00'

# old report
# ========== PAGE 1 ==========
# 0 '\xa0'
# 1 'GENTLEMENS CRICKET LEAGUE (GCL -5) (League Matches)'
# 2 '8/13/26, 5:47 PM cricheroes.com 1 of 4'
# 3 'Match Details'
# 4 'Match ASG Warriors vs'
# 5 'Red Wings'
# 6 'Ground One Champion-3,'
# 7 'Hyderabad (Telangana)'
# 8 'Date 2024-11-09, 09:18 AM UTC'
# 9 'Match Result'
# 10 'Toss ASG Warriors opt to bat'
# 11 'Total ASG Warriors 158/9 (20.0 Ov)'
# 12 'Red Wings 123/8 (14.4 Ov)'
# 13 'Result ASG Warriors won by 35 runs'
# 14 'Best Performances - Batsmen'
# 15 'Players Name R B 4s 6s SR'
# 16 'Harry 50 25 7 1 200.00'
# 17 'Bhawesh D 44 38 6 0 115.79'
# 18 'Nitish Bhagi 26 14 5 0 185.71'
# 19 'Best Performances - Bowlers'
# 20 'Players Name O M R W Eco'
# 21 'Sri 4.0 0 30 3 7.50'
# 22 'Pradeep Sathbhai 2.0 0 11 2 5.50'
# 23 'Bhavesh Lakhani 3.0 0 21 2 7.00'
# 24 'Match Officials'
# 25 'No Name Role Signature'
# 26 '1 Vijay Kumar Yadav Umpire'
# 27 '2 SUNDEEP YANAMALA Scorer'
# 28 '3 Vijay Kumar Yadav Scorer'
# 29 '4 Anshul Bhargava (ASG Warriors) Captain'
# 30 '5 Abhi (Red Wings) Captain'

# ========== PAGE 2 ==========
# 0 '\xa0'
# 1 'GENTLEMENS CRICKET LEAGUE (GCL -5) (League Matches)'
# 2 '8/13/26, 5:47 PM cricheroes.com 2 of 4'
# 3 'Playing Squad'
# 4 'ASG Warriors'
# 5 ' Red Wings'
# 6 '1'
# 7 ' Anshul Bhargava ( C )'
# 8 ' Abhi ( C )'
# 9 '2'
# 10 ' Asif'
# 11 ' Tagore'
# 12 '3'
# 13 ' Bhawesh D'
# 14 ' Jd'
# 15 '4'
# 16 ' Nitish Bhagi'
# 17 ' Mahesh Pasupuleti'
# 18 '5'
# 19 ' Pradeep Sathbhai'
# 20 ' Sudheer Reddy ( WK )'
# 21 '6'
# 22 ' Prashanth Vallur'
# 23 ' Harry'
# 24 '7'
# 25 ' Anil Jeph'
# 26 ' Sandeep Reddy ( WK )'
# 27 '8'
# 28 ' Praveen Sathbhai'
# 29 ' Ravi'
# 30 '9'
# 31 ' Vidhya Sagar'
# 32 ' Sri'

# ========== PAGE 3 ==========
# 0 '\xa0'
# 1 'GENTLEMENS CRICKET LEAGUE (GCL -5) (League Matches)'
# 2 '8/13/26, 5:47 PM cricheroes.com 3 of 4'
# 3 'ASG Warriors 158/9 (20.0 Ov) (1st Innings) Anshul Bhargava (ASG Warriors)'
# 4 'No Batsman Status R B M 4s 6s SR'
# 5 '1 Anil Jeph (LHB) lbw b SRI 4 4 4 1 0 100.00'
# 6 '2 Prashanth Vallur (RHB) c Ravi b SRI 0 4 14 0 0 0.00'
# 7 '3 Vidhya Sagar (RHB) c Tagore b Ravi 5 3 2 1 0 166.67'
# 8 '4 Sumith Kumar (LHB) b Harry Shergill 25 24 25 5 0 104.17'
# 9 '5 Bhawesh D (LHB) not out 44 38 75 6 0 115.79'
# 10 '6 Praveen Sathbhai (RHB) lbw b Harry Shergill 2 2 1 0 0 100.00'
# 11 '7 Asif (RHB) c Abhi b JD 13 12 17 2 0 108.33'
# 12 '8 Nitish Bhagi (RHB) c †Sudheer Reddy b Tagore 26 14 14 5 0 185.71'
# 13 '9 Aashish Bansal (RHB) c Mahesh Pasupuleti b Tagore 0 1 1 0 0 0.00'
# 14 '10 Bhavesh Lakhani (RHB) b SRI 24 18 14 4 0 133.33'
# 15 'Extras: (wd 11, lb 4) 15'
# 16 'Total: Overs 20.0, Wickets 9 158 (CRR: 7.90)'
# 17 'To Bat: Pradeep Sathbhai, Anshul Bhargava (c)'
# 18 'Fall of Wickets'
# 19 '6-1 (Anil Jeph, 0.4 ov), 12-2 (Vidhya Sagar, 1.2 ov), 13-3 (Prashanth Vallur, 2.3 ov), 53-4 (Sumith Kumar, 8.4 ov), 55-5 (Praveen Sathbhai, 9 ov), 84-6 (Asif, 12.1 ov),'
# 20 '124-7 (Nitish Bhagi, 16.1 ov), 124-8 (Aashish Bansal, 16.2 ov), 158-9 (Bhavesh Lakhani, 20 ov)'
# 21 'No Bowler O M R W 0s 4s 6s WD NB Eco'
# 22 '1 SRI 4 0 30 3 13 4 0 4 0 7.50'
# 23 '2 Ravi 2 0 9 1 8 1 0 2 0 4.50'
# 24 '3 Tagore 4 0 32 2 14 6 0 2 0 8.00'
# 25 '4 Mahesh Pasupuleti 4 0 31 0 10 5 0 0 0 7.75'
# 26 '5 Harry Shergill 3 0 32 2 6 6 0 1 0 10.67'
# 27 '6 Sandeep Reddy 2 0 16 0 4 2 0 0 0 8.00'
# 28 '7 JD 1 0 4 1 2 0 0 0 0 4.00'

# ========== PAGE 4 ==========
# 0 '\xa0'
# 1 'GENTLEMENS CRICKET LEAGUE (GCL -5) (League Matches)'
# 2 '8/13/26, 5:47 PM cricheroes.com 4 of 4'
# 3 'Red Wings 123/8 (14.4 Ov) (1st Innings) Abhi (Red Wings)'
# 4 'No Batsman Status R B M 4s 6s SR'
# 5 '1 JD (RHB) b Anil Jeph 1 3 3 0 0 33.33'
# 6 '2 Harry Shergill (RHB) c Bhavesh Lakhani b Vidhya Sagar 50 25 38 7 1 200.00'
# 7 '3 Sudheer Reddy (wk) (RHB) c Nitish Bhagi b Bhavesh Lakhani 9 22 64 1 0 40.91'
# 8 '4 Mahesh Pasupuleti (RHB) c Vidhya Sagar b Bhavesh Lakhani 2 6 6 0 0 33.33'
# 9 '5 SRI (RHB) run out Vidhya Sagar 12 6 7 2 0 200.00'
# 10 '6 Abhi (c) (RHB) c Sumith Kumar b Pradeep Sathbhai 12 7 8 2 0 171.43'
# 11 '7 Sandeep Reddy (wk) (RHB) not out 5 5 15 1 0 100.00'
# 12 '8 Tagore (LHB) b Pradeep Sathbhai 5 6 3 1 0 83.33'
# 13 '9 Ravi (RHB) c Nitish Bhagi b Aashish Bansal 8 8 6 0 1 100.00'
# 14 'Extras: (wd 18, b 1) 19'
# 15 'Total: Overs 14.4, Wickets 8 123 (CRR: 8.39)'
# 16 'To Bat:'
# 17 'Fall of Wickets'
# 18 '3-1 (JD, 0.3 ov), 66-2 (Harry Shergill, 7.2 ov), 74-3 (Mahesh Pasupuleti, 8.5 ov), 91-4 (SRI, 9.5 ov), 105-5 (Abhi, 11.2 ov), 109-6 (Sudheer Reddy, 12.1 ov), 114-7'
# 19 '(Tagore, 13.1 ov), 123-8 (Ravi, 14.4 ov)'
# 20 'No Bowler O M R W 0s 4s 6s WD NB Eco'
# 21 '1 Anil Jeph 2 0 14 1 6 2 0 1 0 7.00'
# 22 '2 Praveen Sathbhai 2 0 11 0 7 1 0 3 0 5.50'
# 23 '3 Sumith Kumar 2 0 27 0 3 3 1 1 0 13.50'
# 24 '4 Aashish Bansal 1.4 0 18 1 5 2 1 1 0 10.80'
# 25 '5 Vidhya Sagar 2 0 20 1 6 2 0 4 0 10.00'
# 26 '6 Bhavesh Lakhani 3 0 21 2 9 3 0 1 0 7.00'
# 27 '7 Pradeep Sathbhai 2 0 11 2 7 2 0 0 0 5.50'