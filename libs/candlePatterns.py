''' This function determines if a candle is a "doji" or a doji candlestick pattern. A "doji" is a candlestick 
    formation with a very small or non-existent body, where the opening price and closing price are very close or equal. 
    The doji indicates indecision in the market and may signal a possible reversal or trend change.'''
def is_doji(open_price, close_price, high_price, low_price, threshold_percentage=0.1):
    # Calculate the range of the candle
    vela_rango = high_price - low_price
    
    # Calculate the difference between the opening price and the closing price
    diferencia_cierre_apertura = abs(close_price - open_price)
    
     # Calculate the percentage difference with respect to the candle range
    porcentaje_diferencia = diferencia_cierre_apertura / vela_rango
    
    # Check if the percentage difference is below the set threshold
    return porcentaje_diferencia <= threshold_percentage

''' This function identifies if a candle is a "low test" or a "hammer." A "low test" is a candlestick formation that usually 
    occurs in a downtrend. It has a small body at the bottom of the candle and a longer upper shadow, suggesting a possible 
    bullish reversal.'''
def is_low_test(open_price, close_price, high_price, low_price, threshold_body_percentage=0.1, threshold_upper_shadow_percentage=0.5):
    # Calculate the size of the candle body
    cuerpo_vela = abs(close_price - open_price)
    
    # Calculate the candle shadows
    sombra_superior = high_price - max(open_price, close_price)
    # sombra_inferior = min(open_price, close_price) - low_price
    
    # Calculate the percentage of body size and upper shadow with respect to the candle range
    vela_rango = high_price - low_price
    porcentaje_cuerpo = cuerpo_vela / vela_rango
    porcentaje_sombra_superior = sombra_superior / vela_rango
    # porcentaje_sombra_inferior = sombra_inferior / vela_rango

    # Check if the body and upper shadow percentages meet the set thresholds
    if porcentaje_cuerpo <= threshold_body_percentage and porcentaje_sombra_superior >= threshold_upper_shadow_percentage:
        return True  # Indicates a low test candlestick
    else:
        return False  # Not a low test candlestick

''' This function determines if a candle is a "high test" or a "shooting star." A "high test" is a candlestick formation that 
    typically occurs in an uptrend. It has a small body at the top of the candle and a longer lower shadow, suggesting a possible 
    bearish reversal.'''
def is_high_test(open_price, close_price, high_price, low_price, threshold_body_percentage=0.1, threshold_lower_shadow_percentage=0.5):
    # Calculate the size of the candle body
    cuerpo_vela = abs(close_price - open_price)

    # Calculate the candle shadows
    # sombra_superior = high_price - max(open_price, close_price)
    sombra_inferior = min(open_price, close_price) - low_price

    # Calculate the percentage of body size and lower shadow with respect to the candle range
    vela_rango = high_price - low_price
    porcentaje_cuerpo = cuerpo_vela / vela_rango
    porcentaje_sombra_inferior = sombra_inferior / vela_rango
    # porcentaje_sombra_superior = sombra_superior / vela_rango

    # Check if the body and lower shadow percentages meet the set thresholds
    if porcentaje_cuerpo <= threshold_body_percentage and porcentaje_sombra_inferior >= threshold_lower_shadow_percentage:
        return True  # Indicates a high test candlestick
    else:
        return False  # Not a high test candlestick

''' This function identifies if a candle is a "bullish engulfing" pattern. A "bullish engulfing" is a pattern composed of 
    a small bearish candle followed by a larger bullish candle that completely "engulfs" the previous candle. This pattern may 
    indicate a possible bullish reversal in a downtrend.'''
def is_bullish_engulfing(open_price, close_price, prev_open_price, prev_close_price):
    # Check if the current candle is bullish and the previous candle is bearish
    if close_price > open_price and prev_close_price < prev_open_price:
        # Check if the current candle completely engulfs the previous candle
        if open_price <= prev_close_price and close_price >= prev_open_price:
            return True  # It is a bullish engulfing candlestick
    return False

''' This function determines if a candle is a "bearish engulfing" pattern. A "bearish engulfing" is a pattern composed of 
    a small bullish candle followed by a larger bearish candle that completely "engulfs" the previous candle. This pattern may 
    indicate a possible bearish reversal in an uptrend.'''
def is_bearish_engulfing(open_price, close_price, prev_open_price, prev_close_price):
    # Check if the current candle is bearish and the previous candle is bullish
    if close_price < open_price and prev_close_price > prev_open_price:
        # Check if the current candle completely engulfs the previous candle
        if open_price >= prev_close_price and close_price <= prev_open_price:
            return True  # It is a bearish engulfing candlestick
    return False