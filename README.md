\# Netflix India Market Entry Strategy 🎬



A comprehensive data-driven analysis of Netflix's strategic challenge to acquire 100 million subscribers in India's competitive streaming market. This project combines \*\*SQL analysis\*\*, \*\*calculus-based optimization\*\*, and \*\*strategic frameworks\*\* to provide actionable recommendations backed by quantitative evidence.



---



\## 🎯 Project Overview



\*\*Business Problem:\*\* Netflix has only 2 million subscribers in India versus Hotstar's 129 million, despite declaring India as the source of its "next 100 million" subscribers. Should Netflix adapt its premium positioning, ad-free model, and pricing strategy to win in this price-sensitive market?



\*\*Approach:\*\* Built comprehensive database, performed SQL analysis on 5,000+ subscriber records, applied calculus for CLV optimization, and developed strategic recommendations in consulting format.



\*\*Key Finding:\*\* Netflix can capture 50-75 million subscribers and generate $2-3.5 billion annual revenue through tiered pricing ($2.50-11/month), regional content investment, and selective ad-supported offerings.



---



\## 📊 Skills Demonstrated



\### SQL \& Data Analysis

\- ✅ Database design with 5 tables, 5,000+ records

\- ✅ Complex queries: JOINs, subqueries, window functions, CTEs

\- ✅ Customer segmentation by demographics, behavior, engagement

\- ✅ Churn analysis, cohort retention, market sizing

\- ✅ Competitive benchmarking across 10 streaming platforms



\### Calculus Applications

\- ✅ \*\*Customer Lifetime Value\*\* using limit theory: `CLV = ARPU × Margin / (Churn + Discount)`

\- ✅ \*\*Pricing optimization\*\* through marginal analysis (finding where MR = MC)

\- ✅ Sensitivity analysis showing exponential churn impact on CLV

\- ✅ Demand curve modeling with price elasticity



\### Business Strategy

\- ✅ McKinsey/BCG-style case study analysis

\- ✅ Market sizing: TAM/SAM/SOM framework for 300M video viewers

\- ✅ Competitive positioning analysis

\- ✅ Strategic recommendations with 3-year implementation roadmap

\- ✅ Financial modeling with revenue projections



---



\## 📁 Project Structure

```

netflix-india-case-study/

│

├── data/

│   └── netflix\_india.db                     # SQLite database with 5 tables

│

├── sql/

│   ├── analysis\_queries.sql                 # 16 SQL queries for analysis

│   └── query\_results.txt                    # Query outputs

│

├── analysis/

│   └── netflix\_india\_financial\_model.xlsx   # Excel with CLV, pricing, market sizing

│

├── docs/

│   └── Netflix\_India\_Case\_Study.docx        # 12-page strategic analysis

│

├── generate\_data.py                         # Database generation script

├── run\_queries.py                           # SQL execution script

├── create\_excel.py                          # Financial model generator

└── README.md

```



---



\## 🔍 Key Analyses



\### 1. Market Opportunity Analysis

\*\*Finding:\*\* Total addressable market of 300 million video viewers segmented into 5 tiers by income and language preference. Realistic subscriber potential: 50-75 million.



\*\*SQL Query Example:\*\*

```sql

SELECT 

&nbsp;   m.segment\_name,

&nbsp;   m.video\_viewers\_millions AS potential\_viewers,

&nbsp;   m.willingness\_to\_pay\_usd,

&nbsp;   ROUND(m.video\_viewers\_millions \* m.willingness\_to\_pay\_usd \* 12, 2) AS annual\_revenue\_potential\_millions

FROM market\_segments m

ORDER BY annual\_revenue\_potential\_millions DESC;

```



\### 2. Pricing Optimization

\*\*Finding:\*\* Optimal price point is $2.85-3.50/month for mobile plan. Pricing above $5 reduces conversion by 60%.



\*\*Excel Model:\*\* Uses marginal analysis to find price where `Marginal Revenue = Marginal Cost`



\### 3. Customer Lifetime Value (Calculus)

\*\*Finding:\*\* At 12% monthly churn, CLV = $17.54. Reducing churn to 8% increases CLV by 31% due to geometric series convergence.



\*\*Formula:\*\* 

```

CLV = lim(n→∞) Σ\[ARPU × (Retention Rate)^t × (1+Discount)^-t]

&nbsp;   = ARPU × Gross Margin / (Churn Rate + Discount Rate)

```



\### 4. Competitive Analysis

\*\*Finding:\*\* Hotstar dominates with 70% market share through freemium model. Netflix's premium-only approach addresses just 6% of market (English speakers).



\*\*SQL Query Example:\*\*

