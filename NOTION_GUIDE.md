\# Notion Portfolio Page Setup Guide 📋



\## Page Structure



\### 1. Header Section

\*\*Title:\*\* Netflix India Market Entry Strategy  

\*\*Subtitle:\*\* SQL + Calculus + Strategic Analysis  

\*\*Cover Image:\*\* Use a Netflix/India themed image (search Unsplash in Notion)  

\*\*Icon:\*\* 🎬 or 📊



---



\### 2. Project Overview (Toggle Block)



\*\*What to write:\*\*

> Analyzed Netflix's strategic challenge to acquire 100 million subscribers in India's competitive streaming market. Combined SQL analysis, calculus-based optimization, and McKinsey-style frameworks to deliver actionable recommendations backed by quantitative evidence.



\*\*Key Stats (3 columns):\*\*

\- 📊 5,000+ subscriber records analyzed

\- 💰 $2-3.5B revenue opportunity identified  

\- 🎯 16 SQL queries + 4 Excel models



---



\### 3. Skills Demonstrated (Callout Boxes)



\*\*SQL \& Data Analysis\*\*

\- Database design (5 tables, 5,000+ records)

\- Complex queries: JOINs, subqueries, window functions

\- Customer segmentation, churn analysis, cohort retention



\*\*Calculus Applications\*\*

\- CLV using limit theory

\- Pricing optimization (marginal analysis)

\- Sensitivity analysis



\*\*Business Strategy\*\*

\- McKinsey/BCG-style case study

\- Market sizing (TAM/SAM/SOM)

\- 3-year implementation roadmap



---



\### 4. Key Findings (Database - Table View)



Create a table with these columns:

| Analysis | Finding | Business Impact |

|----------|---------|----------------|

| Pricing | Optimal $2.85-3.50/month | +40% subscriber potential |

| CLV | $17.54 at 12% churn | 31% increase if churn→8% |

| Market | 300M viewers, 50-75M realistic | $2-3.5B revenue opportunity |

| Competition | Hotstar 70% share via freemium | Netflix serves only 6% of market |



---



\### 5. SQL Examples (Code Blocks)



\*\*Market Sizing Query:\*\*

```sql

SELECT 

&nbsp;   segment\_name,

&nbsp;   video\_viewers\_millions,

&nbsp;   willingness\_to\_pay\_usd,

&nbsp;   ROUND(video\_viewers\_millions \* willingness\_to\_pay\_usd \* 12, 2) AS annual\_revenue\_millions

FROM market\_segments

ORDER BY annual\_revenue\_millions DESC;

```



\*\*CLV Analysis Query:\*\*

```sql

SELECT 

&nbsp;   plan\_type,

&nbsp;   ROUND(AVG(monthly\_price), 2) AS avg\_arpu,

&nbsp;   ROUND(1.0 / AVG(CASE WHEN status = 'Churned' THEN 1.0 ELSE 0.0 END), 1) AS avg\_lifetime\_months

FROM subscribers

GROUP BY plan\_type;

```



---



\### 6. Excel Models (Embed Files)



\*\*Upload these files to Notion:\*\*

1\. Netflix India Financial Model.xlsx

2\. Screenshots of key sheets (Pricing Optimization, CLV Analysis)



\*\*Caption each:\*\* "Live Excel model with formulas - download to explore"



---



\### 7. Strategic Recommendations (Numbered List)



1\. \*\*Three-Tier Pricing\*\*

&nbsp;  - Mobile: $2.85 → 40-60M subs

&nbsp;  - Premium: $5-7 → 15-25M subs

&nbsp;  - Ultra: $9-11 → 5-10M subs



2\. \*\*Regional Content 3x Investment\*\*

&nbsp;  - Tamil, Telugu, Bengali, Marathi focus

&nbsp;  - 60% lower cost, 70% larger audience



3\. \*\*Telecom Partnerships\*\*

&nbsp;  - Bundle with Jio/Airtel

&nbsp;  - Reduce CAC from $5 to <$1



4\. \*\*Selective Ad-Supported Tier\*\*

&nbsp;  - $0.99/month for Tier 3/rural

&nbsp;  - Unlock 150M+ potential viewers



---



\### 8. Project Files (Links)



\*\*GitHub Repository:\*\* \[Link to your repo]  

\*\*Case Study Document:\*\* \[Upload .docx file]  

\*\*Excel Model:\*\* \[Upload .xlsx file]  

\*\*SQL Queries:\*\* \[Code block or file upload]



---



\### 9. Target Roles (Gallery View)



Create cards for:

\- 💼 Management Consulting (McKinsey, BCG, Bain)

\- 💰 Investment Banking / Private Equity

\- 📊 Strategy \& Analytics

\- 🎯 Product Management



---



\### 10. Contact CTA (Callout)



> \*\*Let's Connect!\*\*  

> Interested in discussing this project or exploring opportunities?  

> 📧 your.email@example.com  

> 💼 \[LinkedIn Profile]  

> 🐙 \[GitHub Repository]



---



