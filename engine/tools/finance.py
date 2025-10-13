from langchain.tools import tool
import yfinance as yf

@tool("stock_report", return_direct=True)
def stock_report(ticker: str) -> str:
    """Get a short financial report of a stock symbol using yfinance.
    
    Args:
        ticker: ticker of the stock to be queried
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        name = info.get("shortName", ticker)
        price = info.get("currentPrice", None)
        previous_close = info.get("previousClose", None)
        market_cap = info.get("marketCap", None)
        pe_ratio = info.get("trailingPE", None)
        high_52 = info.get("fiftyTwoWeekHigh", None)
        low_52 = info.get("fiftyTwoWeekLow", None)

        # Compute % change if possible
        if price and previous_close:
            change = ((price - previous_close) / previous_close) * 100
            change_str = f"{change:.2f}%"
        else:
            change_str = "N/A"

        report = (
            f"📊 Stock Report: {name} ({ticker.upper()})\n"
            f"• Current Price: ${price:.2f}\n"
            f"• Change (1D): {change_str}\n"
            f"• Market Cap: {market_cap:,} USD\n"
            f"• P/E Ratio: {pe_ratio}\n"
            f"• 52-Week Range: ${low_52:.2f} - ${high_52:.2f}"
        )

        return report

    except Exception as e:
        return f"Error fetching data for {ticker}: {e}"
