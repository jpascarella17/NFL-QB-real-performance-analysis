# NFL QB Real Performance Analysis

This project analyzes **NFL quarterbacks** using a **context-adjusted QBScore**, which evaluates performance beyond traditional passer rating by incorporating efficiency, turnovers, rushing ability, and offensive line quality. It identifies overperformers and underperformers relative to conventional metrics and highlights which QBs are truly excelling in context.

---

## Project Overview
Traditional passer rating often fails to capture the complete picture because it doesn’t account for:
- Offensive line quality
- Sack rate
- Rushing contributions

(All stats are from the 2025 NFL Season up until Week 10)

This project creates a **composite QBScore** using weighted, normalized stats to account for these factors and rank QBs more fairly.

---

## Methodology
1. **Normalize Stats**  
   - All stats are normalized between 0 and 1.  
   - Stats where lower is better (e.g., INT, Sack Rate) are inverted.  

2. **Weighted QBScore**  
   Weights reflect importance of each stat:

| Stat                  | Weight |
|--------------------------------|
| Yards per Attempt (Y/A) | 0.25 |
| Passing TDs             | 0.15 |
| Interceptions (INT)     | 0.20 |
| Passer Rating           | 0.12 |
| Rushing Yards           | 0.07 |
| Rushing TDs             | 0.07 |
| Sack Rate               | 0.12 |
| OL Rank                 | 0.12 |
| Passing Yards           | 0.12 |

3. **Rank QBs**  
   - QBs are ranked by both **Passer Rating** and **context-adjusted QBScore**.  
   - Differences in ranks identify **overperformers** and **underperformers**.

4. **Visualization**  
   - Scatter plot of Passer Rating vs QBScore
   - Trend line indicates expected QBScore based on Passer Rating  
   - Annotated QB names for clarity  
   - Top improved/worsened QBs highlighted with arrows and tables  

---

## Results

### Top Improvements (relative to Passer Rating)
| QB | Rank Difference |
|----|----------------|
| Trevor Lawrence | +11 |
| Michael Penix   | +8 |
| Justin Herbert  | +7 |
| Caleb Williams  | +7 |
| Bo Nix          | +6 |

**Interpretation:**  
- These QBs outperform what their traditional passer rating suggests.  
- Trevor Lawrence (+11) shows strong efficiency, low turnovers, and success in context even if raw stats aren’t the highest.  
- Michael Penix (+8) and Justin Herbert (+7) excel under pressure or behind weaker offensive lines.  
- Running QBs with modest rushing contributions still rank highly due to efficiency.  
- Overall, these players are **hidden gems whose real value exceeds traditional metrics**.

---

### Top Declines (relative to Passer Rating)
| QB | Rank Difference |
|----|----------------|
| Aaron Rodgers   | -12 |
| Kyler Murray    | -10 |
| Mac Jones       | -7 |
| Carson Wentz    | -7 |
| Tua Tagovailoa  | -6 |

**Interpretation:**  
- These QBs appear strong in traditional passer rating but underperform when context is considered.  
- Aaron Rodgers (-12) is likely affected by turnovers, sack pressure, or suboptimal offensive line performance.  
- Kyler Murray (-10) demonstrates that even elite athleticism may be outweighed by inefficiencies.  
- Mac Jones, Carson Wentz, and Tua Tagovailoa show that traditional stats can mask struggles under pressure or with weaker lines.  
- Highlights the **importance of context** in evaluating true quarterback performance.


