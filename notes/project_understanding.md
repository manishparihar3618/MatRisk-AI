# Dataset Understanding

## DS1 Material Properties
Purpose:
Contains material properties used in bridge construction.

Important Features:
- Material Name
- Density
- Bulk Modulus
- Shear Modulus
- Crystal Structure

Why Important:
Strong and stable materials reduce bridge failure risk.

Possible Contribution:
- Material Strength Score*
- Stability Score
- Durablility Score


## DS2 Commodity Prices
Purpose:
Tracks commodity prices over time.

Important Features:
- Commodity Name
- Price (Open, High, Low, Close)
- Date
- Volume 
- Volatility

Why Important:
High price volatility can increase project risk.
Instability in Commodity Prices can increase Construction cost, maintanence cost and supply chain uncertaninty

Possible Contribution:
- Market Risk Score*
- Economic Risk 
- Supply Chain Risk


## DS3 Infrastructure Bridges
Purpose:
Contains bridge and infrastructure information.

Important Features:
- Bridge Age
- Condition Rating
- Material
- Structure defeciency
- Traffic Load
- Remaining Thickness
- Corrosion Rate
- Tensile Strength
- Yield Strength

Why Important:
Older bridges generally have higher failure probability.
Directly Measure the health and condition of a bridge 

Possible Contribution:
Infrastructure Risk Score
Structural Risk
Physical Risk
Operational Risk


## DS4 Crossdomain Features 
Purpose:
Combines information from multiple domains such as material quality, supply chain, market conditions, and sustainability factors.

Important Features:
- MQI (Material Quality Index)
- Supply Disruption Probability
- Substitution Elasticity
- Herfindahl Index
- Carbon Intensity
- MQI Trends

Why Important:
Shows external risks affecting materials and projects.
Helps estimate risks that arise from material availability, supplier dependency, market conditions, and quality trends.

Possible Contribution:
- Supply Chain Risk Score
- Market Risk
- Material Quality Risk


## DS5 Element Prices 
Purpose:
Tracks prices of important engineering elements.

Important Features:
- Element
- Price per Kg
- Monthly Return
- Base Price

Why Important:
Material cost fluctuations affect project planning.
Helps estimate economic and mainatainace risks caused by changing material prices.

- Possible Contribution:
- Economic Risk Score
- Material Cost Risk
- Maintanaince Risk


## DS6 Historical Failures
Purpose:
Contains records of past infrastructure failures.

Important Features:
- Failure Mode
- Severity
- Corrosion Rate
- Age at Failure
- Warning lead time
- Was predicted
- Repair cost
- Loss ratio


Why Important:
Past failures help predict future failures.

Possible Contribution:
- Failure Risk Score
- Failure Pattern Risk
- Severity Risk




# How can all this Datasets Combined contribute in single bridge risk score ??
##  Bullet Points
- Material with low stability, durability, strength have more failure rate
- Volatility in prices delay maintainence results in increase in failure rate 
- Older bridges have higher risk 
- high corrosion rate reduce bridge health
- Supply chain disruptions affect repair schedules 
- historical failures reveal common failure pattern 
- poor condition rating indicates structural problems 
- MQI affect durability
- high traffic load accelarates bridge wear and tear
- lower remaining thickness indicates fast corrosion
- large repair cost means its critical already 
- high fatigue cycles increase structural stress 
- high loss ratio suggests severe impact 
- If a material if difficult to replace with another material(like a speacila steel) then supply problem become more dangeuous 
- High supply disruption (factory shutdown or transportation issue) affect project continuity
- If warning time is less engineer get less time to repair 
- Higher tensile strength can withstand greater load before failure
- Higher carbon intensity may increase dependence on a few suppliers, increasing supply risk.
- 