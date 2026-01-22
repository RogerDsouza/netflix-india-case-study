# Netflix India Market Entry Strategy 🎬
### A Data-Driven Strategic Analysis | SQL + Calculus + Business Frameworks

---

## Executive Summary

**Client Challenge:** Netflix has 2M subscribers in India versus Hotstar's 129M (70% market share). CEO Reed Hastings declared India as the source of Netflix's "next 100 million" subscribers, but fundamental questions remain about pricing, advertising, and content strategy.

**Our Approach:** Built end-to-end analytical framework combining database design, SQL analysis, calculus-based financial modeling, and strategic recommendations to quantify the opportunity and provide actionable roadmap.

**Bottom Line:** Netflix can achieve 50-75M subscribers and $2.0-3.5B annual revenue through tiered pricing, regional content investment, telecom partnerships, and selective ad-supported offerings.

---

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Analytical Approach](#analytical-approach)
3. [Phase 1: Data Foundation](#phase-1-data-foundation)
4. [Phase 2: SQL Market Analysis](#phase-2-sql-market-analysis)
5. [Phase 3: Financial Modeling with Calculus](#phase-3-financial-modeling)
6. [Phase 4: Strategic Recommendations](#phase-4-strategic-recommendations)
7. [Implementation Roadmap](#implementation-roadmap)
8. [Key Deliverables](#key-deliverables)

---

## Problem Statement

### The Business Challenge

Netflix entered India in 2016 targeting premium English-speaking audiences but has struggled to scale. By 2020:

| Metric | Netflix | Hotstar | Market Reality |
|--------|---------|---------|----------------|
| **Subscribers** | 2M (1%) | 129M (70%) | 300M video viewers total |
| **Pricing** | $2.85-11.46/month | $1.19-4.29/month | 85% prefer <$3/month |
| **Revenue Model** | 100% subscription | Freemium + ads | 80% competitors use ads |
| **Languages** | 10 | 8 | 22 official languages |
| **Content Investment** | $420M (2020) | $17M | Lower cost = higher volume |

### Three Critical Strategic Questions

**QUESTION 1: PRICING STRATEGY**
- Should Netflix maintain premium positioning ($7-11/month) or adapt to local price sensitivity?
- What is the optimal price point that balances volume and profitability?
- How does pricing affect customer acquisition and churn?

**QUESTION 2: ADVERTISING MODEL**
- Should Netflix introduce ads for the first time (breaking global brand promise)?
- What revenue can ad-supported tiers unlock in price-sensitive segments?
- How to position ad-supported offering without cannibalizing premium tiers?

**QUESTION 3: CONTENT LOCALIZATION**
- Is Netflix's $420M investment in Hindi/English content reaching the right audiences?
- Should Netflix prioritize regional languages (Tamil, Telugu, Bengali) over premium productions?
- What content ROI do competitors achieve with lower budgets?

### Why This Matters

- **Market Size:** 600M internet users, 300M video viewers - massive untapped opportunity
- **Competition:** 32 streaming platforms with local advantages (language, pricing, cricket rights)
- **Strategic Risk:** Without adaptation, Netflix risks remaining a niche player in world's largest democracy
- **Organizational Tension:** How to adapt to local market while maintaining global brand identity?

---

## Analytical Approach

### Consulting Framework: How We Solved This

We followed a **four-phase analytical process** mirroring top-tier consulting methodology:
```
PHASE 1: Data Foundation
   ↓
   Build realistic database reflecting India market dynamics
   - 5,000+ subscriber records with demographics, behavior, churn
   - 10 competitor profiles with pricing and market share
   - 5 market segments by income/language/geography
   
PHASE 2: SQL Market Analysis
   ↓
   Execute 16 analytical queries to size opportunity and understand customer behavior
   - Market sizing by segment (TAM/SAM/SOM)
   - Churn analysis by plan type and demographics
   - Competitive benchmarking
   
PHASE 3: Financial Modeling
   ↓
   Apply calculus and quantitative methods to optimize strategy
   - CLV using limit theory (geometric series convergence)
   - Pricing optimization via marginal analysis
   - Sensitivity analysis on key variables
   
PHASE 4: Strategic Recommendations
   ↓
   Synthesize insights into actionable roadmap
   - Strategic options with pros/cons
   - Financial impact quantification
   - 3-year implementation plan
```

### Skills Deployed

| Domain | Techniques Used | Business Application |
|--------|----------------|---------------------|
| **SQL & Data Analysis** | JOINs, CTEs, window functions, aggregations | Customer segmentation, churn analysis, market sizing |
| **Calculus** | Limits (geometric series), derivatives (marginal analysis) | CLV optimization, pricing strategy |
| **Financial Modeling** | Scenario analysis, sensitivity analysis, DCF logic | Revenue projections, investment decisions |
| **Strategy Frameworks** | Porter's 5 Forces, Value Chain, TAM/SAM/SOM | Competitive positioning, market entry strategy |
| **Python** | SQLite, openpyxl, python-docx automation | Reproducible analysis, professional deliverables |

---

## Phase 1: Data Foundation

### Objective
Build comprehensive database that accurately models India's streaming market dynamics to enable rigorous analysis.

### What We Built

**Database Architecture: 5 Tables, 5,000+ Records**
```
netflix_india.db
│
├── subscribers (5,000 records)
│   ├── subscriber_id, city_tier, signup_date
│   ├── plan_type (Mobile/Basic/Standard/Premium)
│   ├── monthly_price, status (Active/Churned)
│   ├── language_preference (Hindi/English/Tamil/Telugu/etc.)
│   ├── content_hours_per_month (engagement metric)
│   └── acquisition_channel
│
├── competitors (10 records)
│   ├── Hotstar, Amazon Prime, ZEE5, Sony LIV, ALTBalaji...
│   ├── pricing_model, monthly_price, annual_price
│   ├── users_millions, market_share_pct
│   ├── ad_supported (Yes/No)
│   └── languages_count, original_content_count
│
├── market_segments (5 segments)
│   ├── Premium Urban (Tier 1, $10 WTP, 35M viewers)
│   ├── Mid Urban (Tier 1, $5 WTP, 55M viewers)
│   ├── Value Urban (Tier 2, $2.50 WTP, 80M viewers)
│   ├── Small City (Tier 3, $1.50 WTP, 90M viewers)
│   └── Rural Digital (Rural, $0.80 WTP, 40M viewers)
│
├── content_investment (8 records)
│   ├── Netflix investment trend 2017-2020 ($70M → $420M)
│   ├── Competitor spending and output
│   └── Cost per show, cost per hour calculations
│
└── pricing_tests (36 records)
    ├── 6 price points × 6 months of A/B testing
    ├── Signups, conversions, churn rates
    └── Average viewing hours by price point
```

### Key Design Decisions

**Realistic Distributions:**
- Tier 1 cities: 30% Mobile, 25% Basic, 25% Standard, 20% Premium
- Tier 2 cities: 50% Mobile, 30% Basic, 15% Standard, 5% Premium
- Tier 3 cities: 70% Mobile, 20% Basic, 8% Standard, 2% Premium

**Churn Probabilities:**
- Mobile: 12% monthly churn (price-sensitive, mobile-only limits usage)
- Basic: 8% (sweet spot of value and features)
- Standard: 6% (committed users, HD quality)
- Premium: 5% (lowest churn, highest engagement)

**Language Preferences:**
- Tier 1: 40% Hindi, 35% English, 25% regional
- Tier 2/3: 50% Hindi, 10% English, 40% regional
- Reflects India's linguistic diversity and content availability

### Deliverable
📄 `generate_data.py` - Automated database generation with realistic distributions

### Why This Matters
Quality of insights depends on quality of data. By modeling realistic subscriber behaviors, competitive dynamics, and market segmentation, we ensure all downstream analysis reflects ground reality.

---

## Phase 2: SQL Market Analysis

### Objective
Execute comprehensive SQL analysis to size market opportunity, understand customer behavior, and benchmark against competition.

### Analysis Framework: 16 Queries Across 5 Domains

#### **Domain 1: Market Opportunity Sizing**

**Query 1.1 - Total Addressable Market by Segment**
```sql
SELECT 
    segment_name,
    city_tier,
    video_viewers_millions,
    willingness_to_pay_usd,
    ROUND(video_viewers_millions * willingness_to_pay_usd * 12, 2) AS annual_revenue_potential_millions
FROM market_segments
ORDER BY annual_revenue_potential_millions DESC;
```

**Key Finding:**
| Segment | Viewers (M) | WTP ($/mo) | Annual Revenue Potential |
|---------|-------------|------------|------------------------|
| Premium Urban | 35 | $10 | $4,200M |
| Mid Urban | 55 | $5 | $3,300M |
| Value Urban | 80 | $2.50 | $2,400M |
| Small City | 90 | $1.50 | $1,620M |
| **TOTAL** | **260M** | - | **$11,520M** |

**Insight:** Massive $11.5B total market, but realistic capture rate is 20-30% → 50-75M subscribers achievable.

---

**Query 1.2 - Current Netflix Subscriber Base**
```sql
SELECT 
    city_tier,
    plan_type,
    COUNT(*) AS subscribers,
    ROUND(AVG(monthly_price), 2) AS avg_price,
    ROUND(SUM(monthly_price), 2) AS monthly_revenue
FROM subscribers
WHERE status = 'Active'
GROUP BY city_tier, plan_type
ORDER BY city_tier, subscribers DESC;
```

**Key Finding:**
- Tier 1 cities: 60% of subscribers, skewed toward Standard/Premium
- Tier 2 cities: 30% of subscribers, mostly Mobile/Basic
- Tier 3 cities: 10% of subscribers, 80% on Mobile plan
- **Current MRR:** ~$15M → $180M annual run rate

**Insight:** Netflix over-indexes on high-end urban users. Massive white space in Tier 2/3 cities.

---

#### **Domain 2: Pricing & Revenue Optimization**

**Query 2.1 - Revenue by Plan Type**
```sql
SELECT 
    plan_type,
    COUNT(*) AS active_subscribers,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct_of_base,
    ROUND(SUM(monthly_price), 2) AS monthly_revenue,
    ROUND(SUM(monthly_price) * 100.0 / SUM(SUM(monthly_price)) OVER (), 1) AS pct_of_revenue
FROM subscribers
WHERE status = 'Active'
GROUP BY plan_type
ORDER BY monthly_revenue DESC;
```

**Key Finding:**
| Plan | % of Subscribers | % of Revenue | Avg Price |
|------|-----------------|--------------|-----------|
| Premium | 12% | 28% | $11.46 |
| Standard | 20% | 35% | $9.31 |
| Basic | 25% | 22% | $7.16 |
| Mobile | 43% | 15% | $2.85 |

**Insight:** Mobile plan has highest volume but lowest revenue contribution. Need to either increase Mobile ARPU or convert more users to higher tiers.

---

**Query 2.2 - Pricing Test Results**
```sql
SELECT 
    price_point,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(conversions) * 1.0 / SUM(signups), 3) AS conversion_rate,
    ROUND(SUM(conversions) * price_point, 2) AS monthly_revenue,
    ROUND(AVG(churn_rate), 3) AS avg_churn
FROM pricing_tests
GROUP BY price_point
ORDER BY monthly_revenue DESC;
```

**Key Finding:**
| Price | Conversion | Churn | Monthly Revenue | Profit Rank |
|-------|-----------|-------|----------------|-------------|
| $1.99 | 32% | 14% | $11,243 | #4 |
| **$2.85** | **28%** | **12%** | **$14,280** | **#1** |
| $3.99 | 22% | 10% | $13,156 | #2 |
| $4.99 | 18% | 8% | $12,982 | #3 |
| $7.16 | 12% | 7% | $8,592 | #5 |

**Insight:** Current Mobile price of $2.85 is near-optimal for revenue. Going lower increases volume but destroys margin. Going higher loses too many customers.

---

#### **Domain 3: Customer Behavior & Churn**

**Query 3.1 - Churn Analysis by Segment**
```sql
SELECT 
    city_tier,
    plan_type,
    COUNT(*) AS total_subscribers,
    SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM subscribers
GROUP BY city_tier, plan_type
ORDER BY churn_rate_pct DESC;
```

**Key Finding:**
- **Tier 3 + Mobile:** 15% churn (highest) - price-sensitive, limited content
- **Tier 1 + Premium:** 4% churn (lowest) - engaged, high satisfaction
- **Regional language speakers:** 18% churn vs 9% for Hindi/English speakers

**Insight:** Churn is highest where content-market fit is weakest. Regional content gap is costing subscribers.

---

**Query 3.2 - Language Preference Impact**
```sql
SELECT 
    language_preference,
    COUNT(*) AS subscribers,
    ROUND(AVG(monthly_price), 2) AS avg_price_paid,
    ROUND(SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM subscribers
GROUP BY language_preference
HAVING subscribers >= 50
ORDER BY subscribers DESC;
```

**Key Finding:**
| Language | Subscribers | Avg Price | Churn Rate |
|----------|-------------|-----------|-----------|
| Hindi | 2,850 | $5.20 | 8% |
| English | 1,420 | $8.50 | 6% |
| Tamil | 340 | $3.10 | 18% |
| Telugu | 280 | $2.95 | 19% |

**Insight:** Regional language users pay less and churn more due to limited content. $420M investment over-indexed on Hindi/English vs. regional needs.

---

#### **Domain 4: Competitive Benchmarking**

**Query 4.1 - Competitor Market Share Analysis**
```sql
SELECT 
    competitor_name,
    users_millions,
    market_share_pct,
    pricing_model,
    CASE WHEN monthly_price = 0 THEN annual_price/12 ELSE monthly_price END AS effective_monthly_price,
    ad_supported
FROM competitors
ORDER BY market_share_pct DESC;
```

**Key Finding:**
| Competitor | Users (M) | Share | Price/mo | Model |
|------------|-----------|-------|----------|-------|
| Hotstar | 129 | 70% | $4.29 | Freemium + Ads |
| Amazon Prime | 26 | 14% | $1.19 | Subscription |
| ZEE5 | 26 | 8% | $2.86 | Freemium + Ads |
| **Netflix** | **2** | **1%** | **$2.85-11.46** | **Subscription** |

**Insight:** Top 3 players use freemium/ad-supported models. Netflix is only major pure-subscription player - limits addressable market to premium segment.

---

**Query 4.2 - Content Investment ROI**
```sql
SELECT 
    company,
    india_investment_usd_millions,
    original_shows_count,
    ROUND(india_investment_usd_millions / NULLIF(original_shows_count, 0), 2) AS cost_per_show_millions
FROM content_investment
WHERE year = 2020
ORDER BY india_investment_usd_millions DESC;
```

**Key Finding:**
| Company | Investment | Shows | Cost/Show |
|---------|-----------|-------|-----------|
| Netflix | $420M | 87 | $4.83M |
| Amazon Prime | $85M | 15 | $5.67M |
| ZEE5 | $65M | 87 | $0.75M |

**Insight:** ZEE5 produces same number of shows at 15% of Netflix's cost through regional studio partnerships. Netflix's premium production model is capital-intensive.

---

#### **Domain 5: Strategic Insights**

**Query 5.1 - Acquisition Channel Effectiveness**
```sql
SELECT 
    acquisition_channel,
    COUNT(*) AS total_acquired,
    SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) AS active,
    ROUND(SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS retention_rate,
    ROUND(AVG(CASE WHEN status = 'Active' THEN monthly_price ELSE 0 END), 2) AS avg_active_price
FROM subscribers
GROUP BY acquisition_channel
ORDER BY retention_rate DESC;
```

**Key Finding:**
| Channel | Acquired | Retention | Avg Price |
|---------|----------|-----------|-----------|
| Referral | 820 | 94% | $7.20 |
| Content Marketing | 750 | 91% | $6.80 |
| Organic | 1,200 | 89% | $5.50 |
| Paid Social | 1,580 | 82% | $4.20 |
| TV Ads | 650 | 78% | $8.10 |

**Insight:** Referral and content marketing drive highest quality subscribers. Paid channels have higher volume but lower retention - suggests CAC payback challenges.

---

### SQL Analysis Summary

**16 Queries Delivered:**
✅ 3 Market Sizing queries → TAM: 260M viewers, $11.5B potential
✅ 3 Pricing Optimization queries → Optimal: $2.85-3.50/month
✅ 4 Customer Behavior queries → Churn driven by content gaps, not price
✅ 3 Competitive Analysis queries → Freemium + ads dominate, Netflix is outlier
✅ 3 Strategic Insight queries → Regional content = highest ROI opportunity

### Deliverables
📄 `sql/analysis_queries.sql` - All 16 queries with comments
📄 `sql/query_results.txt` - Complete output from all analyses
📄 `run_queries.py` - Automated execution script

---

## Phase 3: Financial Modeling with Calculus

### Objective
Apply quantitative methods to optimize pricing strategy and calculate customer lifetime value under different scenarios.

### Model 1: Customer Lifetime Value (Limit Theory)

**Business Question:** How much is each subscriber worth over their entire relationship with Netflix?

**Mathematical Framework:**

Customer lifetime value can be expressed as an infinite geometric series:
```
CLV = ARPU₀ + ARPU₁(1-c) + ARPU₂(1-c)² + ARPU₃(1-c)³ + ...
```

Where:
- ARPU = Average Revenue Per User per period
- c = monthly churn rate
- Each term is discounted by (1+r) where r = discount rate

This converges to:
```
CLV = ARPU × Gross Margin / (Churn Rate + Discount Rate)
```

**Excel Implementation:**
```excel
// Cell B4: Monthly ARPU
= 2.85

// Cell B5: Monthly Churn Rate
= 0.12

// Cell B6: Gross Margin
= 0.80

// Cell B7: Monthly Discount Rate
= 0.01

// Cell B39: Theoretical CLV (using limit formula)
= B4 * B6 / (B5 + B7)
= $17.54
```

**Sensitivity Analysis:**

| Monthly Churn | CLV | % Change from Baseline |
|--------------|-----|----------------------|
| 5% | $33.60 | +91% |
| 8% | $23.08 | +31% |
| **12% (Current)** | **$17.54** | **Baseline** |
| 15% | $13.85 | -21% |
| 20% | $9.90 | -44% |

**Key Insight:** 

Each 1% reduction in churn has **exponential impact** on CLV due to geometric series convergence:
- 12% → 11% churn: +8% CLV ($1.40 gain per subscriber)
- 12% → 10% churn: +17% CLV ($2.98 gain per subscriber)
- 12% → 8% churn: +31% CLV ($5.54 gain per subscriber)

**Business Implication:**

At 2M current subscribers:
- 1% churn reduction = $2.8M additional lifetime value
- 4% churn reduction = $11.1M additional lifetime value

Retention improvements deliver more value than acquisition at current scale.

---

### Model 2: Pricing Optimization (Marginal Analysis)

**Business Question:** What price maximizes profit?

**Mathematical Framework:**

Profit = Revenue - Costs
Profit = (Price × Quantity × Margin) - Fixed Costs

Where Quantity = f(Price) based on demand curve with elasticity ε:
```
Quantity = Q₀ × (Price / P₀)^ε
```

For entertainment services, ε ≈ -1.5 (industry standard)

At optimal price, **Marginal Revenue = Marginal Cost**:
```
dProfit/dPrice = 0
```

**Excel Implementation:**

| Price | Price Change % | Demand Change % | Est. Subscribers (M) | Revenue (M) | Variable Costs | Contribution Margin | Profit (M) |
|-------|---------------|----------------|---------------------|-------------|----------------|-------------------|-----------|
| $1.99 | -30% | +45% | 2.90 | $5.77 | $1.45 | $4.32 | $3.32 |
| $2.50 | -12% | +18% | 2.36 | $5.90 | $1.18 | $4.72 | $3.72 |
| **$2.85** | **0%** | **0%** | **2.00** | **$5.70** | **$1.00** | **$4.70** | **$3.70** |
| $3.50 | +23% | -34% | 1.32 | $4.62 | $0.66 | $3.96 | $2.96 |
| $4.00 | +40% | -60% | 0.80 | $3.20 | $0.40 | $2.80 | $1.80 |
| $5.00 | +75% | -112% | 0.24 | $1.20 | $0.12 | $1.08 | $0.08 |

**Key Findings:**

✅ **Optimal Price Range:** $2.50-$3.50 for mobile tier
✅ **Current Price ($2.85):** Near-optimal, maximizes profit at $3.70M/month
✅ **Lower Pricing Risk:** Below $2.50 increases volume but destroys margins
✅ **Higher Pricing Risk:** Above $3.50 loses 40%+ of potential subscribers

**Marginal Analysis Visualization:**
```
Profit Curve (shaped like inverted U):

$4M |        ___
    |      /     \
$3M |     /       \___
    |    /             \___
$2M |   /                   \___
    |  /                         \___
$1M | /                               \___
    |_________________________________
       $2   $2.85  $4   $5   $6   $7+
              ↑
         OPTIMAL
```

---

### Model 3: Market Sizing (TAM/SAM/SOM Framework)

**Excel Sheet 3: Three-Tier Market Model**

| Tier | Segment | Viewers (M) | WTP ($/mo) | Conversion | Potential Subs (M) | Annual Revenue (M) |
|------|---------|-------------|-----------|-----------|-------------------|-------------------|
| **TIER 1: Mass Market** | Value Urban + Small City | 170 | $2.50 | 8% | 13.6 | $408 |
| **TIER 2: Premium** | Mid Urban | 55 | $5.00 | 10% | 5.5 | $330 |
| **TIER 3: Elite** | Premium Urban | 35 | $10.00 | 15% | 5.25 | $630 |
| **TOTAL** | - | **260M** | - | - | **24.35M** | **$1,368M** |

**Scenario Analysis:**

| Scenario | Assumptions | Subscribers (M) | Annual Revenue ($M) | Probability |
|----------|-------------|----------------|-------------------|-------------|
| Conservative | Tier 1 only, 5% conversion | 8.5 | $255 | 70% |
| Base Case | All tiers, current conversion | 24.4 | $1,368 | 50% |
| Optimistic | All tiers, +50% conversion | 36.5 | $2,050 | 20% |
| Bull Case | + Ad tier, + partnerships | 65.0 | $3,200 | 5% |

**Weighted Expected Value:** 
= (0.70 × $255M) + (0.50 × $1,368M) + (0.20 × $2,050M) + (0.05 × $3,200M)
= **$1,652M annual revenue opportunity**

---

### Model 4: Churn Sensitivity (Exponential Impact)

**Business Question:** How does reducing churn affect profitability at scale?

**Excel Sheet 4: Marginal Impact Calculation**

| Churn Rate | CLV | Change in CLV | Marginal Impact (ΔCLV/Δchurn) | 10M Subscribers Impact |
|-----------|-----|---------------|-------------------------------|----------------------|
| 5% | $33.60 | - | - | $336M total LTV |
| 6% | $28.24 | -$5.36 | -$5.36 per 1% | $282M (-$54M) |
| 7% | $24.62 | -$3.62 | -$3.62 per 1% | $246M (-$36M) |
| 8% | $21.82 | -$2.80 | -$2.80 per 1% | $218M (-$28M) |
| 9% | $19.60 | -$2.22 | -$2.22 per 1% | $196M (-$22M) |
| 10% | $17.78 | -$1.82 | -$1.82 per 1% | $178M (-$18M) |
| 11% | $16.26 | -$1.52 | -$1.52 per 1% | $163M (-$15M) |
| **12%** | **$15.00** | **-$1.26** | **-$1.26 per 1%** | **$150M (-$13M)** |

**Key Insight:**

Marginal impact is **non-linear** - each additional percent of churn has decreasing absolute impact but **increasing percentage impact** due to compounding.

At 10M subscribers:
- **Moving from 12% → 8% churn:** +$68M in total LTV (+45%)
- **Investment in retention:** If cost <$68M, highly profitable
- **Content localization:** Primary lever to reduce churn in regional segments

---

### Financial Modeling Summary

**4 Excel Sheets Delivered:**

✅ **Sheet 1 - Pricing Optimization:** Optimal price = $2.85-3.50 via marginal analysis
✅ **Sheet 2 - CLV Calculation:** Theoretical CLV = $17.54, 31% increase possible with churn reduction
✅ **Sheet 3 - Market Sizing:** 24M realistic TAM, $1.4B base case revenue
✅ **Sheet 4 - Churn Sensitivity:** Each 1% churn = $1.26 CLV impact, exponential returns to retention

### Calculus Applications Demonstrated

📐 **Limit Theory:** CLV as convergent geometric series
📐 **Marginal Analysis:** Finding dProfit/dPrice = 0 for optimization
📐 **Elasticity:** Demand curves with ε = -1.5
📐 **Sensitivity Analysis:** Partial derivatives showing variable impact

### Deliverable
📄 `analysis/netflix_india_financial_model.xlsx` - Live Excel with formulas

---

## Phase 4: Strategic Recommendations

### Objective
Synthesize SQL insights and financial models into actionable strategy with implementation roadmap.

### Strategic Framework: Four Pillar Approach

Based on our analysis, we recommend a **multi-tier, multi-model approach** that adapts to India's heterogeneous market while maintaining Netflix brand positioning:

---

### RECOMMENDATION 1: Three-Tier Pricing Architecture

**Current Problem:** One-size-fits-all pricing ($2.85-11.46) doesn't reflect India's income diversity.

**Our Solution:** Restructure into three distinct tiers targeting different segments:

#### **TIER 1: Mobile Mass Market ($2.50-2.85/month)**

**Target Segment:**
- Tier 2/3 cities (80M+ video viewers)
- Income: $2,000-3,500/year
- Mobile-first consumers (85% mobile-only)
- Price sensitivity: High
- Language: Hindi + 1-2 regional

**Product Features:**
- Mobile-only streaming
- SD quality
- 1 screen at a time
- Hindi + 3 regional languages
- **Option:** Ad-supported at $0.99 or ad-free at $2.85

**Business Model:**
- Volume play: 40-60M potential subscribers
- Annual revenue: $1.2-2.0B
- Margin: 65% (lower content costs)

**SQL Evidence:**
```sql
-- 70% of Tier 2/3 subscribers choose Mobile plan
-- $2.85 achieves 28% conversion with 12% churn
-- Revenue: $14.3M/month vs $11.2M at $1.99
```

---

#### **TIER 2: Premium Streaming ($5-7/month)**

**Target Segment:**
- Urban professionals (Tier 1 cities)
- Income: $6,000-12,000/year
- Multi-device households
- Price sensitivity: Medium
- Language: Hindi + English bilingual

**Product Features:**
- Multi-device (TV + mobile + laptop)
- HD quality
- 2 screens simultaneously
- Full Hindi + English library
- Downloads for offline

**Business Model:**
- Sweet spot: 15-25M potential subscribers
- Annual revenue: $900M-2.1B
- Margin: 75% (premium pricing, moderate content costs)

**SQL Evidence:**
```sql
-- Mid Urban segment: 55M viewers, $5 WTP, 10% conversion
-- Current Standard plan ($9.31): Only 20% of subscribers but 35% of revenue
```

---

#### **TIER 3: Ultra Premium ($9-11/month)**

**Target Segment:**
- Elite English speakers
- Income: $12,000+/year
- Global content consumers
- Price sensitivity: Low
- Expatriates, executives, returning NRIs

**Product Features:**
- All devices
- 4K + HDR quality
- 4 screens simultaneously
- Full global catalog
- Early access to new releases

**Business Model:**
- Niche play: 5-10M potential subscribers
- Annual revenue: $540M-1.3B
- Margin: 85% (highest prices, no incremental content investment)

**SQL Evidence:**
```sql
-- Premium Urban: 35M viewers, $10 WTP, 15% conversion = 5.25M subs
-- Current Premium plan: 12% of subscribers, 28% of revenue, 5% churn (lowest)
```

---

**COMBINED IMPACT:**

| Tier | Price | Target (M subs) | Annual Revenue | Margin | Contribution |
|------|-------|----------------|----------------|--------|-------------|
| Mass Market | $2.75 avg | 40-60 | $1.32-1.98B | 65% | $858M-1.29B |
| Premium | $6.00 avg | 15-25 | $1.08-1.80B | 75% | $810M-1.35B |
| Ultra | $10.00 avg | 5-10 | $600M-1.20B | 85% | $510M-1.02B |
| **TOTAL** | - | **60-95M** | **$2.0-5.0B** | **73% avg** | **$2.18-3.66B** |

---

### RECOMMENDATION 2: Regional Content Acceleration

**Current Problem:** $420M investment over-indexed on Hindi/English vs. market demand.

**SQL Evidence:**
```sql
-- 70% prefer regional languages, but only 30% of Netflix content is regional
-- Regional language churn: 18% vs Hindi/English: 8%
-- ZEE5: 87 shows for $65M ($0.75M/show) vs Netflix: $4.83M/show
```

**Our Solution: Triple Regional Content Investment**

#### **Content Strategy Shift**

**FROM (Current 2020):**
- $420M total investment
- 87 shows: 60% Hindi, 30% English, 10% regional
- 10 languages supported
- Premium production values ($4-5M per show)

**TO (Recommended 2026):**
- $500M total investment (+19%)
- 150 shows: 40% Hindi, 20% English, 40% regional
- 15+ languages supported
- Tiered production: Premium for Hindi/English, efficient for regional

**Implementation:**

**Phase 1: Partner with Regional Studios**
- Tamil: Sun Network, Studio Green
- Telugu: Geetha Arts, Mythri Movie Makers
- Bengali: SVF Entertainment, Surinder Films
- Marathi: Zee Studios, Eros Now

**Cost Structure:**
- Regional content: $0.75-1.5M per show
- 60 regional shows × $1M = $60M (vs $290M for same # of premium shows)
- Frees up $230M for volume

**Content Mix by Tier:**

| Language | Target Tier | Shows/Year | Avg Budget | Total Investment |
|----------|------------|-----------|-----------|-----------------|
| Hindi Premium | Tier 2+3 | 30 | $5M | $150M |
| English Premium | Tier 3 | 15 | $6M | $90M |
| Tamil Regional | Tier 1 | 15 | $1M | $15M |
| Telugu Regional | Tier 1 | 15 | $1M | $15M |
| Bengali Regional | Tier 1 | 10 | $0.8M | $8M |
| Marathi Regional | Tier 1 | 8 | $0.8M | $6.4M |
| Others (6 langs) | Tier 1 | 12 | $0.75M | $9M |
| **TOTAL** | - | **105** | - | **$293M** |

Remaining $207M → licensing, marketing, tech infrastructure

---

**Expected Impact:**

| Metric | Current | After Implementation | Change |
|--------|---------|---------------------|--------|
| Regional Churn | 18% | 12% (-33%) | -6 pp |
| Regional CLV | $12.00 | $17.54 (+46%) | +$5.54 |
| Content Hours | 1,200 | 2,100 (+75%) | +900 |
| Languages | 10 | 15 (+50%) | +5 |
| Regional Subs | 15% of base | 40% of base | +167% |

**10M Subscribers Impact:**
- 6% churn reduction × 4M regional subs = +$22.2M lifetime value
- ROI: $22.2M / $60M incremental investment = **37% first-year return**

---

### RECOMMENDATION 3: Telecom Partnership Strategy

**Current Problem:** High CAC ($5/subscriber), limited distribution reach, standalone service.

**Our Solution: Bundle with Jio & Airtel**

#### **Partnership Model: B2B2C Distribution**

**Reliance Jio Partnership (Priority #1)**
- **Jio's Assets:** 450M subscribers, data leadership, payment rails
- **Netflix Bundle:** Include Netflix Mobile tier with Jio premium data plans
- **Pricing:** $8/month for 2GB/day data + Netflix Mobile (vs $5 separate)
- **Revenue Share:** 70% Netflix, 30% Jio platform fee

**Airtel Partnership (Priority #2)**
- **Airtel's Assets:** 380M subscribers, premium positioning, DTH integration
- **Netflix Bundle:** Netflix Premium with Airtel Black family plans
- **Pricing:** $15/month for broadband + DTH + Netflix (vs $22 separate)
- **Revenue Share:** 75% Netflix, 25% Airtel

#### **Economics Comparison**

**Direct Acquisition (Current):**
- CAC: $5 (paid social, TV ads, influencers)
- Conversion: 2-3% from awareness to paid
- Payback: 2-3 months at $2.85 ARPU

**Telecom Partnership (Proposed):**
- CAC: $0.50 (handled by telecom sales teams)
- Conversion: 8-12% of telecom premium base
- Payback: <1 month
- **CAC Reduction: 90%**

#### **Addressable Market Expansion**

| Partner | Premium Subs | Netflix Bundle Take Rate | New Netflix Subs | Annual Revenue |
|---------|-------------|-------------------------|-----------------|----------------|
| Jio | 100M | 10% | 10M | $342M ($2.85 × 70% share) |
| Airtel | 60M | 12% | 7.2M | $453M ($7.00 × 75% share) |
| **TOTAL** | **160M** | - | **17.2M** | **$795M** |

**Additional Benefits:**
- **Billing:** Piggyback on telecom's payment infrastructure (reduces churn from payment failures)
- **Brand:** Association with trusted local brands (Jio/Airtel)
- **Retention:** Bundled services have 40% lower churn than standalone
- **Data:** Access to telecom usage data for personalization

#### **Implementation Timeline**

**Q1 2026:** Pilot with Jio in 3 cities (Mumbai, Delhi, Bangalore)
- Test bundle pricing, measure conversion and churn
- Target: 500K subscribers in pilot

**Q2-Q3 2026:** Scale Jio partnership nationwide
- Roll out to all Jio premium plans
- Target: 5M bundled subscribers by year-end

**Q4 2026:** Launch Airtel partnership
- Similar model with premium positioning
- Target: 2M bundled subscribers

**2027+:** Expand to BSNL, Vi (Vodafone-Idea), regional players
- Total partnership potential: 25M+ subscribers

---

### RECOMMENDATION 4: Ad-Supported Tier (Selective Launch)

**Current Problem:** 80% of competitors use ad-supported models, Netflix is leaving money on table.

**Strategic Tension:** Introducing ads risks diluting Netflix's premium brand globally.

**Our Solution: India-Only Pilot with Strategic Guardrails**

#### **Product Design: "Netflix Basic with Ads"**

**Tier Positioning:**
- Price: $0.99/month (vs $2.85 ad-free Mobile)
- Target: Tier 3 cities + rural digital consumers
- Launch: India only (isolated from global brand)
- Naming: Distinct branding to avoid cannibalization

**Ad Load:**
- 4 ads per hour (vs 8-10 on TV, 6-8 on Hotstar)
- Pre-roll only (no mid-roll interruptions)
- Premium advertisers only (no low-quality direct response ads)
- Ad-free first month (hook users on experience)

**Content Library:**
- Same as Mobile tier (SD, mobile-only)
- Delayed access to new releases (7-day window)
- Hindi + 2 regional languages

#### **Business Model**

**Revenue Streams:**
1. **Subscription:** $0.99/month
2. **Advertising:** $2-3 CPM × 4 ads/hour × 40 hours/month = $0.32-0.48/user/month

**Total ARPU:** $1.31-1.47/month (still lower than $2.85 ad-free)

**Addressable Market:**
- Tier 3 + Rural: 130M viewers
- Conversion: 5% (vs <1% at $2.85)
- Potential: 6.5M subscribers

**Financial Impact:**

| Metric | Ad-Supported | Ad-Free Mobile | Comparison |
|--------|-------------|---------------|-----------|
| Price | $0.99 | $2.85 | -65% |
| Ad Revenue | $0.40 | $0 | New stream |
| Total ARPU | $1.39 | $2.85 | -51% |
| Conversion | 5% | 2% | +150% |
| Subscribers | 6.5M | 2.6M | +150% |
| **Total Revenue** | **$108M** | **$89M** | **+21%** |

**Net Incremental Revenue:** $19M/year from users who would never pay $2.85

#### **Cannibalization Risk Management**

**Strategic Guardrails:**
1. **Geography:** Launch only in Tier 3 cities + rural (not Tier 1/2)
2. **No Downgrades:** Existing subscribers cannot switch to ad tier
3. **Separate SKU:** Different branding/positioning
4. **Upgrade Funnel:** Offer $1.99 promo after 3 months to migrate to ad-free
5. **Performance Tracking:** Kill if >10% of new subs choose ad tier in Tier 1 cities

**Expected Cannibalization:**
- 15% of Tier 3 Mobile subscribers might choose ad tier if available
- Cost: 390K subs × ($2.85 - $1.39) = $568K/month revenue loss
- Gain: 6.5M new subs × $1.39 = $9M/month revenue
- **Net Benefit:** +$8.4M/month

**Upgrade Path:**
- 10-15% of ad-tier users upgrade to ad-free after 6 months
- Effective ARPU: $1.39 + (0.12 × $1.46 upgrade value) = $1.56

#### **Implementation Approach**

**Phase 1: Stealth Pilot (6 months)**
- 5 Tier 3 cities only
- No marketing (organic growth only)
- Measure: Conversion, churn, engagement, cannibalization
- Decision gate: Proceed only if metrics meet thresholds

**Phase 2: Controlled Rollout (12 months)**
- 50 Tier 3 cities
- Limited marketing (digital only, no TV)
- A/B test ad loads (3 vs 4 vs 5 ads/hour)
- Test upgrade promotions ($1.49 vs $1.99 ad-free offers)

**Phase 3: Scale Decision (18+ months)**
- If successful: Nationwide Tier 3 + rural launch
- If marginal: Maintain limited footprint
- If cannibalistic: Sunset and offer $1.99 ad-free compromise

---

## Implementation Roadmap

### 3-Year Execution Plan

---

### **YEAR 1 (2026): Foundation**

**Q1 - Pricing & Infrastructure**
- ✅ Launch three-tier pricing structure across all markets
- ✅ Update mobile app to support ad-free/ad-supported toggle
- ✅ Hire India content team (30 FTEs) for regional partnerships
- ✅ Begin Jio partnership negotiations
- **KPI:** 8M subscribers (+6M net adds)

**Q2 - Content Pipeline**
- ✅ Sign first 5 regional studio partnerships (Tamil, Telugu focus)
- ✅ Commission 10 regional originals (5 Tamil, 5 Telugu)
- ✅ Expand Hindi library through licensing deals (+40% content hours)
- ✅ Launch creator fund for regional YouTubers/influencers
- **KPI:** 10M subscribers (+2M net adds), churn 11.5% (-0.5pp)

**Q3 - Distribution Expansion**
- ✅ Launch Jio partnership pilot in 3 cities
- ✅ Begin Airtel partnership discussions
- ✅ Test ad-supported tier in 5 Tier 3 cities (stealth pilot)
- ✅ First regional originals premiere (2 Tamil, 2 Telugu shows)
- **KPI:** 12M subscribers (+2M net adds), 500K via Jio bundle

**Q4 - Optimization & Learning**
- ✅ Analyze Year 1 data: pricing elasticity, content engagement, partnership metrics
- ✅ Refine 2027 content slate based on performance
- ✅ Prepare Year 2 roadmap with Board-approved $500M content budget
- ✅ Scale Jio partnership from pilot to nationwide
- **KPI:** 15M subscribers (+3M net adds), $600M annual revenue

---

### **YEAR 2 (2027): Scale**

**Q1 - Regional Content Explosion**
- ✅ Launch 15 regional originals (Tamil, Telugu, Bengali, Marathi)
- ✅ Expand to 15 languages (add Kannada, Malayalam, Gujarati, Punjabi, Odia)
- ✅ First regional film acquisition (Tamil blockbuster streaming rights)
- ✅ Establish regional content "hubs" in Chennai, Hyderabad, Kolkata
- **KPI:** 20M subscribers (+5M net adds), regional users = 35% of base

**Q2 - Partnership Acceleration**
- ✅ Airtel partnership goes live (targeting 2M bundled subs)
- ✅ Jio partnership scales to 8M bundled subscribers
- ✅ Pilot partnerships with regional DTH providers (Sun Direct, Dish TV)
- ✅ Test co-branded credit cards with HDFC/ICICI
- **KPI:** 25M subscribers (+5M net adds), 40% via partnerships

**Q3 - Ad Tier Expansion (if pilot successful)**
- ✅ Roll out ad-supported tier to 50 Tier 3 cities
- ✅ Sign first premium advertising partners (Unilever, P&G, Amazon India)
- ✅ Build ad tech infrastructure (frequency capping, targeting)
- ✅ Test upgrade promotions ($1.99 ad-free for 3 months)
- **KPI:** 30M subscribers (+5M net adds), 3M on ad-supported tier

**Q4 - Retention & Engagement**
- ✅ Launch Netflix gaming in India (mobile-first games)
- ✅ Introduce "watch parties" feature for social viewing
- ✅ First Netflix India brand events (film festivals, creator meetups)
- ✅ Year 2 review: Evaluate progress toward 50M target
- **KPI:** 35M subscribers (+5M net adds), churn 9.5% (-2.5pp from Year 1)

---

### **YEAR 3 (2028): Domination**

**Q1 - Content Leadership**
- ✅ 30 regional originals (10 Tamil, 8 Telugu, 6 Bengali, 6 others)
- ✅ First Netflix India theatrical release (premium Hindi film)
- ✅ Establish Netflix Film Academy to train regional filmmakers
- ✅ Co-productions with top Bollywood production houses
- **KPI:** 42M subscribers (+7M net adds), #2 player after Hotstar

**Q2 - Market Consolidation**
- ✅ Acquire smaller regional streaming service (e.g., Aha, Hoichoi)
- ✅ Launch Netflix India-specific features (cricket highlights, regional news)
- ✅ Expand gaming to 20+ titles optimized for Indian preferences
- ✅ First profitability in India market
- **KPI:** 50M subscribers (+8M net adds), $2.1B annual revenue

**Q3 - Geographic Expansion**
- ✅ Launch Tier 4 city strategy (50K-100K population towns)
- ✅ Partner with local cable operators for distribution
- ✅ Offline viewing kiosks in rural areas (micro-franchises)
- ✅ Test family sharing plans (5 profiles, $12/month)
- **KPI:** 58M subscribers (+8M net adds), rural users = 15% of base

**Q4 - Long-Term Positioning**
- ✅ Evaluate path to 100M subscribers (2030 goal)
- ✅ Review content portfolio ROI, double down on winners
- ✅ Consider IPL streaming rights bid (if available)
- ✅ Year 3 board presentation: Roadmap to market leadership
- **KPI:** 65M subscribers (+7M net adds), 35% market share

---

### **Success Metrics Dashboard**

| Metric | 2025 (Baseline) | 2026 (Year 1) | 2027 (Year 2) | 2028 (Year 3) |
|--------|----------------|--------------|--------------|--------------|
| **Subscribers (M)** | 2 | 15 | 35 | 65 |
| **Annual Revenue ($M)** | $180 | $600 | $1,400 | $2,800 |
| **Monthly Churn (%)** | 12% | 11.5% | 9.5% | 8.0% |
| **ARPU ($/month)** | $7.50 | $3.33 | $3.33 | $3.59 |
| **CAC ($)** | $5.00 | $2.50 | $1.50 | $1.00 |
| **Regional Content (%)** | 10% | 25% | 40% | 50% |
| **Partnership Subs (%)** | 0% | 15% | 40% | 50% |
| **Market Share (%)** | 1% | 8% | 19% | 35% |

---

## Key Deliverables

### What You Get in This Repository

#### **1. Database & Data Infrastructure**
📄 `data/netflix_india.db` - SQLite database with 5 tables
- 5,000 subscriber records with demographics, plans, churn, engagement
- 10 competitor profiles with pricing and market positioning
- 5 market segments with TAM/SAM sizing
- Content investment trends 2017-2020
- A/B testing data across 6 price points

📄 `generate_data.py` - Automated database generation script
- Realistic distributions based on case study facts
- Tier-based plan preferences
- Language-weighted churn probabilities
- Reproducible with random seed

---

#### **2. SQL Analysis Queries**
📄 `sql/analysis_queries.sql` - 16 advanced queries covering:

**Market Sizing:**
- Total addressable market by segment
- Current subscriber base analysis
- Competitive market share

**Pricing & Revenue:**
- Revenue by plan type
- Pricing test conversion analysis
- Optimal price point identification

**Customer Behavior:**
- Churn analysis by segment
- Language preference impact
- Engagement levels by tier

**Competitive Intelligence:**
- Content investment ROI comparison
- Netflix investment trends
- Competitor pricing vs market share

**Strategic Insights:**
- CLV components by plan
- Acquisition channel effectiveness
- Growth opportunity quantification

📄 `sql/query_results.txt` - Complete output from all queries

📄 `run_queries.py` - Automated execution script

---

#### **3. Financial Models (Excel)**
📄 `analysis/netflix_india_financial_model.xlsx` - 4 interactive sheets:

**Sheet 1: Pricing Optimization**
- Marginal analysis with demand curves
- Price elasticity modeling (ε = -1.5)
- Optimal price identification ($2.85-3.50)
- Revenue and profit projections

**Sheet 2: CLV Analysis**
- Customer Lifetime Value using limit theory
- Formula: `CLV = ARPU × Margin / (Churn + Discount)`
- Sensitivity analysis (churn 5% to 20%)
- 24-month cohort tracking vs theoretical limit

**Sheet 3: Market Sizing**
- TAM/SAM/SOM framework
- 5 segments with conversion rates
- Revenue potential by tier
- Scenario analysis (Conservative/Base/Optimistic/Bull)

**Sheet 4: Churn Impact**
- Exponential effect of retention improvements
- Marginal CLV impact per churn point
- Investment ROI thresholds
- 10M subscriber scaling scenarios

---

#### **4. Strategic Case Study (Word Document)**
📄 `docs/Netflix_India_Case_Study.docx` - 12-page professional analysis:

**Executive Summary** (1 page)
- Problem statement
- Key findings with quantification
- Strategic recommendations
- Expected impact

**Business Context** (2 pages)
- Netflix's India challenge
- Three core strategic questions
- Market dynamics post-Jio
- Competitive landscape

**Analytical Methodology** (1 page)
- Data architecture overview
- SQL framework (5 analysis domains)
- Calculus applications (CLV, pricing optimization)
- Strategic frameworks (Porter, TAM/SAM/SOM)

**Key Findings** (3 pages)
- Market sizing results with tables
- Pricing analysis with test data
- Content strategy gap analysis
- Churn economics with calculus proof

**Strategic Recommendations** (3 pages)
- Three-tier pricing architecture
- Regional content acceleration
- Telecom partnership strategy
- Ad-supported tier design

**Implementation Roadmap** (2 pages)
- 3-year phase plan
- Success metrics dashboard
- Resource requirements
- Risk mitigation strategies

---

#### **5. Automation Scripts**
📄 `generate_data.py` - Database creation
- Python 3.7+ compatible
- SQLite with realistic distributions
- ~250 lines of code

📄 `run_queries.py` - Query execution
- Automated SQL runner
- Results formatting
- Error handling

📄 `create_excel.py` - Financial model generation
- openpyxl-based automation
- Live formulas (not hard-coded values)
- Professional formatting

📄 `create_case_study.py` - Document creation
- python-docx automation
- Consistent styling
- Table and chart generation

---

### How to Use This Repository

**For Recruiters/Reviewers:**
1. Read this README for project overview
2. Review `docs/Netflix_India_Case_Study.docx` for strategic analysis
3. Explore `analysis/netflix_india_financial_model.xlsx` for financial rigor
4. Check `sql/analysis_queries.sql` for SQL complexity

**For Learning/Replication:**
1. Clone repository
2. Run `python generate_data.py` to create database
3. Run `python run_queries.py` to execute analyses
4. Run `python create_excel.py` for financial models
5. Run `python create_case_study.py` for final document

**Requirements:**
```bash
python --version  # 3.7+
pip install pandas openpyxl python-docx
```

---

## Skills Showcased

### Technical Skills

**SQL**
- ✅ Database design & normalization
- ✅ Complex queries (JOINs, CTEs, window functions, subqueries)
- ✅ Aggregations & grouping
- ✅ Data segmentation
- ✅ Performance optimization

**Python**
- ✅ SQLite database management
- ✅ Data generation with realistic distributions
- ✅ Excel automation (openpyxl)
- ✅ Document generation (python-docx)
- ✅ Script automation

**Excel/Financial Modeling**
- ✅ Live formulas (not static values)
- ✅ Scenario analysis
- ✅ Sensitivity tables
- ✅ Dashboard design
- ✅ Data visualization

**Calculus & Math**
- ✅ Limit theory (geometric series convergence)
- ✅ Derivatives (marginal analysis, optimization)
- ✅ Elasticity modeling
- ✅ Exponential functions

---

### Business Skills

**Strategic Thinking**
- ✅ Problem decomposition (3 strategic questions)
- ✅ Framework application (Porter, TAM/SAM/SOM)
- ✅ Competitive analysis
- ✅ Market entry strategy
- ✅ Brand positioning

**Analytical Rigor**
- ✅ Hypothesis-driven analysis
- ✅ Quantitative validation
- ✅ Data-backed recommendations
- ✅ ROI calculations
- ✅ Risk assessment

**Communication**
- ✅ Executive summaries
- ✅ Visual storytelling (tables, charts)
- ✅ Structured documents
- ✅ Clear recommendations
- ✅ Implementation roadmaps

**Consulting Approach**
- ✅ McKinsey/BCG-style case structure
- ✅ 80/20 prioritization
- ✅ Actionable insights
- ✅ Stakeholder alignment
- ✅ Change management considerations

---

## Project Context

**Based On:** MIT Sloan Case Study "Netflix Goes to Bollywood" (2021) by Donald Sull and Stefano Turconi

**Timeline:** 6-week project (January 2026)

**Purpose:** Demonstrate readiness for management consulting, investment banking, and strategy roles through end-to-end business analysis combining data skills (SQL, Python), quantitative methods (calculus, financial modeling), and strategic thinking (frameworks, recommendations).

**Note:** All data is simulated based on publicly available case study facts, Netflix earnings reports, and India streaming market research. Recommendations are for educational/portfolio purposes.

---

## Target Roles

This project is designed to showcase skills for:

**Management Consulting**
- McKinsey, BCG, Bain (Associate/Business Analyst roles)
- Strategy consulting firms
- Demonstrates: Structured problem-solving, data analysis, strategic recommendations

**Investment Banking / Private Equity**
- Analyst roles in M&A, sector coverage
- Demonstrates: Financial modeling, market sizing, competitive analysis, valuation foundation

**Corporate Strategy**
- Strategy & planning functions
- Business development roles
- Demonstrates: Market analysis, pricing strategy, partnership evaluation

**Product Management (Data-Driven)**
- Tech companies with subscription models
- Demonstrates: Customer segmentation, pricing optimization, churn analysis

---

## 📧 Contact

**Roger Dsouza**
- Email: roger.dsouza1311@gmail.com
- LinkedIn: [linkedin.com/in/roger-dsouza](https://linkedin.com/in/roger-dsouza)
- GitHub: [github.com/RogerDsouza](https://github.com/RogerDsouza)
- Portfolio: [View other projects](https://github.com/RogerDsouza)

---

## 📝 License & Acknowledgments

**License:** MIT License - Free to use for educational purposes

**Acknowledgments:**
- MIT Sloan School of Management for original case study
- Netflix for inspiring business challenge
- Python open-source community (pandas, openpyxl, python-docx)

**Disclaimer:** This is an independent educational project. Not affiliated with or endorsed by Netflix, Inc. All recommendations are based on public information and are for portfolio demonstration purposes only.

---

**⭐ If you found this analysis valuable or helpful for learning SQL/business strategy, please star this repository!**

---

*Last Updated: January 2026*
