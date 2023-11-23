from leeger.league_loader import SleeperLeagueLoader 
from leeger.league_loader import YahooLeagueLoader
from leeger.model.league import League
from leeger.util.excel import leagueToExcel
from dotenv import load_dotenv
import os
#from env import clientID, clientSecret, sleeperLeagueID

if __name__ == "__main__":
    # Sometimes, you may want to combine League objects.
    # This may be because you switched fantasy sites and now the league data is split across different sites.

# First, get League from Yahoo for 2015-2020.
# Get a League object with years 2015 through 2020 for the Yahoo league with the most recent league ID of "264328" or others.
    load_dotenv()
    clientId = os.getenv('clientID')
    clientSecret = os.getenv('clientSecret')
    yahooLeagueLoader = YahooLeagueLoader(
        '68635', [2015,2016,2017,2018,2019,2020], clientId=clientId, clientSecret=clientSecret, loginTimeoutSeconds=6
    )

    #2020: 68635 2023:264328
    yahooLeague: League = yahooLeagueLoader.loadLeague()

    # When you load your Yahoo league, it will attempt to authenticate based on your client ID and client secret.
    # You can set a timeout for this by passing in loginTimeoutSeconds.
    # clientId = "myClientId"
    # clientSecret = "myClientSecret"
    # yahooLeagueLoader = YahooLeagueLoader(
    #   "123456", [2013,2014,2015,2016,2017,2018,2019, 2020], clientId=clientId, clientSecret=clientSecret, loginTimeoutSeconds=4
    #)
    # yahooleague: League = yahooLeagueLoader.loadLeague()

    # Second, get League from Sleeper for 2021-2022.
    #sleeperleagueID=os.getenv('sleeperLeagueID')
    # #sleeper doesn't like a definition being passed as a str, only straight defined int
    sleeperLeagueLoader = SleeperLeagueLoader("916883370397880320", [2021, 2022, 2023])
    sleeperLeague: League = sleeperLeagueLoader.loadLeague()

    # Finally, combine the leagues to get a single League object.
    #myLeague = yahooLeague + sleeperLeague
    myLeague = sleeperLeague
    # Save league stats to an Excel sheet.
    leagueToExcel(myLeague, "/users/brandonschleter/Sleeper/comboLeagueStats.xlsx")

     #   Special behaviors:
    #       - name
    #           - "name" will become a combination of both league's names IF the names are not the same.
    #       - owners
    #           - "owners" will be merged on Owner.name, since this field must be unique by League.
    #           - Unmerged owners will simply be combined.
    #       - years
    #           - "years" will be combined in order oldestYearNumber -> newestYearNumber.
    #           - Duplicate Year.yearNumber across leagues will raise an exception.



