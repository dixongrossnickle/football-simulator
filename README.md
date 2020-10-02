# Football Simulator
The football simulator uses [pandas](https://pypi.org/project/pandas/) to read two CSV's: one containing every match from Europe's top 5 leagues (2019-20 season), and another containing the all players' ratings from the FIFA 20 video game. It finds the mean and standard deviation of each team's goals for & goals conceded, depending on home or away matches. Then, it creates Gaussian distributions for each, and averages the two to determine the goals scored by each team.<br/><br/>

Pseudo-code:<br/>

```
goals_scored_in_match = [ random(avg_goals_scored) + random(avg_goals_conceded) ] / 2
```
<br/>

Then, a player is randomly selected for each event using the weights of each player's relevant attribute (`finishing` for goals and `aggression` for red cards).<br/><br/><br/>

## Simulator API
The simulator can be used via a web API — Just replace `HomeTeamID` and `AwayTeamID` with the corresponding team ID's. ID–name pairs can be found [below](#api-variables).<br/><br/>

### Request format:
<br/>

```
https://dixongrossnickle.com/sim/run/?home=<HomeTeamID>&away=<AwayTeamID>
```

#### Example: ####
`https://dixongrossnickle.com/sim/run/?home=G12&away=E116`<br/><br/>

### Response format:
<br/>

```
{
    result: {
        result: 'home win',
        homeTeamGoals: 2,
        awayTeamGoals: 1
    },
    homeTeam: {
        name: 'Bayern',
        startingXI: {
            1: {
                name: 'R. Lewandowski',
                clubName: 'Bayern',
                position: 'ST',
                nationality: 'Poland',
                overall: 89,
                finishing: 88,
                aggression: 81
            },
            [2–11]: { ...
            }
        }
    },
    awayTeam: {
        name: 'Tottenham',
        startingXI: {
            1: {
                name: 'H. Kane',
                clubName: 'Tottenham',
                position: 'ST',
                nationality: 'England',
                overall: 89,
                finishing: 94,
                aggression: 78
            },
            [2–11]: { ...
            }
        }
    },
    matchEvents: {
        82: {
            event: 'goal',
            team: 'Bayern',
            player: 'K. Coman'
        },
        42: {
            event: 'goal',
            team: 'Bayern',
            player: 'A. Davies'
        },
        16: {
            event: 'goal',
            team: 'Tottenham',
            player: 'T. Ndombele'
        },
        68: {
            event: 'red card',
            team: 'Tottenham',
            player: 'T. Ndombele'
        }
    }
}
```
<br/>

Note: events may be returned in any order.<br/><br/><br/>

# API variables
### ID: Team Name
<br/>

### England
`E10`: Arsenal <br/>
`E11`: Aston Villa <br/>
`E12`: Bournemouth <br/>
`E13`: Brighton <br/>
`E14`: Burnley <br/>
`E15`: Chelsea <br/>
`E16`: Crystal Palace <br/>
`E17`: Everton <br/>
`E18`: Leicester <br/>
`E19`: Liverpool <br/>
`E110`: Manchester City <br/>
`E111`: Manchester United <br/>
`E112`: Newcastle <br/>
`E113`: Norwich <br/>
`E114`: Sheffield United <br/>
`E115`: Southampton <br/>
`E116`: Tottenham <br/>
`E117`: Watford <br/>
`E118`: West Ham <br/>
`E119`: Wolves <br/>

### Germany
`G10`: Augsburg <br/>
`G11`: Leverkusen <br/>
`G12`: Bayern <br/>
`G13`: Dortmund <br/>
`G14`: Borussia M'gladbach <br/>
`G15`: Frankfurt <br/>
`G16`: Köln <br/>
`G17`: Düsseldorf <br/>
`G18`: Freiburg <br/>
`G19`: Hertha <br/>
`G110`: Hoffenheim <br/>
`G111`: Mainz <br/>
`G112`: Paderborn <br/>
`G113`: Leipzig <br/>
`G114`: Schalke <br/>
`G115`: Union Berlin <br/>
`G116`: Werder Bremen <br/>
`G117`: Wolfsburg <br/>

### Italy
`I10`: AC Milan <br/>
`I11`: Atalanta <br/>
`I12`: Bologna <br/>
`I13`: Brescia <br/>
`I14`: Cagliari <br/>
`I15`: Fiorentina <br/>
`I16`: Genoa <br/>
`I17`: Verona <br/>
`I18`: Inter Milan <br/>
`I19`: Juventus <br/>
`I110`: Lazio <br/>
`I111`: Lecce <br/>
`I112`: Napoli <br/>
`I113`: Parma <br/>
`I114`: Roma <br/>
`I115`: SPAL <br/>
`I116`: Sampdoria <br/>
`I117`: Sassuolo <br/>
`I118`: Torino <br/>
`I119`: Udinese <br/>

### Spain
`S10`: Alavés <br/>
`S11`: Athletic Club <br/>
`S12`: Atlético Madrid <br/>
`S13`: Barcelona <br/>
`S14`: Celta Vigo <br/>
`S15`: Eibar <br/>
`S16`: Espanyol <br/>
`S17`: Getafe <br/>
`S18`: Granada <br/>
`S19`: Leganés <br/>
`S110`: Levante <br/>
`S111`: Mallorca <br/>
`S112`: Osasuna <br/>
`S113`: Real Betis <br/>
`S114`: Real Madrid <br/>
`S115`: Real Sociedad <br/>
`S116`: Sevilla <br/>
`S117`: Valencia <br/>
`S118`: Valladolid <br/>
`S119`: Villarreal <br/>

### France
`F10`: Amiens <br/>
`F11`: Angers <br/>
`F12`: Bordeaux <br/>
`F13`: Brest <br/>
`F14`: Dijon <br/>
`F15`: Lille <br/>
`F16`: Lyon <br/>
`F17`: Marseille <br/>
`F18`: Metz <br/>
`F19`: Monaco <br/>
`F110`: Montpellier <br/>
`F111`: Nantes <br/>
`F112`: Nice <br/>
`F113`: Nîmes <br/>
`F114`: PSG <br/>
`F115`: Reims <br/>
`F116`: Rennes <br/>
`F117`: Saint-Étienne <br/>
`F118`: Strasbourg <br/>
`F119`: Toulouse <br/>
