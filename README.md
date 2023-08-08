# sdc.broadband.acs

## Graph
```mermaid
graph LR;
  year=2021-->ACS;
  ACS--B19013_001-->B19013_001["MEDIAN HOUSEHOLD INCOME IN THE PAST 12 MONTHS <br/>(IN 2021 INFLATION-ADJUSTED DOLLARS)"];
  ACS--B28002_001-->B28002_001["PRESENCE AND TYPES OF INTERNET <br/> SUBSCRIPTIONS IN HOUSEHOLD"];
  ACS--B28001_002-->B28001_002["Estimate!!Total:!!<br/>Has one or more types of computing devices:"];
  ACS--B28002_004-->B28002_004["Estimate!!Total:!!<br/>With an Internet subscription!!Broadband of any type"];
  ACS--B28002_007-->B28002_007["Estimate!!Total:!!With an Internet subscription!!</br>Broadband such as cable, fiber optic or DSL"];
  ACS--B28002_013-->B28002_013["Estimate!!Total:!!No Internet access"];
```
  
## General notes
- Can check for the variable descriptions [here](https://api.census.gov/data/2021/acs/acs1/groups/B28002.html)
- Different ACS estimate annotation value:

| Estimate Value | Annotation Value | Meaning |
| --- | --- | --- |
| -666666666 | -   | The estimate could not be computed because there were an insufficient number of sample observations. For a ratio of medians estimate, one or both of the median estimates falls in the lowest interval or highest interval of an open-ended distribution. The estimate could not be computed because there were an insufficient number of sample observations. For a ratio of medians estimate, one or both of the median estimates falls in the lowest interval or highest interval of an open-ended distribution. For a 5-year median estimate, the margin of error associated with a median was larger than the median itself. |
| -999999999 | N   | The estimate or margin of error cannot be displayed because there were an insufficient number of sample cases in the selected geographic area. |
| -888888888 | (X) | The estimate or margin of error is not applicable or not available. |
| Varies | median- | The median falls in the lowest interval of an open-ended distribution (for example "2,500-") |
| Varies | median+ | The median falls in the highest interval of an open-ended distribution (for example "250,000+"). |
| -222222222 | **  | The margin of error could not be computed because there were an insufficient number of sample observations. |
| -333333333 | \*\*\* | The margin of error could not be computed because the median falls in the lowest interval or highest interval of an open-ended distribution. |
| -555555555 | \*\*\*\*\* | A margin of error is not appropriate because the corresponding estimate is controlled to an independent population or housing estimate. Effectively, the corresponding estimate has no sampling error and the margin of error may be treated as zero. |
| *   | N/A | An * indicates that the estimate is significantly different (at a 90% confidence level) than the estimate from the most current year. A "c" indicates the estimates for that year and the current year are both controlled; a statistical test is not appropriate. |
| null | null | A null value in the estimate means there is no data available for the requested geography. |
