# Interview Preparation Guide

This introductory module prepares you for coding interviews with a systematic approach to problem-solving and data structure selection.

## What's Included

### 1. `interview_guide.py`
Comprehensive guide covering:
- **Data Structure Interview Frequency** - Which structures appear most in interviews
- **7-Step Problem-Solving Framework** - Systematic approach to any coding problem
- **Pattern Recognition** - How to identify which data structure/algorithm to use
- **Common Pitfalls** - What to avoid during interviews
- **30-Day Prep Roadmap** - Structured learning path

### 2. `quick_reference.md`
One-page cheat sheet with:
- Problem pattern → Data structure mapping
- Time/space complexity reference
- Common interview patterns
- Edge cases checklist

### 3. `problem_breakdown_template.md`
Blank template for practicing the 7-step framework on any problem.

## How to Use This Guide

### First Time Setup (30-45 minutes)
1. **Read** `interview_guide.py` completely
   ```bash
   # Open in your editor or run to see practice problems
   python interview_guide.py
   ```

2. **Review** the data structure frequency ratings
   - Focus on ⭐⭐⭐⭐⭐ rated structures first
   - Understand WHY each structure is important

3. **Learn** the 7-Step Framework
   - Understand → Examples → Pattern → Breakdown → Complexity → Code → Test
   - This framework works for ANY coding problem

4. **Practice** with the included problems
   - Work through `practice_problem_1()` manually first
   - Then compare with the solution

### Before Every Interview (10 minutes)
- Review `quick_reference.md` cheat sheet
- Remind yourself of the 7-step framework
- Practice thinking out loud

### During Problem Practice (Always)
- Use `problem_breakdown_template.md` for each new problem
- Force yourself to complete Steps 1-5 BEFORE coding
- Time yourself to build speed

## The 7-Step Framework (Quick Reference)

```
1. UNDERSTAND (2-3 min)    → What are inputs/outputs/constraints?
2. EXAMPLES (2-3 min)      → Work through 2-3 concrete cases
3. PATTERN (2-3 min)       → Which algorithm/DS applies?
4. BREAKDOWN (3-5 min)     → Write pseudocode/plan
5. COMPLEXITY (1-2 min)    → Analyze time/space trade-offs
6. CODE (10-15 min)        → Implement the solution
7. TEST (3-5 min)          → Verify with test cases
```

**Total: ~25-35 minutes per problem** (typical interview length)

## Data Structure Priority

### Must Master (Do These First)
1. **Lists/Arrays** - 70% of problems
2. **Strings** - 60% of problems
3. **Hash Maps/Sets** - 65% of problems
4. **Stacks** - 40% of problems
5. **Queues** - 35% of problems
6. **Binary Trees** - 45% of problems

### Important (Do These Second)
7. **Linked Lists** - 30% of problems
8. **Heaps** - 25% of problems
9. **Graphs** - 30% of senior interviews

### Advanced (Nice to Have)
10. **Tries** - 15% of problems
11. **Deques** - Specialized tool
12. **Tuples** - Supporting role

## 30-Day Roadmap

- **Week 1**: Arrays, Strings, Hash Maps (foundations)
- **Week 2**: Stacks, Queues, Linked Lists (sequential)
- **Week 3**: Trees, Heaps, Graphs (hierarchical)
- **Week 4**: Advanced topics + Mock interviews

**Daily commitment**: 2-3 hours
**Weekly goal**: Master 2-3 data structures

## Tips for Success

✅ **DO:**
- Spend time understanding before coding
- Think out loud during interviews
- Start with brute force, then optimize
- Test with edge cases
- Ask clarifying questions

❌ **DON'T:**
- Start coding immediately
- Stay silent while thinking
- Memorize solutions
- Ignore edge cases
- Give up when stuck

## Next Steps

1. ✅ Complete this introduction module
2. → Start with `01_strings` lesson
3. → Follow the 30-day roadmap
4. → Practice 2-3 problems daily
5. → Review patterns weekly

## Quick Problem-Solving Tips

**Stuck on a problem?**
1. Re-read the problem (did you miss something?)
2. Try more examples (spot a pattern?)
3. Ask yourself: "Have I seen something similar?"
4. Consider: Could a different data structure help?
5. Start with brute force (then optimize)

**Can't identify the pattern?**
- Look for keywords: "find pair" → hash map, "balanced" → stack
- Check constraints: sorted? → binary search, unweighted graph? → BFS
- Ask: "What's the bottleneck?" → Optimize that part

**Code not working?**
- Test with simple example step-by-step
- Check off-by-one errors (< vs <=)
- Verify edge cases (empty, single element)
- Print intermediate values

---

**Remember**: Interview success comes from:
1. **Pattern recognition** (knowing which tool to use)
2. **Systematic approach** (following the framework)
3. **Practice** (applying it repeatedly)

You've got this! 🚀
