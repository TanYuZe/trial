import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup as soup
import urllib
from urllib.request import Request, urlopen


def page_settings():
    with st.container():
        components.html(
        """
        <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_d0726"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 800,
  "height": 700,
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_d0726"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->
        """,height = 700
        )

    st.title('View fundamentals of stock')
    with st.expander('Description'):
        st.write("Enter stock symbol for the stock that you would like to view.")
        st.write("Results provided would be the fundementals of stock, and also the latest news of the particular stock")
    user_input = st.text_input("ENTER STOCK SYMBOL",value="AAPL")
    information = []
    information.append(yf.Ticker(user_input).info)
    df = pd.DataFrame(information)
    col1,col2,col3 = st.columns(3)
    overview = {}
    try:
        for i in df:
            overview[i] = df[i].loc[0]
        del overview['longBusinessSummary']
        for key, value in overview.items():
            with col1:
                if 'longName' == key:
                    st.write(key + ":  " + value)
                if 'shortName' == key:
                    st.write(key + ":  " + str(value))
                if 'country' == key:
                    st.write(key + ":  " + value)
                if 'sector' == key:
                    st.write(key + ":  " + value)
                if 'industry' == key:
                    st.write(key + ":  " + value)
                if 'financialCurrency' == key:
                    st.write(key + ":  " + str(value))
                if 'exchange' == key:
                    st.write(key + ":  " + str(value))
                if 'quoteType' == key:
                    st.write(key + ":  " + str(value))
                if 'market' == key:
                    st.write(key + ":  " + str(value))
                if 'fullTimeEmployees' == key:
                    st.write(key + ":  " + str(value))
                if 'website' == key:
                    st.write(key + ":  " + str(value))
                if 'bid' == key:
                    st.write(key + ":  " + str(value))
                if 'revenuePerShare' == key:
                    st.write(key + " ($): " + str(value))
                if 'totalCashPerShare' == key:
                    st.write(key + " ($):  " + str(value))
                if 'ebitda' == key:
                    st.write(key + " ($):  " + str(value))
                if 'beta' == key:
                    st.write(key + ":  " + str(value))
                if 'returnOnAssets' == key:
                    st.write(key + " (%):  " + str(value))
            with col2:
                if 'regularMarketVolume' == key:
                    st.write(key + ":  " + str(value))
                if 'averageVolume10days' == key:
                    st.write(key + ":  " + str(value))
                if 'averageDailyVolume10Day' == key:
                    st.write(key + ":  " + str(value))
                if 'profitMargins' == key:
                    st.write(key + " (%):  " + str(value))
                if 'ebitdaMargins' == key:
                    st.write(key + " (%):  " + str(value))
                if 'grossMargins' == key:
                    st.write(key + " (%):  " + str(value))
                if 'operatingMargins' == key:
                    st.write(key + " (%):  " + str(value))
                if 'quickRatio' == key:
                    st.write(key + ":  " + str(value))
                if 'payoutRatio' == key:
                    st.write(key + ":  " + str(value))
                if 'revenueGrowth' == key:
                    st.write(key + " (%):  " + str(value))
                if 'currentRatio' == key:
                    st.write(key + ":  " + str(value))
                if 'bookValue' == key:
                    st.write(key + ":  " + str(value))
                if 'priceToBook' == key:
                    st.write(key + ":  " + str(value))
                if 'heldPercentInstitutions' == key:
                    st.write(key + " (%):  " + str(value))
                if 'heldPercentInsiders' == key:
                    st.write(key + " (%):  " + str(value))
                if 'sharesOutstanding' == key:
                    st.write(key + ":  " + str(value))
                if 'floatShares' == key:
                    st.write(key + ":  " + str(value))
            with col3:
                if 'grossProfits' == key:
                    st.write(key + " ($):  " + str(value))
                if 'totalCash' == key:
                    st.write(key + " ($):  " + str(value))
                if 'totalDebt' == key:
                    st.write(key + " ($):  " + str(value))
                if 'totalRevenue' == key:
                    st.write(key + " ($):  " + str(value))
                if 'operatingCashflow' == key:
                    st.write(key + " ($):  " + str(value))
                if 'freeCashflow' == key:
                    st.write(key + " ($):  " + str(value))
                if 'enterpriseValue' == key:
                    st.write(key + " ($):  " + str(value))
                if 'mostRecentQuarter' == key:
                    st.write(key + " ($):  " + str(value))
                if 'marketCap' == key:
                    st.write(key + ":  " + str(value))
                if 'lastFiscalYearEnd' == key:
                    st.write(key + " ($):  " + str(value))
                if '52WeekChange' == key:
                    st.write(key + " (%):  " + str(value))
                if 'fiftyTwoWeekHigh' == key:
                    st.write(key + " ($):  " + str(value))
                if 'fiftyTwoWeekLow' == key:
                    st.write(key + " ($):  " + str(value))
                if 'fiftyDayAverage' == key:
                    st.write(key + " ($):  " + str(value))
                if 'debtToEquity' == key:
                    st.write(key + ":  " + str(value))
                if 'returnOnEquity' == key:
                    st.write(key + " (%):  " + str(value))
                if 'lastDividendValue' == key:
                    st.write(key + ":  " + str(value))

            #news scraper
        st.title("Latest News column")
        url = ("http://finviz.com/quote.ashx?t=" + user_input.lower())
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        html = soup(webpage, "html.parser")
    except KeyError:
        st.error('Please enter valid input')
    except NameError:
        pass
    except HTTPError:
        pass


    def get_news():
        try:   # Find news table
            news = pd.read_html(str(html), attrs={'class': 'fullview-news-outer'})[0]
            links = []
            for a in html.find_all('a', class_="tab-link-news"):
                links.append(a['href'])
                        # Clean up news dataframe
            news.columns = ['Date', 'News Headline']
            news['Article Link'] = links
            news = news.set_index('Date')
            return news

        except Exception as e:
            return e
        except requests.HTTPError as exception:
            pass
    st.write(get_news())

def app():
    with st.container():
        page_settings()
