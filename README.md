# sdc.broadband.acs

## General notes
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
