
import streamlit as st
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="OmniMarket Options Simulator", layout="wide")

st.title("OmniMarket Options Strategy Simulator")

ticker = st.text_input("Enter Ticker (e.g., AAPL, TSLA)", "AAPL").upper()

try:
    stock = yf.Ticker(ticker)
    expirations = stock.options

    if not expirations:
        st.error("No options expirations found for this ticker.")
    else:
        expiry = st.selectbox("Select Expiration Date", expirations)

        chain = stock.option_chain(expiry)
        calls = chain.calls
        puts = chain.puts

        st.subheader("Define Strategy Legs")
        st.caption("Add multiple legs (buy/sell call or put options)")

        legs = []
        with st.form("strategy_form"):
            for i in range(1, 4):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    leg_type = st.selectbox(f"Leg {i} - Type", ["Call", "Put"], key=f"type_{i}")
                with col2:
                    side = st.selectbox(f"Leg {i} - Buy/Sell", ["Buy", "Sell"], key=f"side_{i}")
                with col3:
                    strike = st.number_input(f"Leg {i} - Strike", min_value=0.0, step=1.0, key=f"strike_{i}")
                with col4:
                    enabled = st.checkbox(f"Use Leg {i}", key=f"enable_{i}", value=(i == 1))
                if enabled:
                    legs.append({"type": leg_type.lower(), "side": side.lower(), "strike": strike})
            submitted = st.form_submit_button("Simulate")

        if submitted and legs:
            S0 = stock.history(period='1d')['Close'].iloc[-1]
            price_range = np.linspace(S0 * 0.7, S0 * 1.3, 150)
            pnl = np.zeros_like(price_range)

            for leg in legs:
                df = calls if leg['type'] == 'call' else puts
                match = df[df['strike'] == leg['strike']]
                if not match.empty:
                    row = match.iloc[0]
                    premium = (row['bid'] + row['ask']) / 2
                    for i, price in enumerate(price_range):
                        intrinsic = max(0, price - leg['strike']) if leg['type'] == 'call' else max(0, leg['strike'] - price)
                        leg_pnl = intrinsic - premium if leg['side'] == 'buy' else premium - intrinsic
                        pnl[i] += leg_pnl

            st.subheader("Strategy P&L at Expiry")
            fig, ax = plt.subplots()
            ax.plot(price_range, pnl, label="P&L")
            ax.axhline(0, color="black", linestyle="--")
            ax.set_xlabel("Stock Price at Expiry")
            ax.set_ylabel("Profit / Loss")
            ax.set_title(f"{ticker} Strategy P&L")
            ax.grid(True)
            st.pyplot(fig)

except Exception as e:
    st.error(f"Error: {e}")