```sql

SELECT 

&nbsp;   competitor\_name,

&nbsp;   users\_millions,

&nbsp;   market\_share\_pct,

&nbsp;   pricing\_model,

&nbsp;   ad\_supported

FROM competitors

ORDER BY market\_share\_pct DESC;

```



\### 5. Content Strategy Gap

\*\*Finding:\*\* 70% of viewers prefer regional language content, but Netflix supports only 10 languages vs competitors' 12. Regional content costs 60% less but serves larger audience.



---



\## 💡 Strategic Recommendations



\### 1. Three-Tier Pricing Architecture

\- \*\*Mobile Mass Market ($2.50-2.85):\*\* Target 40-60M subscribers in Tier 2/3 cities

\- \*\*Premium Streaming ($5-7):\*\* Urban professionals, 15-25M potential

\- \*\*Ultra Premium ($9-11):\*\* Elite segment, 5-10M potential



\### 2. Regional Content Acceleration

\- Triple investment in Tamil, Telugu, Bengali, Marathi content

\- Shift 30% of budget from premium Hindi/English to regional productions

\- Partner with regional studios rather than building in-house



\### 3. Telecom Partnerships

\- Bundle Netflix with Jio/Airtel data plans

\- Reduce CAC from $5 to <$1 while maintaining ARPU

\- Leverage telecom's 500M+ customer base



\### 4. Selective Ad-Supported Tier

\- Launch $0.99/month ad-supported mobile plan for Tier 3/rural

\- Pilot in India only, positioned as entry to premium experience

\- Unlocks 150M+ viewers who won't pay current prices



\*\*Projected Impact:\*\* 50-75 million subscribers, $2.0-3.5 billion annual revenue within 3 years



---



\## 📈 Sample Results



\### Pricing Analysis Output

| Price | Subscribers (M) | Revenue (M) | Profit (M) |

|-------|----------------|-------------|-----------|

| $1.99 | 2.8 | $5.57 | $3.17 |

| $2.85 | 2.0 | $5.70 | $3.30 |

| $3.50 | 1.6 | $5.60 | $3.20 |

| $5.00 | 1.0 | $5.00 | $2.50 |



\### CLV by Churn Rate

| Monthly Churn | CLV | Change |

|--------------|-----|--------|

| 5% | $33.60 | +91% |

| 8% | $23.08 | +31% |

| 12% | $17.54 | Baseline |

| 15% | $13.85 | -21% |



---



\## 🛠️ Technologies Used



\- \*\*Python 3.14:\*\* Data generation, automation

\- \*\*SQLite:\*\* Database management

\- \*\*SQL:\*\* Advanced queries and analysis

\- \*\*Excel/openpyxl:\*\* Financial modeling with formulas

\- \*\*python-docx:\*\* Document generation

\- \*\*Pandas:\*\* Data manipulation



---



\## 🚀 How to Run This Project



\### Prerequisites

```bash

python --version  # Requires Python 3.7+

pip install pandas openpyxl python-docx

```



\### Generate Database

```bash

python generate\_data.py

```



\### Run SQL Analysis

```bash

python run\_queries.py

```



\### Create Excel Model

```bash

python create\_excel.py

```



\### Generate Case Study Document

```bash

python create\_case\_study.py

```



---



\## 📚 Based On



\*\*MIT Sloan Case Study:\*\* "Netflix Goes to Bollywood" by Donald Sull and Stefano Turconi (2021)



This project analyzes the strategic challenge Netflix faced entering India's streaming market, where it needed to balance global brand consistency with local market realities.



---



\## 🎓 Learning Outcomes



\### For Recruiters

This project demonstrates skills directly applicable to:

\- \*\*Management Consulting:\*\* Strategic problem-solving, framework application, client-ready deliverables

\- \*\*Investment Banking/Private Equity:\*\* Financial modeling, market sizing, valuation

\- \*\*Strategy \& Analytics:\*\* Data-driven decision making, competitive analysis, business case development



\### Technical Skills

\- Advanced SQL for business analytics

\- Calculus applications in business contexts

\- Financial modeling with Excel

\- Professional business documentation

\- Python for automation and analysis



---



\## 📧 Contact



\*\*\[Your Name]\*\*

\- Email: your.email@example.com

\- LinkedIn: \[linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)

\- Portfolio: \[yourportfolio.com](https://yourportfolio.com)



---



\## 📝 License



This project is for educational and portfolio purposes. Case study content based on publicly available MIT case study.



---



\## ⭐ Acknowledgments



\- MIT Sloan School of Management for the original case study

\- Netflix for the inspiring business challenge

\- Open source community for Python libraries



---



\*\*⭐ If this project helped you learn SQL, calculus, or business strategy, please star this repo!\*\*

